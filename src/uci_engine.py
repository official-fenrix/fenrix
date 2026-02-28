import sys, os, gzip, base64, tempfile, atexit
from ctypes import *
import chess, chess.polyglot
import time

# ==============================
# تحميل الموارد من الذاكرة
# ==============================
import resources

_temp_files = []

def load_resource_to_tempfile(encoded_data, suffix=""):
    raw = gzip.decompress(base64.b85decode(encoded_data))
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    tmp.write(raw)
    tmp.close()
    _temp_files.append(tmp.name)
    return tmp.name

def cleanup():
    for f in _temp_files:
        try: os.unlink(f)
        except: pass

atexit.register(cleanup)

_dll_path  = load_resource_to_tempfile(resources.nnueprobe_dll,        suffix=".dll")
_nnue_path = load_resource_to_tempfile(resources.nn_04cf2b4ed1da_nnue, suffix=".nnue")
_book_path = load_resource_to_tempfile(resources.book_bin,             suffix=".bin")

nnue = cdll.LoadLibrary(_dll_path)
nnue.nnue_init(_nnue_path.encode())
nnue.nnue_evaluate_fen.restype  = c_int
nnue.nnue_evaluate_fen.argtypes = [c_char_p]

BOOK_PATH = _book_path

# ==============================
# جداول التحسين
# ==============================
TT           = {}
TT_EXACT     = 0
TT_LOWER     = 1
TT_UPPER     = 2
MAX_TT_SIZE  = 500_000
KILLER_MOVES = [[None, None] for _ in range(64)]
HISTORY      = {}

# ==============================
# Opening Book
# ==============================
def book_move(board):
    try:
        with chess.polyglot.open_reader(BOOK_PATH) as reader:
            return reader.weighted_choice(board).move
    except:
        return None

# ==============================
# التقييم
# ==============================
def evaluate(board):
    return nnue.nnue_evaluate_fen(board.fen().encode())

# ==============================
# Move Ordering
# ==============================
def order_moves(board, ply, tt_move=None):
    def move_score(move):
        if tt_move and move == tt_move: return 20000
        if move.promotion:              return 15000
        if board.is_capture(move):
            v  = board.piece_at(move.to_square)
            a  = board.piece_at(move.from_square)
            vt = v.piece_type if v else 0
            at = a.piece_type if a else 0
            return 10000 + 10 * vt - at
        killers = KILLER_MOVES[ply] if ply < 64 else [None, None]
        if move == killers[0]: return 9000
        if move == killers[1]: return 8000
        return HISTORY.get((board.turn, move.from_square, move.to_square), 0)
    return sorted(board.legal_moves, key=move_score, reverse=True)

def store_killer(move, ply):
    if ply < 64 and move != KILLER_MOVES[ply][0]:
        KILLER_MOVES[ply][1] = KILLER_MOVES[ply][0]
        KILLER_MOVES[ply][0] = move

def update_history(board, move, depth):
    key = (board.turn, move.from_square, move.to_square)
    HISTORY[key] = HISTORY.get(key, 0) + depth * depth

# ==============================
# Negamax
# ==============================
def negamax(board, depth, alpha, beta, ply=0, null_allowed=True):
    # ✅ صحيح
    key = chess.polyglot.zobrist_hash(board)

    tt_move = None
    if key in TT:
        tt_depth, tt_score, tt_flag, tt_mv = TT[key]
        tt_move = tt_mv
        if tt_depth >= depth:
            if   tt_flag == TT_EXACT: return tt_score
            elif tt_flag == TT_LOWER: alpha = max(alpha, tt_score)
            elif tt_flag == TT_UPPER: beta  = min(beta,  tt_score)
            if alpha >= beta: return tt_score

    if board.is_game_over():
        return -100000 + ply if board.is_checkmate() else 0
    if depth <= 0:
        return evaluate(board)

    in_check = board.is_check()

    if null_allowed and not in_check and depth >= 3 and ply > 0:
        board.push(chess.Move.null())
        null_score = -negamax(board, depth - 3, -beta, -beta + 1, ply + 1, False)
        board.pop()
        if null_score >= beta:
            return beta

    original_alpha  = alpha
    best_score      = -float("inf")
    best_move_found = None
    moves_searched  = 0

    for move in order_moves(board, ply, tt_move):
        was_capture = board.is_capture(move)
        board.push(move)
        moves_searched += 1
        gives_check = board.is_check()

        if (moves_searched > 3 and depth >= 3
                and not in_check and not gives_check
                and not was_capture and not move.promotion):
            reduction = 1 if moves_searched <= 6 else 2
            score = -negamax(board, depth - 1 - reduction, -alpha - 1, -alpha, ply + 1)
            if score > alpha:
                score = -negamax(board, depth - 1, -beta, -alpha, ply + 1)
        else:
            score = -negamax(board, depth - 1, -beta, -alpha, ply + 1)

        board.pop()

        if score > best_score:
            best_score      = score
            best_move_found = move
        alpha = max(alpha, score)
        if alpha >= beta:
            if not was_capture:
                store_killer(move, ply)
                update_history(board, move, depth)
            break

    if len(TT) < MAX_TT_SIZE:
        flag = (TT_EXACT if original_alpha < best_score < beta
                else TT_LOWER if best_score >= beta
                else TT_UPPER)
        TT[key] = (depth, best_score, flag, best_move_found)

    return best_score

# ==============================
# Adaptive Time Management
# ==============================
def parse_time(line, board):
    parts = line.split()
    wtime = btime = winc = binc = movestogo = movetime = 0

    try:
        if "movetime" in parts:
            t = int(parts[parts.index("movetime") + 1]) / 1000.0
            return t, _depth_for_time(t)
        if "wtime"     in parts: wtime     = int(parts[parts.index("wtime")     + 1])
        if "btime"     in parts: btime     = int(parts[parts.index("btime")     + 1])
        if "winc"      in parts: winc      = int(parts[parts.index("winc")      + 1])
        if "binc"      in parts: binc      = int(parts[parts.index("binc")      + 1])
        if "movestogo" in parts: movestogo = int(parts[parts.index("movestogo") + 1])
    except:
        return 3.0, 5

    my_time = wtime if board.turn == chess.WHITE else btime
    my_inc  = winc  if board.turn == chess.WHITE else binc

    if my_time == 0:
        return 3.0, 5

    moves_left    = movestogo if movestogo > 0 else 40
    time_for_move = (my_time / moves_left) + my_inc * 0.8
    time_for_move = max(50, min(time_for_move, my_time * 0.15))
    time_sec      = time_for_move / 1000.0

    return time_sec, _depth_for_time(time_sec)

def _depth_for_time(t):
    if   t >= 10.0: return 8
    elif t >=  5.0: return 7
    elif t >=  2.0: return 6
    elif t >=  1.0: return 5
    elif t >=  0.5: return 4
    elif t >=  0.2: return 3
    else:           return 2

# ==============================
# Iterative Deepening
# ==============================
def best_move(board, max_depth=5, time_limit=3.0):
    move = book_move(board)
    if move:
        print(f"info string Book move: {move.uci()}")
        sys.stdout.flush()
        return move

    best  = list(board.legal_moves)[0]
    start = time.time()

    for depth in range(1, max_depth + 1):
        if time.time() - start >= time_limit * 0.75:
            break

        current_best = None
        alpha        = -float("inf")

        for m in order_moves(board, 0):
            if time.time() - start >= time_limit:
                break
            board.push(m)
            score = -negamax(board, depth - 1, -float("inf"), float("inf"), 1)
            board.pop()
            if score > alpha:
                alpha        = score
                current_best = m

        if current_best:
            best = current_best

        elapsed = int((time.time() - start) * 1000)
        print(f"info depth {depth} score cp {alpha} time {elapsed} pv {best.uci()}")
        sys.stdout.flush()

    return best

# ==============================
# UCI Loop
# ==============================
def uci_loop():
    board      = chess.Board()
    max_depth  = 5
    time_limit = 3.0

    while True:
        line = input().strip()

        if line == "uci":
            print("id name FENRIX")
            print("id author Lecheheb Djaafar")
            print("option name Depth type spin default 5 min 1 max 10")
            print("option name MoveTime type spin default 3000 min 100 max 15000")
            print("uciok")
            sys.stdout.flush()

        elif line == "isready":
            print("readyok")
            sys.stdout.flush()

        elif line == "ucinewgame":
            board = chess.Board()
            TT.clear()
            HISTORY.clear()
            for i in range(64): KILLER_MOVES[i] = [None, None]

        elif line.startswith("setoption name Depth value"):
            try: max_depth = int(line.split()[-1])
            except: pass

        elif line.startswith("setoption name MoveTime value"):
            try: time_limit = int(line.split()[-1]) / 1000.0
            except: pass

        elif line.startswith("position"):
            parts = line.split()
            if "startpos" in parts:
                board = chess.Board()
                if "moves" in parts:
                    for m in parts[parts.index("moves") + 1:]:
                        board.push_uci(m)
            elif "fen" in parts:
                idx = parts.index("fen") + 1
                if "moves" in parts:
                    end   = parts.index("moves")
                    board = chess.Board(" ".join(parts[idx:end]))
                    for m in parts[end + 1:]: board.push_uci(m)
                else:
                    board = chess.Board(" ".join(parts[idx:]))

        elif line.startswith("go"):
            if "infinite" in line:
                move = best_move(board, max_depth=10, time_limit=9999.0)
            else:
                tl, ad = parse_time(line, board)
                move   = best_move(board, min(max_depth, ad), tl)
            print(f"bestmove {move.uci() if move else '0000'}")
            sys.stdout.flush()

        elif line == "quit":
            break

if __name__ == "__main__":
    uci_loop()

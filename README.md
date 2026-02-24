<p align="center">
  <img src="https://raw.githubusercontent.com/official-fenrix/.github/main/logo.png" width="160">
</p>

# FENRIX

**A modern high-performance UCI chess engine**

🇩🇿 Proudly built in Algeria

---

![Language](https://img.shields.io/badge/Language-Python-blue)
![Protocol](https://img.shields.io/badge/Protocol-UCI-green)
![License](https://img.shields.io/badge/License-GPLv3-red)
![Status](https://img.shields.io/badge/Status-Active-orange)

---

## 🚀 Overview

FENRIX is a modern open-source UCI chess engine written in Python and built from scratch.

It combines:

- Bitboard-based board representation
- Advanced Alpha-Beta search
- Move ordering heuristics
- Transposition tables (Zobrist hashing)
- NNUE neural network evaluation
- Self-play training pipeline
- Full UCI protocol support

---

## ♟ Engine Strength

| Stage | Elo |
|-------|------|
| Classical evaluation | ~1050 |
| + NNUE integration | ~1300 |
| + Search improvements | ~1407 |
| + Opening Book | **~1447** |

Estimated rating: ~1447 Elo  
Win rate vs Stockfish Level 5: ~70%

---

## 🧠 Architecture

### Search
- Alpha-Beta pruning
- Iterative Deepening
- Quiescence Search
- Killer Moves
- History Heuristic
- Mate Distance Pruning

### Evaluation
- Material balance
- Piece-Square Tables
- NNUE (768x256x1 architecture)

### Transposition Table
- 64-bit Zobrist hashing
- 64MB hash size

---

## 🔌 UCI Support

Supported commands:

```
uci
isready
ucinewgame
position startpos
position fen <FEN>
go depth <n>
go movetime <ms>
stop
quit
```

Compatible with:
- Arena
- CuteChess

---

## 🛠 Running

```bash
python uci.py
```

---

## 📜 License

FENRIX is released under GNU GPL v3.

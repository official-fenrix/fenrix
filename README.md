<div align="center">

<br/>

<img src="assets/logo.png" width="100" alt="FENRIX"/>

<br/>

# FENRIX

**Open-source UCI chess engine — crafted in Algeria 🇩🇿**

<br/>

[![License](https://img.shields.io/github/license/official-fenrix/fenrix?style=flat-square)](LICENSE)
[![Release](https://img.shields.io/github/v/release/official-fenrix/fenrix?include_prereleases&label=release&style=flat-square)](https://github.com/official-fenrix/fenrix/releases/latest)
[![Language](https://img.shields.io/badge/language-Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Protocol](https://img.shields.io/badge/protocol-UCI-orange?style=flat-square)](https://www.chessprogramming.org/UCI)
[![ELO](https://img.shields.io/badge/ELO-~1800-critical?style=flat-square)](https://github.com/official-fenrix/fenrix/releases/latest)

<br/>

[**Download**](https://github.com/official-fenrix/fenrix/releases/latest) · [**Report Bug**](https://github.com/official-fenrix/fenrix/issues) · [**Discussions**](https://github.com/official-fenrix/fenrix/discussions)

<br/>

</div>

---

## Overview

FENRIX is a free, open-source **UCI chess engine** written in Python and built from scratch. It features a neural network evaluation (NNUE), advanced search techniques, and full compatibility with major chess GUIs.

---

## Strength

| Milestone | Estimated ELO |
|:---|---:|
| Classical evaluation | ~1050 |
| + NNUE integration | ~1550 |
| + Search improvements | ~1700 |
| + Opening book | **~1800** |

**Performance results (indicative):**

| Opponent | Score |
|:---|---:|
| Stockfish Level 1 (~1350 ELO) | 85% |
| Stockfish Level 2 (~1500 ELO) | 72.5% |
| Stockfish Level 3 (~1650 ELO) | >80% |

> Results vary by hardware, time control, and test conditions.

---

## Architecture

### Search
- Negamax with Alpha–Beta pruning
- Iterative Deepening
- Null Move Pruning (R=3)
- Late Move Reduction (LMR)
- Killer Move Heuristic
- History Heuristic
- Mate Distance Pruning

### Evaluation
- NNUE neural network evaluation
- Positional understanding
- Efficient incremental board representation

### Transposition Table
- 64-bit Zobrist hashing
- Exact / Lower / Upper bound entries
- Up to ~500,000 entries (configurable)

### Opening Book
- Polyglot `.bin` format
- Weighted move selection

---

## UCI Protocol

FENRIX supports the full standard UCI command set:

```
uci
isready
ucinewgame
position startpos [moves ...]
position fen <FEN> [moves ...]
go depth <n>
go movetime <ms>
go wtime <ms> btime <ms> [winc <ms>] [binc <ms>]
go infinite
stop
quit
```

Compatible with **Arena**, **CuteChess**, **Banksia**, and any UCI-compliant GUI.

---

## Time Management

FENRIX uses adaptive time management, scaling search depth to available clock time:

| Time Available | Typical Depth |
|:---|:---:|
| > 10s | 8 |
| 5–10s | 7 |
| 2–5s | 6 |
| 1–2s | 5 |
| 0.5–1s | 4 |
| < 0.5s | 2–3 |

---

## Installation

### Option 1 — Windows Executable (Recommended)

Download `fenrix.exe` from the [latest release](https://github.com/official-fenrix/fenrix/releases/latest) and add it to your GUI.

### Option 2 — Run from Source

```bash
git clone https://github.com/official-fenrix/fenrix.git
cd fenrix
pip install -r requirements.txt
python uci_engine.py
```

---

## GUI Setup (Arena)

1. Open **Arena**
2. Navigate to **Engines → Install New Engine**
3. Select `fenrix.exe`
4. Set protocol to **UCI**
5. Click **OK** — you're ready to play

---

## License

FENRIX is released under the **GNU GPL v3** license. See [`LICENSE`](LICENSE) for full terms.

---

## Author

**Lecheheb Djaafar** — Algeria 🇩🇿  
[github.com/LechehebDjaafar](https://github.com/LechehebDjaafar)

---

<div align="center">

Built with ♟️ and passion in Algeria 🇩🇿

</div>

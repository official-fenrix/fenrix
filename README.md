<p align="center">
  <img src="assets/logo.png" width="140">
</p>

<h1 align="center">FENRIX</h1>

<p align="center">
  A free and strong UCI chess engine.<br>
  Built for strength, scalability, and intelligent evaluation.
</p>

<p align="center">
  <a href="https://github.com/official-fenrix/fenrix/issues">Report a bug</a>
  ·
  <a href="https://github.com/official-fenrix/fenrix/discussions">Open a discussion</a>
  ·
  <a href="https://github.com/official-fenrix/fenrix/releases">Releases</a>
</p>


<p align="center">
  <img alt="License" src="https://img.shields.io/github/license/official-fenrix/fenrix">
  <img alt="Stars" src="https://img.shields.io/github/stars/official-fenrix/fenrix?style=flat">
  <img alt="Issues" src="https://img.shields.io/github/issues/official-fenrix/fenrix">
  <img alt="Last commit" src="https://img.shields.io/github/last-commit/official-fenrix/fenrix">
</p>

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
---

## 👥 Development Team

FENRIX is developed and maintained by:

### 🧠 Lead Developer
- **Djaafar Lecheheb** — Founder & Engine Architect  
  [GitHub Profile](https://github.com/LechehebDjaafar)

---

### 🤝 Contributors

Contributions are welcome.

If you would like to contribute to FENRIX:

- Improve search performance
- Enhance NNUE training
- Optimize evaluation
- Improve testing infrastructure

Please open a Pull Request or start a Discussion.

---

<p align="center">
  Built with ambition. Engineered with precision. ♟️
</p>

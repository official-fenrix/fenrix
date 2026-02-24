```{=html}
<p align="center">
```
`<img src="https://raw.githubusercontent.com/official-fenrix/.github/main/logo.png" width="180"/>`{=html}
```{=html}
</p>
```
```{=html}
<h1 align="center">
```
FENRIX
```{=html}
</h1>
```
```{=html}
<p align="center">
```
`<strong>`{=html}A modern high-performance UCI chess
engine`</strong>`{=html}`<br>`{=html} Engineered for strength,
scalability, and intelligent evaluation.`<br>`{=html} 🇩🇿 Proudly built
in Algeria
```{=html}
</p>
```
```{=html}
<p align="center">
```
`<img src="https://img.shields.io/badge/Language-Python-blue.svg"/>`{=html}
`<img src="https://img.shields.io/badge/Protocol-UCI-green.svg"/>`{=html}
`<img src="https://img.shields.io/badge/License-GPLv3-red.svg"/>`{=html}
`<img src="https://img.shields.io/badge/Status-Active%20Development-orange.svg"/>`{=html}
```{=html}
</p>
```

------------------------------------------------------------------------

## 🚀 Overview

FENRIX is a modern open-source UCI chess engine written in Python and
built from scratch.

It combines:

-   Bitboard-based board representation\
-   Advanced Alpha-Beta search\
-   Move ordering heuristics\
-   Transposition tables (Zobrist hashing)\
-   NNUE neural network evaluation\
-   Self-play training pipeline\
-   Full UCI protocol support

FENRIX is designed to be:

-   Cleanly engineered\
-   Experiment-friendly\
-   Performance-oriented\
-   Educational yet competitive

------------------------------------------------------------------------

## ♟ Engine Strength

  Stage                    Elo
  ------------------------ ------------
  Classical evaluation     \~1050
  \+ NNUE integration      \~1300
  \+ Search improvements   \~1407
  \+ Opening Book          **\~1447**

Estimated rating: \~1447 Elo\
Win rate vs Stockfish Level 5: \~70%

------------------------------------------------------------------------

## 🧠 Architecture

### Board Representation

-   64-bit Bitboards
-   Efficient bitwise move generation

### Search Engine

-   Alpha-Beta pruning
-   Iterative Deepening
-   Quiescence Search
-   Check Extensions
-   Mate Distance Pruning
-   MVV-LVA
-   Killer Moves
-   History Heuristic

### Transposition Table

-   64-bit Zobrist hashing
-   64MB hash table
-   Exact / Lowerbound / Upperbound storage

### Evaluation

**Classical Evaluation** - Material balance - Piece-Square Tables -
Tempo bonus

**NNUE (Efficiently Updatable Neural Network)** - 768 input neurons -
256 hidden neurons - ReLU activation - 1 output node - \~9MB network
file

------------------------------------------------------------------------

## 🔌 UCI Support

Supported commands:

    uci
    isready
    ucinewgame
    position startpos
    position fen <FEN>
    go depth <n>
    go movetime <ms>
    stop
    quit

Tested with Arena and CuteChess.

------------------------------------------------------------------------

## 🛠 Running

``` bash
python uci.py
```

To use with a GUI:

-   Command: python
-   Parameters: path/to/uci.py
-   Protocol: UCI

------------------------------------------------------------------------

## 📊 Performance

  Metric                Value
  --------------------- -------------
  NPS                   \~400--2000
  Transposition Table   64 MB
  NNUE Size             9 MB
  Self-play Games       1000+

------------------------------------------------------------------------

## 🤝 Contributing

Contributions are welcome!

If you'd like to contribute:

1.  Fork the repository\
2.  Create a feature branch\
3.  Commit your changes\
4.  Open a Pull Request

Please ensure:

-   Clean and readable code
-   Proper documentation
-   Performance impact consideration

------------------------------------------------------------------------

## 📦 Releases

Official releases will include:

-   Pre-trained NNUE network
-   Stable engine version
-   Performance benchmarks
-   Changelog

Releases will be published in the GitHub Releases section.

------------------------------------------------------------------------

## 📜 License

FENRIX is released under the GNU General Public License v3.0.

------------------------------------------------------------------------

## 🇩🇿 About

FENRIX is an independent Algerian chess engine project.

Built from zero, engineered step by step, and continuously evolving
toward competitive strength.

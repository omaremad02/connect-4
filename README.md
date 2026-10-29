# Connect 4 vs. AI

A playable **Connect 4** game built with **Pygame**, where you play against a computer opponent that picks its moves using a heuristic board evaluation.

Built for the *Artificial Intelligence* course.

## Features
- 6×7 board with a graphical interface: hover over a column and click to drop your piece
- A computer opponent with a heuristic evaluation function
- A random player goes first
- Win detection in all four directions: horizontal, vertical and both diagonals

## How the AI works
For every valid column the AI simulates dropping its piece, then scores the resulting board using the `score_position` function. The function scans every 4-cell window (horizontal, vertical and diagonal):
- 4 of its own pieces in a window: **+100** (a win)
- 3 of its own pieces plus one empty cell: **+10** (a threat)

The AI then plays the column with the highest score, and picks a random column if every move scores the same. This is a one-move-ahead greedy search.

**Possible next step:** replace the greedy search with **Minimax + alpha-beta pruning**, and add a penalty for the opponent's open threats so the AI also blocks.

## Run it
```bash
pip install pygame numpy
python connect-4.py
```

## Tech
Python · Pygame · NumPy · game AI · heuristic evaluation

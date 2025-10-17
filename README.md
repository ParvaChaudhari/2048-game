## Deployed Application

- **Desktop**: Download the standalone executable from [main.exe](https://github.com/ParvaChaudhari/2048-game/raw/main/dist/main.exe) and run it.

## Source Code

1. Ensure Python 3.6+ is installed. Tkinter, the GUI library used, is included with standard Python installations on Windows and macOS.
2. To Clone the repository and start the game:

   ```bash
   git clone https://github.com/ParvaChaudhari/2048-game.git
   cd 2048-game
   python main.py
   ```

# Implementation Details

## Overview

This project is a complete implementation of the 2048 game, built using Python and Tkinter. It’s a fully functional, GUI based version of the classic puzzle game, designed with an emphasis on clarity, modularity, and reusability. The game supports a configurable board size, realtime score updates, and intuitive keyboard controls. It also includes thoughtful interface features such as fullscreen mode, restart and quit buttons, and a clean, user friendly layout for an enjoyable gameplay experience.

## Technical Approach

- Python was chosen for its simplicity and readability, as well as its strong standard library support and cross platform compatibility.

- Tkinter was used to create the graphical interface since it’s built into Python and requires no external dependencies making the project easy to run and review.

## File Structure

game_logic.py – Contains all the core game mechanics, such as board initialization, tile movement, merging logic, and win/loss detection. Functions are designed to be as pure and stateless as possible to follow functional programming principles.

gui.py – Handles the Tkinter based interface, including user input (arrow keys), game board rendering, score display, and the control buttons (Restart & Quit).

main.py – The main entry point of the application, responsible for initializing and running the game.

## Functional Programming

To keep the code clean and maintainable, most functions in game_logic.py are written as pure functions—they don’t modify global state and instead return new data structures. Eg. include move(), add_random_tile(), and is_game_over().
Meanwhile, gui.py manages the game’s stateful aspects, such as visual updates and user interactions, keeping the logic and interface clearly separated.

## GUI Design

- The game launches in fullscreen mode (window.attributes('-fullscreen', True)) for an immersive experience, with the Escape key set to exit fullscreen.

- Instructions are displayed on the left side of the window in a neatly formatted frame with a readable font (Arial, 14) and proper text wrapping.

- The game board is made up of a grid of Label widgets, styled with larger tiles (width=12, height=6) and bold text (Arial, 24) for clarity.

- Restart and Quit buttons are placed in a dedicated frame below the board, styled consistently and spaced evenly for a polished look.

- When a game ends, a messagebox pops up displaying the final score and automatically restarts the game when confirmed, using a game_ended flag to prevent repeated dialogs.

## Features

- 4x4 game board (configurable size via code).
- Move tiles using arrow keys to merge identical numbers.
- Score tracking based on merged tiles.
- New tiles (2 or 4) appear after each valid move.
- Game ends on reaching 2048 (win) or no valid moves (loss).
- Restart button to start a new game.
- Instructions displayed in the GUI on the left side.
- Modular, readable code with functional programming principles.

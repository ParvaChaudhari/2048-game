import tkinter as tk
from tkinter import messagebox
from typing import List, Tuple
from game_logic import initialize_game, move, add_random_tile, is_game_over, has_won


class GameGUI:
    def __init__(self, size: int = 4):
        self.size = size
        self.board, self.score = initialize_game(size)
        self.window = tk.Tk()
        self.window.title("2048 Game by Parva J Chaudhari")
        self.window.attributes("-fullscreen", True)
        self.colors = {
            0: "#cdc1b4",
            2: "#eee4da",
            4: "#ede0c8",
            8: "#f2b179",
            16: "#f59563",
            32: "#f67c5f",
            64: "#f65e3b",
            128: "#edcf72",
            256: "#edcc61",
            512: "#edc850",
            1024: "#edc53f",
            2048: "#edc22e",
        }
        self.game_ended = False  # Flag to prevent multiple messageboxes
        self.setup_gui()

    def setup_gui(self):
        # Main container frame for layout
        self.main_frame = tk.Frame(self.window)
        self.main_frame.pack(pady=10)

        # Instructions frame on the left
        self.instructions_frame = tk.Frame(self.main_frame)
        self.instructions_frame.pack(side="left", padx=10)

        instructions_text = (
            "How to Play 2048:\n"
            "1. Use arrow keys (Up , Down, Left, Right) to slide tiles.\n"
            "2. Tiles with the same number merge into their sum.\n"
            "3. A new tile (2 or 4) appears after each move.\n"
            "4. Win by creating a 2048 tile!\n"
            "5. Game over when no moves are possible.\n\n"
            "Enjoy the game!        - Parva J Chaudhari"
        )
        self.instructions_label = tk.Label(
            self.instructions_frame,
            text=instructions_text,
            font=("Arial", 12),
            justify="left",
            wraplength=400,
        )
        self.instructions_label.pack()

        # Right frame for score, grid, and restart button
        self.right_frame = tk.Frame(self.main_frame)
        self.right_frame.pack(side="left")

        # Score label
        self.score_label = tk.Label(
            self.right_frame, text=f"Score: {self.score}", font=("Arial", 16)
        )
        self.score_label.pack(pady=10)

        # Game grid
        self.grid_frame = tk.Frame(self.right_frame)
        self.grid_frame.pack()
        self.cells = [
            [
                tk.Label(
                    self.grid_frame,
                    text="",
                    width=10,
                    height=5,
                    font=("Arial", 20),
                    bg="#cdc1b4",
                    relief="ridge",
                )
                for _ in range(self.size)
            ]
            for _ in range(self.size)
        ]
        for i in range(self.size):
            for j in range(self.size):
                self.cells[i][j].grid(row=i, column=j)

        self.button_frame = tk.Frame(self.right_frame)
        self.button_frame.pack(pady=20)

        # Restart button
        self.restart_button = tk.Button(
            self.button_frame, text="Restart", command=self.restart, font=("Arial", 14)
        )
        self.restart_button.pack(side="left", padx=10)

        # Quit button
        self.quit_button = tk.Button(
            self.button_frame,
            text="Quit",
            command=self.window.destroy,
            font=("Arial", 14),
        )
        self.quit_button.pack(side="left", padx=10)

        # Bind arrow keys
        self.window.bind("<Down>", lambda event: self.handle_move("up"))
        self.window.bind("<Up>", lambda event: self.handle_move("down"))
        self.window.bind("<Left>", lambda event: self.handle_move("left"))
        self.window.bind("<Right>", lambda event: self.handle_move("right"))

        self.update_gui()

    def update_gui(self):
        for i in range(self.size):
            for j in range(self.size):
                value = self.board[i][j]
                self.cells[i][j].config(
                    text=str(value) if value else "",
                    bg=self.colors.get(value, "#ff0000"),
                    fg="white" if value > 4 else "black",
                )
        self.score_label.config(text=f"Score: {self.score}")
        if not self.game_ended:  # Show messagebox only once
            if has_won(self.board):
                self.game_ended = True
                messagebox.showinfo(
                    "Congratulations!",
                    f"You reached 2048!",
                )
                self.restart()
            elif is_game_over(self.board):
                self.game_ended = True
                messagebox.showinfo(
                    "Game Over!",
                    f"No more moves possible. Your final score: {self.score}",
                )
                self.restart()

    def handle_move(self, direction: str):
        if not self.game_ended:  # Allow moves only if game hasn't ended
            new_board, score = move(self.board, direction)
            if new_board != self.board:  # Move made
                self.board = add_random_tile(new_board)
                self.score += score
                self.update_gui()

    def restart(self):
        self.board, self.score = initialize_game(self.size)
        self.game_ended = False  # Reset flag for new game
        self.update_gui()

    def run(self):
        self.window.mainloop()

import random
import tkinter as tk
from tkinter import messagebox

# Game Constants
WINNING_POSITION = 36  # The number of steps required to win
GRID_SIZE = 6  # 6x6 Ludo Board
CELL_SIZE = 50  # Size of each cell

class LudoGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Ludo Game 🎲")
        self.root.geometry("400x450")

        self.players = ["Player 1", "Player 2"]
        self.colors = ["red", "blue"]  # Player 1 is red, Player 2 is blue
        self.positions = {player: 0 for player in self.players}  # Track player positions
        self.current_player = 0  # Index of the current player

        # Create UI
        self.label = tk.Label(root, text="🎲 Ludo Game - Player 1's Turn 🎲", font=("Arial", 14))
        self.label.pack(pady=5)

        self.dice_label = tk.Label(root, text="🎲", font=("Arial", 24))
        self.dice_label.pack(pady=5)

        self.roll_button = tk.Button(root, text="Roll Dice 🎲", font=("Arial", 14), command=self.roll_dice)
        self.roll_button.pack(pady=5)

        self.canvas = tk.Canvas(root, width=GRID_SIZE * CELL_SIZE, height=GRID_SIZE * CELL_SIZE, bg="white")
        self.canvas.pack(pady=5)

        self.score_label = tk.Label(root, text=self.get_score_text(), font=("Arial", 12))
        self.score_label.pack(pady=5)

        self.draw_board()
        self.pawn_objects = self.create_pawns()

    def get_score_text(self):
        return f"Positions:\nPlayer 1: {self.positions['Player 1']}\nPlayer 2: {self.positions['Player 2']}"

    def draw_board(self):
        """Draws a simple Ludo board grid"""
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                x1, y1 = j * CELL_SIZE, i * CELL_SIZE
                x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black")

    def create_pawns(self):
        """Creates player pawns"""
        pawns = {}
        for i, player in enumerate(self.players):
            x, y = self.get_coordinates(0)  # Start at position 0
            pawns[player] = self.canvas.create_oval(x, y, x + CELL_SIZE, y + CELL_SIZE, fill=self.colors[i])
        return pawns

    def get_coordinates(self, position):
        """Converts a board position to canvas coordinates"""
        row = position // GRID_SIZE
        col = position % GRID_SIZE
        return col * CELL_SIZE + 5, row * CELL_SIZE + 5

    def roll_dice(self):
        """Handles dice roll and player movement"""
        dice_value = random.randint(1, 6)
        self.dice_label.config(text=f"🎲 {dice_value}")

        player = self.players[self.current_player]
        new_position = self.positions[player] + dice_value

        if new_position <= WINNING_POSITION:
            self.positions[player] = new_position
            self.move_pawn(player, new_position)

            if new_position == WINNING_POSITION:
                messagebox.showinfo("Game Over", f"🏆 {player} wins! 🏆")
                self.root.quit()

        self.score_label.config(text=self.get_score_text())
        self.current_player = (self.current_player + 1) % 2  # Switch turns
        self.label.config(text=f"🎲 {self.players[self.current_player]}'s Turn 🎲")

    def move_pawn(self, player, position):
        """Moves the pawn to the new position"""
        x, y = self.get_coordinates(position)
        self.canvas.coords(self.pawn_objects[player], x, y, x + CELL_SIZE, y + CELL_SIZE)

if __name__ == "__main__":
    root = tk.Tk()
    game = LudoGame(root)
    root.mainloop()

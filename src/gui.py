import tkinter as tk
from game import Game

class ChessGUI:
    def __init__(self):
        self.game = Game()
        self.selected_piece = None
        self.root = tk.Tk()
        self.root.title("AI Chess")
        self.root.geometry("800x800")
        self.canvas = tk.Canvas(self.root, width=800, height=800)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_click)
        self.draw_board()
        self.draw_pieces()
    
    def draw_board(self):
        tile_size = 100
        for row in range(8):
            for col in range(8):
                color = "white" if (row + col) % 2 == 0 else "gray"
                x1 = col * tile_size
                y1 = row * tile_size
                x2 = x1 + tile_size
                y2 = y1 + tile_size
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)

    def draw_pieces(self):
        self.canvas.delete("piece")
        tile_size = 100
        for row in range(8):
            for col in range(8):
                piece = self.game.board[row][col]
                if piece:
                    x = col * tile_size + tile_size // 2
                    y = row * tile_size + tile_size // 2
                    self.canvas.create_text(
                        x, y, text=piece, font=("Arial", 36), tags="piece"
                    )

    def on_click(self, event):
        tile_size = 100
        col = event.x // tile_size
        row = event.y // tile_size
        if self.selected_piece:
            self.game.move_piece(self.selected_piece, (row, col))
            self.selected_piece = None
            self.draw_pieces()
        else:
            piece = self.game.board[row][col]
            if piece:
                self.selected_piece = (row, col)

    def run(self):
        self.root.mainloop()
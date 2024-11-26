import tkinter as tk

class ChessGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("AI Chess")
        self.root.geometry("800x800")
        self.canvas = tk.Canvas(self.root, width=800, height=800)
        self.canvas.pack()
        self.draw_board()
    
    def draw_board(self):
        title_size = 100
        for row in range(8):
            for col in range(8):
                color = "white" if (row + col) % 2 == 0 else "black"
                x1 = col * title_size
                y1 = row * title_size
                x2 = x1 + title_size
                y2 = y1 + title_size
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    def run(self):
        self.root.mainloop()

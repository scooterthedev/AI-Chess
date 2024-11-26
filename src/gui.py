import tkinter as tk

class ChessGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("AI Chess")
        self.root.geometry("800x800")

    def run(self):
        self.root.mainloop()

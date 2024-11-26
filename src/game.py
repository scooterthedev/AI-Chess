class Game:
    def __init__(self):
        self.board = self.initialize_board()

    def initialize_board(self):
        board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP"] * 8,
            [""] * 8,
            [""] * 8,
            [""] * 8,
            [""] * 8,
            ["wP"] * 8,
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ]
        return board
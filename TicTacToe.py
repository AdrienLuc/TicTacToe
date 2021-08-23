
class Position:
    def __init__(self, row, col):
        self.row = row
        self.col = col



class TicTacToe:
    def __init__(self):
        self.current_player=1
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
        
    def record_move (self, pos):
        # 1: changer le board
        self.board[pos.row][pos.col] = self.current_player

        # 2: passer au player suivant
        if self.current_player==2:
            self.current_player=1
        else:
            self.current_player=2


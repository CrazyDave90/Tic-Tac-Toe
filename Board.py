
class Board:
    
    def __init__(self):
        self.gameOver = False
        self.winner = "Nobody"
        self.moves = 0
        self.board = [  [" ", " ", " ",], 
                        [" ", " ", " ",],
                        [" ", " ", " " ]  ]

    def checkGameOver(self):
        if self.moves < 5: # Nobody can win until they place > 3 pieces
            return
        for x in range(0,3): # Checking for a winner
            if self.board[x][0] == self.board[x][1] == self.board[x][2]: # Row
                self.gameOver = True
                self.winner = self.board[x][0]
                return
            if self.board[0][x] == self.board[1][x] == self.board[2][x]: # Column
                self.gameOver = True
                self.winner = self.board[0][x]
                return
        if self.moves == 9: # Game is over, no winners found
            self.gameOver = True
            return

    

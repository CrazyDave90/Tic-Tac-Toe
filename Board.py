class Board:

    
    def __init__(self):
        self.gameOver = False
        self.winner = None
        self.numMoves = 0
        self.player = 'X'
        self.move = ""
        self.board = [
            [" ", " ", " ",], 
            [" ", " ", " ",],
            [" ", " ", " " ]
        ]


    def checkGameOver(self):
        for x in range(0,3):
            if  (self.board[x][0] == self.board[x][1] == self.board[x][2])
            and (self.board[x][0] != " "):
                self.gameOver = True
                self.winner = self.board[x][0]
                return
            if  (self.board[0][x] == self.board[1][x] == self.board[2][x])
            and (self.board[0][x] != " "):
                self.gameOver = True
                self.winner = self.board[0][x]
                return
            if  (self.board[0][0] == self.board[1][1] == self.board[2][2] or
                 self.board[2][0] == self.board[1][1] == self.board[0][2])
            and (self.board[1][1] != " "):
                self.gameOver = True
                self.winner = self.player
                return
        if (self.moves == 9):
            self.gameOver = True
        return


    def checkValidMove(self, move):
        if (not isinstance(move, str)):
            return False
        elif (len(move) != 2):
            return False
        elif (move[0] not in "ABC"):
            return False
        elif (move[1] not in "123"):
            return False
        return True

       
    def switchPlayer(self):
        if (self.player == 'X'):
            self.player = 'O'
            return
        self.player = 'X'
        return

class Board:

    
    def __init__(self):
        self.gameOver = False
        self.winner = None
        self.numMoves = 0
        self.currentPlayer = 'X'
        self.board = [
            [" ", " ", " ",], 
            [" ", " ", " ",],
            [" ", " ", " " ]
        ]
        self.winCombos = (
            # Horizontal
            ((0,0), (0,1), (0,2)),
            ((1,0), (1,1), (1,2)),
            ((2,0), (2,1), (2,2)),
            # Vertical
            ((0,0), (1,0), (2,0)),
            ((0,1), (1,1), (2,1)),
            ((0,2), (1,2), (2,2)),
            #Diagonal
            ((0,0), (1,1), (2,2)),
            ((0,2), (1,1), (2,0))
        )


    def checkGameOver(self):
        for combo in self.winCombos:
            space1 = self.board[combo[0][0]][combo[0][1]]
            space2 = self.board[combo[1][0]][combo[1][1]]
            space3 = self.board[combo[2][0]][combo[2][1]]
            if space1 == space2 == space3 == self.currentPlayer: # Avoid GameOver with 3 blank spaces
                self.winner = self.currentPlayer
                self.gameOver = True
                return
        if (self.numMoves == 9): # All spaces filled
            self.gameOver = True
        return


    def checkValidMove(self, move): # E.g. 1A, 3B, 2C
        if ((not isinstance(move, str))
        or (len(move) != 2)
        or (move[0] not in "123")
        or (move[1] not in "ABC")):
            return False
        return True

       
    def switchPlayer(self):
        if (self.currentPlayer == 'X'):
            self.currentPlayer = 'O'
            return
        self.currentPlayer = 'X'
        return


    def drawBoard(self):
        switch = 1
        print ("  A B C ")
        for row in range(0,5):
            if (switch == 1):
                boardRow = int(row/2)
                print (str(boardRow + 1) + " " +
                      self.board[boardRow][0] + "|" +
                      self.board[boardRow][1] + "|" +
                      self.board[boardRow][2]
                )
            else:
                print ("  -----")
            switch *= -1
        return


 
game = Board()
game.numMoves = 9
game.checkGameOver()
print (game.gameOver)
print ("expected: True")
print (game.winner)
print ("expected: None")
game.numMoves = 5
print (game.checkValidMove("3B"))
print ("expected: True")
game.board = [
        ["X", "X", "X",], 
        ["X", " ", " ",],
        ["X", " ", " " ]
]
print ()
game.drawBoard()
print ()
game.checkGameOver()
print (game.gameOver)
print ("expected: True")
print (game.winner)
print ("expected: X")
game.board = [
        ["O", " ", " ",], 
        ["O", " ", " ",],
        ["O", " ", " " ]
]
print ()
game.drawBoard()
print ()
game.switchPlayer()
game.checkGameOver()
print (game.gameOver)
print ("expected: True")
print (game.winner)
print ("expected: O")


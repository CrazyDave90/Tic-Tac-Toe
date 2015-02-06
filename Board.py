class Board:

    
    def __init__(self):
        self.gameOver = False
        self.winner = None
        self.numMoves = 0
        self.currentPlayer = 'X'
        self.currentMove = ""
        self.coordinate1 = ""
        self.coordinate2 = ""
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

    
    def setCoordinates(self): # coordinates for self.Board
        self.currentMove.upper()
        self.coordinate1 = ord(self.currentMove[0])-1
        self.coordinate2 = ord(self.currentMove[1])-17
        if (self.coordinate1 < 0 or self.coordinate2 < 0):
            self.coordinate1 = "INVALID"
            self.coordinate2 = "INVALID"
        else:
            self.coordinate1 = int(chr(self.coordinate1))
            self.coordinate2 = int(chr(self.coordinate2))
        return


    def isValidMove(self): # checks valid coordinates
        if ((len(self.currentMove) != 2)
        or (str(self.coordinate1) not in "012")
        or (str(self.coordinate2) not in "012")
        or (self.board[self.coordinate1][self.coordinate2] != " ")):
            return False
        return True

       
    def switchPlayer(self):
        if (self.currentPlayer == 'X'):
            self.currentPlayer = 'O'
            return
        self.currentPlayer = 'X'
        return


    def placeMove(self):
        self.board[self.coordinate1][self.coordinate2] = self.currentPlayer
        self.numMoves += 1
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


    def startGame(self):
        self.drawBoard()
        print ("\n To play, enter the row followed by the column of any empty space.")
        while (not self.gameOver):
            print (" Current Player: " + self.currentPlayer)
            self.currentMove = input(" Enter your move: ")
            self.setCoordinates()
            if (self.isValidMove()):
                self.placeMove()
                self.drawBoard()
                self.checkGameOver()
                self.switchPlayer()
            else:
                print (" Invalid Move! Try again.")
        print (" " + self.winner + " wins!")
        return

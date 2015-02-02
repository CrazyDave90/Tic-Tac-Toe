class Board:
    
    def __init__(self):
        self.gameOver = False;
        self.winner = "Nobody";
        self.moves = 0;
        self.player = 'X';
        self.board = [[" ", " ", " ",], 
                      [" ", " ", " ",],
                      [" ", " ", " " ]];

    def checkGameOver(self):
        if (self.moves < 5): # Impossible to win under 5 moves
            return;
        for x in range(0,3): # Check for winner
            if (self.board[x][0] == self.board[x][1] == self.board[x][2]): # Row
                self.gameOver = True;
                self.winner = self.board[x][0];
                return;
            if (self.board[0][x] == self.board[1][x] == self.board[2][x]): # Column
                self.gameOver = True;
                self.winner = self.board[0][x];
                return;
        if (self.moves == 9): # Maximum moves
            self.gameOver = True;
            return;

    def checkMove(self, move): # Checks for correct move E.g. A2, c1, B3, etc.
        if (not isinstance(move, str)):
            return False;
        elif (len(move) != 2):
            return False;
        elif (move[0] not in ["a", "A", "b", "B", "c", "C"]):
            return False;
        elif (move[1] not in ["1", "2", "3"]):
            return False;
        else:
            return True;
       
    def switchPlayer(self):
        if (self.player == 'X'):
            self.player = 'O';
            return;
        else:
            self.player = 'X';
            return;

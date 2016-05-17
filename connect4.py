# connect4.py Hello
# Main class for Connect 4 interface

class connect4(object):
    rows = 6
    cols = 7

    def __init__(self):
        # Board: a list of columns holding 1s or 2s
        self.board = [[] for i in range(self.cols)]

    def canPlayCol(self, col):
        # Check if we can play in column <col> (0-indexed)
        # Returns true if this is a legal move
        return len(self.board[col]) < self.rows

    def move(self, player, col):
        # If possible, get player <player> to move in column <col>
        # Returns true if the move was successful
        if self.canPlayCol(col):
            self.board[col].append(player)
            return True
        return False

    def checkWin(self):
        # Check for wins all over the board
        for x in range(self.cols):
            for y in range(self.rows):
                checkWin = self.checkWinPosition(x, y)
                if checkWin != 0:
                    return checkWin

        return 0

    def checkWinPosition(self, x, y):
        # Check if there's a winner with a bottom-left-most piece 
        # at position (x, y)
        winner = self.pieceAt(x, y)

        # Can't win here if nobody's played it
        if winner == 0:
            return 0
        
        # Check for a win upwards
        if self.pieceAt(x, y+1) == winner and \
            self.pieceAt(x, y+2) == winner and \
            self.pieceAt(x, y+3) == winner:
            return winner

        # Check for a win rightwards
        if self.pieceAt(x+1, y) == winner and \
            self.pieceAt(x+2, y) == winner and \
            self.pieceAt(x+3, y) == winner:
            return winner

        # Check for a win up-right
        if self.pieceAt(x+1, y+1) == winner and \
            self.pieceAt(x+2, y+2) == winner and \
            self.pieceAt(x+3, y+3) == winner:
            return winner

        # Check for a win down-right
        if self.pieceAt(x+1, y-1) == winner and \
            self.pieceAt(x+2, y-2) == winner and \
            self.pieceAt(x+3, y-3) == winner:
            return winner

        # Nobody won!
        return 0

    def pieceAt(self, x, y):
        # Helper function for win-checking
        if x < 0 or x >= self.cols:
            return 0
        if y < 0 or y >= len(self.board[x]):
            return 0
        return self.board[x][y]

    def printBoard(self):
        # Print the board to the screen
        for y in range(self.rows)[::-1]:
            s = ""
            for x in range(self.cols):
                if(len(self.board[x]) > y):
                    s += str(self.board[x][y])
                else:
                    s += "."
            print s


def main():
    c4 = connect4()
    player = 1

    while not c4.checkWin():
        print ""
        c4.printBoard()
        print ""
        try:
            col = int(raw_input("Player {}: ".format(player)))
            if col < 1 or \
                col > c4.cols or \
                not c4.canPlayCol(col-1):
                raise ValueError()
            c4.move(player, col-1)
            player = 3-player
        except:
            print "Invalid move -- try again."


    # Game over
    c4.printBoard()
    print "Winner: Player {}!".format(3-player)

if __name__ == "__main__":
    main()

grid = ["blank", "blank", "blank", "blank", "blank", "blank", "blank", "blank", "blank"]


def makeMark(symbol,gridNum):
    grid[gridNum]= symbol
    
def resetGrid():
    global grid
    grid = ["blank", "blank", "blank", "blank", "blank", "blank", "blank", "blank", "blank"]

def isWinner(board, letter):
    print(board)
    if (board[6] == letter and board[7] == letter and board[8] == letter):
        return letter + " wins!"

    if (board[3] == letter and board[4] == letter and board[5] == letter):
        return letter + " wins!"
    
    if (board[0] == letter and board[1] == letter and board[2] == letter):
        return letter + " wins!"

    if (board[6] == letter and board[3] == letter and board[0] == letter):
        return letter + " wins!"

    if (board[7] == letter and board[4] == letter and board[1] == letter):
        return letter + " wins!"

    if (board[8] == letter and board[5] == letter and board[2] == letter):
        return letter + " wins!"
        
    if(board[6] == letter and board[4] == letter and board[2] == letter):
        return letter + " wins!"
        
    if (board[8] == letter and board[4] == letter and board[0] == letter):
        return letter + " wins!"

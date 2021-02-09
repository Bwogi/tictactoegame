# board
# display board
# play game
# check win
    # check rows
    # check columns
    # check diagonals
# check tie
# flip player

#---

# Global Variables

# Game Board
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

# if game still going
game_still_going = True

# who won or tie
winner = None

# Who's turn is it?
currentPlayer = "X"

# ---

def displayBoard():
    print(" ")
    print(" -------------  ")
    print(" | " + board[0] + " | " + board[1] + " | " + board[2] +  " | ")
    print(" | " + board[3] + " | " + board[4] + " | " + board[5] +  " | ")
    print(" | " + board[6] + " | " + board[7] + " | " + board[8] +  " | ")
    print(" -------------  ")
    print(" ")

def handleTurn(player):
    position = input("Choose a position from 1 - 9 : ")
    position = int(position) - 1
    board[position] = "X"
    displayBoard()

def checkForWinner():
    global winner #setup global variable
    # checkRows()
    # checkColumns()
    # checkDiagonals()
    rowWinner = checkRows()
    columnWinner = checkColumns()
    diagonalWinner = checkDiagonals()
    if rowWinner: 
        winner = rowWinner
    elif columnWinner:
        winner = columnWinner
    elif diagonalWinner:
        winner = diagonalWinner
    else:
        winner = None
    return

def CheckIfTie():
    return

def checkIfGameOver():
    checkForWinner()
    CheckIfTie()

def checkRows():
    global game_still_going # insert and manage a global variable
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    if row1 or row2 or row3: # if any row does have a match, game is done
        game_still_going = False

    if row1: # return the winner (X or O)
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return

def checkColumns():
    global game_still_going # insert and manage a global variable
    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"

    if column1 or column2 or column3:# if any column does have a match, game is done
        game_still_going = False

    if column1: # return the winner (X or O)
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]
    return

def checkDiagonals():
    global game_still_going # insert and manage a global variable
    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[6] == board[4] == board[2] != "-"

    if diagonal1 or diagonal2:# if any diagonal does have a match, game is done
        game_still_going = False

    if diagonal1: # return the winner (X or O)
        return board[0]
    elif diagonal2:
        return board[6]
    return

def flipPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    elif currentPlayer == "O":
        currentPlayer = "X"
    return

def playGame():
    displayBoard()
    while game_still_going: # while the game is still going
        handleTurn(currentPlayer) # handle a single turn of an arbitrary player
        checkIfGameOver() # check if the game has ended
        flipPlayer() # flip to the other player
    if winner == "X" or winner == "O": # the game has ended
        print(winner + " won.")
    elif winner == None:
        print("Tie.")
 




playGame() # play a game of tic tac toe
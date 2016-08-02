from random import randint

board = [] # Initialize Board

# Create Board
for x in range(5):
    board.append(["O"] * 5)

# Print Board to Terminal
def print_board(board):
    for row in board:
        print " ".join(row)

# Start Game
print "Let's play Battleship!"
print_board(board)

# Randomize where the battleship is
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

# Call randomize functions
ship_row = random_row(board)
ship_col = random_col(board)

# Limit turns
for turn in range(4):
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    # Direct Hit
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    
    # Misses
    else:
        # Outside of Board
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        # Hit same spot miss
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        # Normal Miss
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        
        # Let user know their turns are up
        if turn == 3:
            print "Game Over"
    # Let user know what turn it is and what they have guessed
    print "Turn", turn + 1
    print_board(board)
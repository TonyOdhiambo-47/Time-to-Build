# Project 2
# January 4th, 2025
# This is meant to be a 2-Player Game of Tic-Tac-Toe, not playing against the computer.

# Creating the board
def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]

# Displaying the board
def print_board(board):
    print("-------------")
    for row in board:
        print("|", " | ".join(row), "|")
    print("-------------")

# Checking for a win
def check_win(board, player):
    # Rows
    for row in board:
        if row.count(player) == 3:
            return True
    # Columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Checking for a draw
def check_draw(board):
    return all(board[row][col] != " " for row in range(3) for col in range(3))

# Get player's move
def get_move(player):
    while True:
        try:
            row = int(input(f"Player {player}, enter the row (1-3): ")) - 1
            col = int(input(f"Player {player}, enter the column (1-3): ")) - 1
            if 0 <= row <= 2 and 0 <= col <= 2:
                return row, col
            else:
                print("Invalid input. Please enter values between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

# Main game
def play_game():
    board = initialize_board()
    current_player = "X"

    while True:
        print_board(board)
        row, col = get_move(current_player)
        
        # Ensure the cell is empty
        if board[row][col] != " ":
            print("Cell already taken. Try again.")
            continue

        # Make the move
        board[row][col] = current_player

        # Check for a win
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check for a draw
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Start the game
play_game()

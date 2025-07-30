
import math

def show_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def get_winner(board):
   
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2] != " ":
            return board[r][0]
        if board[0][r] == board[1][r] == board[2][r] != " ":
            return board[0][r]

   
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def minimax(board, is_ai_turn):
    winner = get_winner(board)
    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif is_full(board):
        return 0

    if is_ai_turn:
        best = -math.inf
        for r in range(3):
            for j in range(3):
                if board[r][j] == " ":
                    board[r][j] = "O"
                    value = minimax(board, False)
                    board[r][j] = " "
                    best = max(best, value)
        return best
    else:
        best = math.inf
        for r in range(3):
            for j in range(3):
                if board[r][j] == " ":
                    board[r][j] = "X"
                    value = minimax(board, True)
                    board[r][j] = " "
                    best = min(best, value)
        return best


def find_best_move(board):
    best_score = -math.inf
    move = (-1, -1)
    for r in range(3):
        for j in range(3):
            if board[r][j] == " ":
                board[r][j] = "O"
                score = minimax(board, False)
                board[r][j] = " "
                if score > best_score:
                    best_score = score
                    move = (r, j)
    return move


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X'. AI is 'O'.")
    show_board(board)

    while True:
        
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if board[row][col] == " ":
                    board[row][col] = "X"
                    break
                else:
                    print("Cell already taken! Try again.")
            except:
                print("Invalid input. Enter numbers between 0 and 2.")

        show_board(board)

        if get_winner(board):
            print("You win!")
            break
        if is_full(board):
            print("It's a draw!")
            break

      
        ai_row, ai_col = find_best_move(board)
        board[ai_row][ai_col] = "O"
        print("AI played:")
        show_board(board)

        if get_winner(board):
            print("AI wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

play_game()
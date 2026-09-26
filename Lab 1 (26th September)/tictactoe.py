HUMAN = 'X'
AI = 'O'
EMPTY = ' '


def check(board):
    # Rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]

    # Columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None


def minimax(board, is_max):
    winner = check(board)

    if winner == AI:
        return 1

    if winner == HUMAN:
        return -1

    # Draw
    if all(cell != EMPTY for row in board for cell in row):
        return 0

    if is_max:
        best = -100

        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI
                    score = minimax(board, False)
                    board[i][j] = EMPTY

                    if score > best:
                        best = score

        return best

    else:
        best = 100

        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = HUMAN
                    score = minimax(board, True)
                    board[i][j] = EMPTY

                    if score < best:
                        best = score

        return best


def main():
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

    print("Tic Tac Toe")
    print("1 2 3")
    print("4 5 6")
    print("7 8 9")

    while True:

        # Print board
        for row in board:
            print(" | ".join(row))
            print("---------")

        # Human move
        move = int(input("Enter position (1-9): "))

        row = (move - 1) // 3
        col = (move - 1) % 3

        if board[row][col] != EMPTY:
            print("Position already taken!")
            continue

        board[row][col] = HUMAN

        # Check human win
        if check(board) == HUMAN:
            print("You Win!")
            break

        # Check draw before AI move
        if all(cell != EMPTY for row in board for cell in row):
            print("Draw!")
            break

        # AI move
        best_score = -100
        best_move = None

        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI
                    score = minimax(board, False)
                    board[i][j] = EMPTY

                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        board[best_move[0]][best_move[1]] = AI

        # Check AI win
        if check(board) == AI:
            print("AI Wins!")
            break


main()
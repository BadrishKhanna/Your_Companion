import random

def game():
    def print_board(board):
        for row in board:
            print(" | ".join(row))
            print("-" * 9)

    def check_winner(board):
        for row in board:
            if row[0] == row[1] == row[2] != " ":
                return row[0]
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] != " ":
                return board[0][col]
        if board[0][0] == board[1][1] == board[2][2] != " ":
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != " ":
            return board[0][2]
        return None

    def check_draw(board):
        return all(cell != " " for row in board for cell in row)

    def get_available_moves(board):
        return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

    def computer_move(board):
        available_moves = get_available_moves(board)
        return random.choice(available_moves) if available_moves else None

    def tic_tac_toe():
        board = [[" " for _ in range(3)] for _ in range(3)]
        player = "X"
        while True:
            print_board(board)
            if player == "X":
                try:
                    row, col = map(int, input("Enter your move (row and column): ").split())
                    if (row, col) not in get_available_moves(board):
                        print("Invalid move! Try again.")
                        continue
                except ValueError:
                    print("Please enter two valid integers for row and column.")
                    continue
            else:
                row, col = computer_move(board)
                print(f"Computer plays: {row} {col}")

            board[row][col] = player

            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"{winner} wins!")
                break

            if check_draw(board):
                print_board(board)
                print("It's a draw!")
                break

            player = "O" if player == "X" else "X"

    tic_tac_toe()

if __name__ == "__main__":
    game()

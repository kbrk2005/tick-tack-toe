from colorama import Fore, Style, init
init(autoreset=True)

def print_board(board):
    print("\n   1   2   3")
    for i in range(3):
        row = ' | '.join(board[i])
        print(f"{i+1}  {row}")
        if i < 2:
            print("  -----------")

def check_winner(board, symbol):
    for i in range(3):
        if all(board[i][j] == symbol for j in range(3)) or \
           all(board[j][i] == symbol for j in range(3)):
            return True
    if all(board[i][i] == symbol for i in range(3)) or \
       all(board[i][2 - i] == symbol for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def get_move(player_name, symbol, board):
    while True:
        try:
            row = int(input(Fore.CYAN + f"{player_name} ({symbol}), enter row (1-3): ")) - 1
            col = int(input(Fore.CYAN + f"{player_name} ({symbol}), enter column (1-3): ")) - 1
            if row not in range(3) or col not in range(3):
                print(Fore.RED + "Row and column must be between 1 and 3.")
                continue
            if board[row][col] != ' ':
                print(Fore.RED + "Cell already taken. Try again.")
                continue
            return row, col
        except ValueError:
            print(Fore.RED + "Invalid input! Enter numbers only.")

def play_game():
    player1 = input("Enter name for Player X: ")
    player2 = input("Enter name for Player O: ")
    scores = {player1: 0, player2: 0}

    while True:
        board = [[' ' for _ in range(3)] for _ in range(3)]
        current_player = player1
        current_symbol = 'X'
        print_board(board)

        while True:
            row, col = get_move(current_player, current_symbol, board)
            board[row][col] = Fore.GREEN + current_symbol + Style.RESET_ALL
            print_board(board)

            if check_winner(board, Fore.GREEN + current_symbol + Style.RESET_ALL):
                print(Fore.YELLOW + f"🎉 {current_player} wins this round!")
                scores[current_player] += 1
                break
            elif is_draw(board):
                print(Fore.BLUE + "It's a draw!")
                break
            current_player, current_symbol = (
                (player2, 'O') if current_player == player1 else (player1, 'X')
            )

        print(Fore.MAGENTA + f"Current Scores: {player1}: {scores[player1]}, {player2}: {scores[player2]}")
        choice = input("Play again? (y = continue, r = reset score, n = quit): ").lower()
        if choice == 'r':
            scores = {player1: 0, player2: 0}
            print(Fore.LIGHTRED_EX + "Scores reset!")
        elif choice != 'y':
            print(Fore.LIGHTGREEN_EX + "Thanks for playing Tic-Tac-Toe!")
            break

# Start the game
play_game()

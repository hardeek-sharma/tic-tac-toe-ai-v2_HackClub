import random

player1 = "X"
player2 = "O"


def new_board():
    board_holder = []
    for i in range(3):
        row_holder = []
        for j in range(3):
            row_holder.append(None)
        board_holder.append(row_holder)
    return board_holder


def render(init_board):
    for i in range(3):
        for j in range(3):
            if init_board[i][j] is None:
                print(f"   ", end="")
            else:
                print(f" {init_board[i][j]} ", end="")
            if j < 2:
                print("|", end="")
        print()
        if i < 2:
            print("---+---+---")


def get_move():
    x_move = None
    y_move = None
    while True:
        try:
            y_move = int(input("What is your y coordinate: "))
        except ValueError:
            print("\033[31m Enter a NUMBER \033[0m")
        else:
            if not 0 <= y_move <= 2:
                print("\033[31m Enter a number between 0-2 \033[0m")
            else:
                break

    while True:
        try:
            x_move = int(input("What is your x coordinate: "))
        except ValueError:
            print("\033[31m Enter a NUMBER \033[0m")
        else:
            if not 0 <= x_move <= 2:
                print("\033[31m Enter a number between 0-2 \033[0m")
            else:
                break

    return y_move, x_move


def make_move(init_board, coordinates, player):
    while True:
        if is_valid_move(init_board, coordinates):
            break
        print("\033[31m That spot is already taken. Choose again \033[0m")
        coordinates = get_move()

    board_holder = []
    for i in range(3):
        row_holder = []
        for j in range(3):
            if (i, j) == coordinates:
                row_holder.append(player)
            else:
                row_holder.append(init_board[i][j])
        board_holder.append(row_holder)
    return board_holder


def is_valid_move(init_board, coordinates):
    y, x = coordinates
    return init_board[y][x] is None


def get_winner(init_board):
    if init_board[0][0] == init_board[0][1] and init_board[0][1] == init_board[0][2]:  # Top Row
        return init_board[0][0]
    elif init_board[1][0] == init_board[1][1] and init_board[1][1] == init_board[1][2]:  # Middle Row
        return init_board[1][0]
    elif init_board[2][0] == init_board[2][1] and init_board[2][1] == init_board[2][2]:  # Bottom Row
        return init_board[2][0]
    elif init_board[0][0] == init_board[1][0] and init_board[1][0] == init_board[2][0]:  # Left Column
        return init_board[0][0]
    elif init_board[0][1] == init_board[1][1] and init_board[1][1] == init_board[2][1]:  # Middle Column
        return init_board[0][1]
    elif init_board[0][2] == init_board[1][2] and init_board[1][2] == init_board[2][2]:  # Right Column
        return init_board[0][2]
    elif init_board[0][0] == init_board[1][1] and init_board[1][1] == init_board[2][2]:  # Negative Diagonal
        return init_board[0][0]
    elif init_board[0][2] == init_board[1][1] and init_board[1][1] == init_board[2][0]:  # Positive Diagonal
        return init_board[0][2]

    return None


def random_ai(init_board, player):
    legal_moves = []
    for i in range(3):
        for j in range(3):
            if init_board[i][j] is None:
                legal_moves.append((i, j))


    return random.choice(legal_moves)


def run_game():
    board = new_board()
    render(board)
    current_player = player1
    turn = 0
    while True:
        if turn == 9:
            print("It's  Draw. No one wins")
            break
        print(f"** {current_player} Turn **")
        # coords = get_move()
        coords = random_ai(board, current_player)
        board = make_move(board, coords, current_player)
        render(board)
        winner = get_winner(board)

        if winner is not None:
            print(f"Player {winner} Won!!!")
            break

        if current_player == player1:
            current_player = player2
        else:
            current_player = player1

        turn += 1


if __name__ == '__main__':
    run_game()

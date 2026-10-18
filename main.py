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

    print()


def get_move():
    x_move = None
    y_move = None
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

board = new_board()
board[0][0] = "x"

move_coords = get_move()

board = make_move(board, move_coords, "x")

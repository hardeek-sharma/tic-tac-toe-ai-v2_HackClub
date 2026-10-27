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


def human_player(init_board, player):
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
        coordinates = human_player(init_board, player)

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
    if init_board[0][0] is not None and init_board[0][0] == init_board[0][1] and init_board[0][1] == init_board[0][
        2]:  # Top Row
        return init_board[0][0]
    elif init_board[1][0] is not None and init_board[1][0] == init_board[1][1] and init_board[1][1] == init_board[1][
        2]:  # Middle Row
        return init_board[1][0]
    elif init_board[2][0] is not None and init_board[2][0] == init_board[2][1] and init_board[2][1] == init_board[2][
        2]:  # Bottom Row
        return init_board[2][0]
    elif init_board[0][0] is not None and init_board[0][0] == init_board[1][0] and init_board[1][0] == init_board[2][
        0]:  # Left Column
        return init_board[0][0]
    elif init_board[0][1] is not None and init_board[0][1] == init_board[1][1] and init_board[1][1] == init_board[2][
        1]:  # Middle Column
        return init_board[0][1]
    elif init_board[0][2] is not None and init_board[0][2] == init_board[1][2] and init_board[1][2] == init_board[2][
        2]:  # Right Column
        return init_board[0][2]
    elif init_board[0][0] is not None and init_board[0][0] == init_board[1][1] and init_board[1][1] == init_board[2][
        2]:  # Negative Diagonal
        return init_board[0][0]
    elif init_board[0][2] is not None and init_board[0][2] == init_board[1][1] and init_board[1][1] == init_board[2][
        0]:  # Positive Diagonal
        return init_board[0][2]

    return None


def find_legal_moves(init_board):
    legal_moves = []
    for i in range(3):
        for j in range(3):
            if init_board[i][j] is None:
                legal_moves.append((i, j))
    return legal_moves


def random_ai(init_board, player):
    legal_moves = find_legal_moves(init_board)
    return random.choice(legal_moves)


def get_player_mode(player):
    print("(1. Human 2. Dumb Bot 3. Smart Bot 4. Genius Bot 5. God Bot)")
    while True:
        try:
            player_mode = int(input(f"What should player '{player}' be: "))
        except ValueError:
            print("\033[31m Enter a NUMBER 1-5 \033[0m")
        else:
            if not 1 <= player_mode <= 5:
                print("\033[31m Enter a number between 1-5 \033[0m")
            else:
                break
    return player_mode


def finds_winning_moves_ai(init_board, player):
    legal_moves = find_legal_moves(init_board)
    for move in legal_moves:
        i, j = move
        init_board[i][j] = player
        if get_winner(init_board) is not None:
            init_board[i][j] = None
            return move
        init_board[i][j] = None
    return random.choice(legal_moves)


def finds_winning_and_losing_moves_ai(init_board, player):
    legal_moves = find_legal_moves(init_board)
    for move in legal_moves:
        i, j = move
        init_board[i][j] = player
        if get_winner(init_board) is not None:
            init_board[i][j] = None
            return move
        init_board[i][j] = None

    player = get_opponent(player)

    for move in legal_moves:
        i, j = move
        init_board[i][j] = player
        if get_winner(init_board) is not None:
            init_board[i][j] = None
            return move
        init_board[i][j] = None

    return random.choice(legal_moves)


def get_opponent(player):
    if player == player1:
        return player2
    if player == player2:
        return player1
    return None


def minimax_score(init_board, player_to_move, player_to_optimize, depth):
    legal_moves = find_legal_moves(init_board)
    winner = get_winner(init_board)
    depth += 1

    if winner is not None:
        if winner == player_to_optimize:
            return 10 - depth
        else:
            return depth - 10
    if not find_legal_moves(init_board):
        return 0

    scores = []
    for move in legal_moves:
        board_holder = make_move(init_board, move, player_to_move)
        opponent = get_opponent(player_to_move)
        score = minimax_score(board_holder, opponent, player_to_optimize, depth)
        scores.append(score)

    if player_to_move == player_to_optimize:
        return max(scores)
    else:
        return min(scores)


cache = {}

def minimax_score_with_cache(init_board, player_to_move, player_to_optimize, depth):
    board_cache_key = str(init_board)

    if board_cache_key not in cache:
        score = minimax_score(init_board, player_to_move, player_to_optimize, depth)

        cache[board_cache_key] = score

    return cache[board_cache_key]

def minimax_ai(init_board, player):
    best_move = None
    best_score = None

    legal_moves = find_legal_moves(init_board)

    for move in legal_moves:
        board_holder = make_move(init_board, move, player)
        opponent = get_opponent(player)
        score = minimax_score_with_cache(board_holder, opponent, player, 0)

        if best_score is None or score > best_score:
            best_move = move
            best_score = score

    return best_move


def run_game():
    board = new_board()
    coords = None

    current_player = player1
    player1_mode = get_player_mode(player1)
    player2_mode = get_player_mode(player2)
    render(board)
    while True:
        if not find_legal_moves(board):
            print("It's Draw. No one wins")
            break
        print(f"** {current_player} Turn **")
        print()
        if current_player == player1:
            if player1_mode == 1:
                coords = human_player(board, current_player)
            elif player1_mode == 2:
                coords = random_ai(board, current_player)
            elif player1_mode == 3:
                coords = finds_winning_moves_ai(board, current_player)
            elif player1_mode == 4:
                coords = finds_winning_and_losing_moves_ai(board, current_player)
            elif player1_mode == 5:
                coords = minimax_ai(board, current_player)
        elif current_player == player2:
            if player2_mode == 1:
                coords = human_player(board, current_player)
            elif player2_mode == 2:
                coords = random_ai(board, current_player)
            elif player2_mode == 3:
                coords = finds_winning_moves_ai(board, current_player)
            elif player2_mode == 4:
                coords = finds_winning_and_losing_moves_ai(board, current_player)
            elif player2_mode == 5:
                coords = minimax_ai(board, current_player)
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


if __name__ == '__main__':
    run_game()
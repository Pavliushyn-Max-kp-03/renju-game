import random

BOARD_SIZE = 19

def create_board():
    return [['.' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def read_board_from_file(filename):
    try:
        with open(filename, "r") as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")
        return None

    if len(lines) != BOARD_SIZE:
        print(f"Неправильна кількість рядків: очікується {BOARD_SIZE}, знайдено {len(lines)}.")
        return None

    board = []
    for idx, line in enumerate(lines):
        parts = line.strip().split()
        if len(parts) != BOARD_SIZE:
            print(f"Рядок {idx + 1} має {len(parts)} елементів, а очікується {BOARD_SIZE}.")
            return None
        try:
            row = [int(x) for x in parts]
        except ValueError:
            print(f"Рядок {idx + 1} містить нечислові значення.")
            return None
        for val in row:
            if val not in (0, 1, 2):
                print(f"Неприпустиме значення {val} в рядку {idx + 1}. Допустимі тільки 0, 1, 2.")
                return None
        board.append(['.' if x == 0 else 'X' if x == 1 else 'O' for x in row])

    return board

def print_board(board):
    print('  ' + ' '.join([chr(ord('A') + i) for i in range(BOARD_SIZE)]))
    for idx, row in enumerate(board):
        print(f"{idx+1:2} {' '.join(row)}")

def is_valid_move(board, x, y):
    return 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE and board[x][y] == '.'

def place_move(board, x, y, player):
    board[x][y] = player

def check_win(board, x, y, player):
    directions = [ (1,0), (0,1), (1,1), (1,-1) ]
    for dx, dy in directions:
        count = 1
        for dir in [1, -1]:
            nx, ny = x, y
            while True:
                nx += dx * dir
                ny += dy * dir
                if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE and board[nx][ny] == player:
                    count += 1
                else:
                    break
        if count >= 5:
            return True
    return False

def parse_input(user_input):
    user_input = user_input.strip().upper()
    if len(user_input) < 2:
        return None
    col = ord(user_input[0]) - ord('A')
    try:
        row = int(user_input[1:]) - 1
    except ValueError:
        return None
    if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
        return row, col
    return None

def main():
    board = read_board_from_file("input.txt")
    if board is None:
        return  # Вихід, якщо помилка в input.txt

    current_player = 'X'
    while True:
        print_board(board)
        move = input(f"Player {current_player}, enter your move (e.g., A1): ")
        parsed = parse_input(move)
        if not parsed:
            print("Invalid input. Try again.")
            continue
        x, y = parsed
        if not is_valid_move(board, x, y):
            print("Invalid move. Try again.")
            continue
        place_move(board, x, y, current_player)
        if check_win(board, x, y, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
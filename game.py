import random

BOARD_SIZE = 19
WIN_LENGTH = 5

DIRECTIONS = [  
    (0, 1),  
    (1, 0),   
    (1, 1),   
    (-1, 1),  
]

def read_boards_from_file(filename):
    try:
        with open(filename, "r") as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")
        return []

    if not lines:
        print("Файл порожній.")
        return []

    try:
        num_tests = int(lines[0])
    except ValueError:
        print("Перша стрічка повинна містити кількість тестів.")
        return []

    lines = lines[1:]

    if len(lines) < num_tests * BOARD_SIZE:
        print("Недостатньо рядків для всіх тестів.")
        return []

    boards = []
    for i in range(num_tests):
        start = i * BOARD_SIZE
        end = start + BOARD_SIZE
        board_lines = lines[start:end]

        if len(board_lines) != BOARD_SIZE:
            print(f"Тест #{i+1}: неправильна кількість рядків.")
            continue

        board = []
        for idx, line in enumerate(board_lines):
            parts = line.split()
            if len(parts) != BOARD_SIZE:
                print(f"Тест #{i+1}, рядок {idx+1}: неправильна кількість чисел.")
                break
            try:
                row = [int(x) for x in parts]
                for val in row:
                    if val not in (0, 1, 2):
                        raise ValueError
            except ValueError:
                print(f"Тест #{i+1}, рядок {idx+1}: недопустимі значення.")
                break
            board.append(row)
        else:
            boards.append(board)

    return boards

def find_winner(board):
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            player = board[x][y]
            if player == 0:
                continue
            for dx, dy in DIRECTIONS:
                if is_winning_sequence(board, x, y, dx, dy, player):
                    return player, x + 1, y + 1  # 1-based індексація
    return 0, None, None

def is_winning_sequence(board, x, y, dx, dy, player):
    stones = [(x, y)]
    for i in range(1, WIN_LENGTH):
        nx = x + dx * i
        ny = y + dy * i
        if not (0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE):
            return False
        if board[nx][ny] != player:
            return False
        stones.append((nx, ny))

    
    nx1 = x - dx
    ny1 = y - dy
    if 0 <= nx1 < BOARD_SIZE and 0 <= ny1 < BOARD_SIZE:
        if board[nx1][ny1] == player:
            return False

    nx2 = x + dx * WIN_LENGTH
    ny2 = y + dy * WIN_LENGTH
    if 0 <= nx2 < BOARD_SIZE and 0 <= ny2 < BOARD_SIZE:
        if board[nx2][ny2] == player:
            return False

    return True

def main():
    boards = read_boards_from_file("input.txt")
    for i, board in enumerate(boards):
        winner, row, col = find_winner(board)
        print(winner)
        if winner != 0:
            print(row, col)

if __name__ == "__main__":
    main()
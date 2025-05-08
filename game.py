import random

def check_winner(board):
    directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]  
    
    for i in range(19):
        for j in range(19):
            if board[i][j] == 0:
                continue
            player = board[i][j]
            
            for di, dj in directions:
                count = 1
                x, y = i, j
                
                while count < 5:
                    x += di
                    y += dj
                    if 0 <= x < 19 and 0 <= y < 19 and board[x][y] == player:
                        count += 1
                    else:
                        break
                
                if count == 5:
                    
                    if (0 <= i - di < 19 and 0 <= j - dj < 19 and board[i - di][j - dj] == player) or \
                       (0 <= x + di < 19 and 0 <= y + dj < 19 and board[x + di][y + dj] == player):
                        continue
                    return player, i + 1, j + 1  
    
    return 0, None, None 



def main():
    with open("input.txt", "r") as f:
        data = f.read().splitlines()

    
    t = int(data[0])
    index = 1
    for _ in range(t):
        board = [list(map(int, data[index + i].split())) for i in range(19)]
        index += 19
        result, row, col = check_winner(board)
        print(result)
        if result != 0:
            print(row, col)


if __name__ == "__main__":
    main()

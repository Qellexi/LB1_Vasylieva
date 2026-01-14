BOARD_SIZE = 19
WIN_LENGTH = 5

def inside(row, col):
    return 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE


directions = [
    (0, 1),   # horizontal
    (1, 0),   # vertical
    (1, 1),   # diagonal down-right
    (-1, 1),  # diagonal up-right
]

T = int(input())

for _ in range(T):
    board = [list(map(int, input().split())) for _ in range(BOARD_SIZE)]

    winner = 0
    win_row = -1
    win_col = -1
    found_winner = False

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if found_winner:
                break

            color = board[row][col]
            if color == 0:
                continue

            for dr, dc in directions:
                for k in range(WIN_LENGTH):
                    nr = row + dr * k
                    nc = col + dc * k
                    if not inside(nr, nc) or board[nr][nc] != color:
                        break
                else:
                    # Checking next cell
                    nr = row + dr * WIN_LENGTH
                    nc = col + dc * WIN_LENGTH
                    if inside(nr, nc) and board[nr][nc] == color:
                        continue

                    # checking prev cell
                    nr = row - dr
                    nc = col - dc
                    if inside(nr, nc) and board[nr][nc] == color:
                        continue

                    winner = color
                    win_row = row + 1
                    win_col = col + 1
                    found_winner = True
                    break

    print(winner)
    if winner != 0:
        print(win_row, win_col)

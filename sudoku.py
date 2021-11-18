board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def solve(b):
    if not find_empty(b):
        print("Solved!")
        return True
    else:
        row, col = find_empty(b)

    for i in range(1, 10):
        if valid(b, i, (row, col)):
            b[row][col] = i
            if solve(b):
                return True
            b[row][col] = 0

    return False


def valid(b, num, pos):
    # Check Row
    for i in range(9):
        if b[pos[0]][i] == num and i != pos[1]:
            return False

    # Check Row
    for i in range(9):
        if b[i][pos[1]] == num and i != pos[0]:
            return False

    # Check Box
    box_row = pos[0] // 3
    box_col = pos[1] // 3
    for i in range(box_row * 3, box_row * 3 + 3):
        for j in range(box_col * 3, box_col * 3 + 3):
            if b[i][j] == num and (i, j) != pos:
                return False

    return True


def find_empty(b):
    for i in range(9):
        for j in range(9):
            if b[i][j] == 0:
                return (i,j)
    return None


def print_board(b):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("------+-------+------")
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", b[i][j], end=" ")
                else:
                    print(b[i][j], end=" ")
            print()
        else:
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", b[i][j], end=" ")
                else:
                    print(b[i][j], end=" ")
            print()


print_board(board)
solve(board)
print_board(board)

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def boardPrint(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - -')
        for j in range(len(board)):
            if j % 3 == 0 and j != 0:
                print('| ', end='')
            if j == 8:
                print(board[i][j])
            else:
                print(board[i][j], end=' ')

def checkEmpty(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (i,j)        #row, column
    return False

def validate(board, num, pos):
    #check row 
    for i in range(len(board)):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    
    #check col
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    
    #check pos
    pos_x = pos[1] // 3
    pos_y = pos[0] // 3

    for i in range(pos_y * 3, pos_y * 3 + 3):
        for j in range(pos_x * 3, pos_x * 3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True

def solve(board):
    empty = checkEmpty(board)
    if not empty:
        return True
    else:
        row, col = empty

    for num in range(1,10):
        if validate(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True
            
            board[row][col] = 0
    return False

boardPrint(board)
solve(board)
print('|------------------------------------------|')
boardPrint(board)
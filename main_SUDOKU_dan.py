board = [[0,2,4,0,0,0,0,0,0],
         [8,0,5,0,6,0,0,0,0],
         [3,0,0,0,0,0,1,5,9],
         [0,7,0,0,2,0,3,0,0],
         [0,0,1,9,0,7,6,0,0],
         [0,0,2,0,4,0,0,7,0],
         [1,5,9,0,0,0,0,0,6],
         [0,0,0,0,9,0,4,0,7],
         [0,0,0,0,0,0,9,8,0]] 
# The file has 4 functions: solve(), valid(), print_board(), find_empty() 

"""
FUNCTION (METHOD) 1 

print_board(board) - A method to print the sudoku puzzle in a visually appealing format

Arguments (input) : board - a list of nine sub lists with 9 numbers in each sub list

Output: Prints a nine x nine puzzle represented as a sudoku puzzle. Returns None.
"""

"""
FUNCTION (METHOD) 2

find_empty(board) - A method to find the next empty cell of the puzzle. Iterates from left to right and top to bottom

Arguments (input): board - a list of nine sub lists with 9 numbers in each sub list

Output: A tuple (i, j) which is index of row, column
"""

"""
FUNCTION (METHOD) 3 

valid(board, num, pos) - A method to find if a number num is valid or not

Arguments (input):
    board - a list of nine sub lists with 9 numbers in each sub list
    num - a number between 1 to 9 both inclusive
    pos - a tuple (i, j) representing row, column

Output: True if the number is valid in position pos of puzzle else False.
"""


"""
FUNCTION (METHOD) 4 (this method use the methods: find_empty(board), valid(board, num, pos))

solve(board) - A method to solve the sudoku puzzle using the other functions defined. We use a simple recursion and backtracking method.

Arguments (input): board - a list of nine sub lists with 9 numbers in each sub list

Output: Returns True once the puzzle is successfully solved else False
"""
########### FUNCTION: SOLVE #################################
def solve(b):
    find = find_empty(b)
    if not find:
        return True
    else:
        row, col = find  
    
    for i in range(1,10):
        if valid(b, i, (row, col)): # board, num, pos
            b[row][col] = i

            if solve(b):
                return True
            
            b[row][col]=0
    
    return False 


####### FUNCTION: VALID #################################### 
def valid(b, num, pos):
    # Check row 
    l = len(b)
    for i in range(l):
        if b[pos[0]][i] == num and pos[1] != i:
            return False 
    # Chek column
    for i in range(l):
        if b[i][pos[1]] == num and pos[0] != i:
            return False 
    # Check box 
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y *3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if b[i][j] == num and (i,j) != pos:
                return False 

    return True 



def print_board(b):
    l = len(b) # the length of the board 'b'
    for i in range(l):
        # forw rows: if the rest of i/3 => 0, i = [0 .. 8] => 'print line' ( the rest is zero for 0/3, 3/3, 6/3)
        if i % 3 == 0 and i !=0: print("-----"*(l-2));
        # for colomns: 
        for j in range(l):
            if j % 3 == 0 and j !=0: print(" | ", end =  " ") # if j = 0,3,6 = > print '|'
            # this 'if' is independent than previous 'if'
            if j == l-1: print(b[i][j]); # print the last column (colomn 8): [0 9 8]^t, [0 0 5]^t, [2 0 7]^t, 
            else: print(str(b[i][j]) + " ", end = " ");


def find_empty(b):
    l = len(b)
    for i in range(l):
        for j in range(l):
            if b[i][j] == 0:
                return (i,j) # row, col
    return None 


#print_board(board)
print("Unsolved")
print_board(board)
solve(board)
print("Solved")
print_board(board)


    

    
# SUDOKU_PROJECT_VAR1

Python Version 3.0+

# Sudoku Solver
"""
The file 'main_SUDOKU_dan.py' has 4 functions (methods): solve(), valid(), print_board(), find_empty() 
"""

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


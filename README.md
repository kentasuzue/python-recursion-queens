# python-recursion-queens
This Python program demonstrates basic recursion. N queens are placed on a chessboard of NXN size such that no queen can be attacked by another queen.

This program improves on the outlined program at:
https://www.hackerearth.com/practice/basic-programming/recursion/recursion-and-backtracking/tutorial/
One major bug is fixed with separate variables for the size of the board and the number of queens.  In recursive instances, the number of queens decreases but not the size of the board.  Without separate variables, the board shrinks along with the number of queens.
A first speed enhancement is to skip every row that has a queen.  A second speed enhancement is to skip every column that has a queen.
Although not coded, another possible speed enhancement is to also skip squares in every diagonal that has a queen, perhaps with a dictionary of dictionaries. 

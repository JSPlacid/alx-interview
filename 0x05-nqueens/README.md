# NQueens
![](https://camo.githubusercontent.com/b02a4ed89256eddf3d602832539675738d39b429d01f45b854d42f16eef08f11/68747470733a2f2f6d656469612e6765656b73666f726765656b732e6f72672f77702d636f6e74656e742f75706c6f6164732f726174696e6d617a655f66696c6c656431312d312d65313531383038363833353232322e706e67)

Task
The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.

- Usage: nqueens N
	- If the user called the program with the wrong number of arguments, print Usage: nqueens N, followed by a new line, and exit with the status 1
- where N must be an integer greater or equal to 4
	- If N is not an integer, print N must be a number, followed by a new line, and exit with the status 1
	- If N is smaller than 4, print N must be at least 4, followed by a new line, and exit with the status 1
- The program should print every possible solution to the problem
	- One solution per line
	- Format: see example
	- You don’t have to print the solutions in a specific order
- You are only allowed to import the sys module
Read: Queen, Backtracking


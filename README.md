# TicTacToe
Write a program called TicTacToe, which allows two users to play a single game of Tic-Tac-Toe.  Store the game board as a two-dimensional char array with three rows and three columns.

Your program should have separate methods to do each of the following:
1. Add a move to the board, prompting the user to enter the location of the next move (sample 
output is below).
2. Display the board (iterate over the array and print).
3. 3. Determine whose turn it is (the two players are X and O, and they take turns).
4. Determine if there is a winner using a method called checkForWinner which you will be given 
(I will provide the code for this method in a separate file on Canvas; all you need to do is paste 
the method in the program and call it when necessary). This method accepts your game board 
char array as an argument. It returns true if a winner was found, and returns false if not. You 
should call this method after each move. 
5. Display the winner. (Hint: X always goes first, so you might want to keep track of the number 
of moves each player had.)
6. Reinitialize the game to the beginning state (in other words, clear the board).
Write a main() method that will allow the user to play the game at the keyboard. Both players 
will sit at the keyboard and enter their moves in turn.
For entering moves, the row and column numbers should correspond to the indices of the 
array, so they start at zero.

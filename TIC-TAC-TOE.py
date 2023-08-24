'''Write a program called TicTacToe, which allows two users to play a single game of Tic-Tac-Toe. 
Store the game board as a two-dimensional char array with three rows and three columns.
Your program should have separate methods to do each of the following:
1. Add a move to the board, prompting the user to enter the location of the next move (sample 
output is below).
2. Display the board (iterate over the array and print). Something similar to this will work:
for (int row = 0; row < 3; row++)
 {
 for (int col = 0; col < 3; col++)
 {
 System.out.print("[" + b[row][col] + "]"); 
 }//end for col
 System.out.println();
 }//end for row 
3. Determine whose turn it is (the two players are X and O, and they take turns).
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
array, so they start at zero. A sample run might look something like this:'''
import sys
def fild_reset():
    b='\n'
    a='[ ]'
    f_d=[]
    d_fild = ''
    for i in range(3):
        for j in range(3):
            f_d.append(a)
        f_d.append(b)
    d_fild=''.join(f_d)
    print(d_fild)
    return f_d
def move_input(n='row/column'):
    i=0
    j=0
    while i<1:
        x1=input(f'Enter the {n} of your move:')
        if x1.isdigit() and int(x1)<4:
            i=1
            return int(x1)
        else:
            print('Invalid input')
            j+=1
        if j>3: 
           sys.exit()
def fild_refresh(symbol = 'x', f_list_r=None, r = 1, c = 1):
    if f_list_r is None:
        return None
    f_list_r[len(f_list_r) - 1] = ' '
    row=r
    column=c
    if row>2:
        column += 2
    elif row>1:
        column += 1
    x=3*(row-1)+column
    if f_list_r[x-1] == '[ ]':
        f_list_r[x-1] = f'[{symbol}]'
        fild=''.join(f_list_r)
        print(fild)
    else:
        print('This cell is occupied, choose another pls')
        f_list_r[len(f_list_r)-1]='.'
    return f_list_r

def result_check(f_list_r,row,column):
    s=[0,0,0,0]
    for i in range(3):
        a=4*i+column-1
        if f_list_r[a] == f_list_r[column-1] and f_list_r[column-1] != '[ ]':
            s[0] += 1
        a=4*(row-1)+i
        if f_list_r[a] == f_list_r[4*(row-1)] and f_list_r[4*(row-1)] != '[ ]':
            s[1] += 1
        if f_list_r[i*5] == f_list_r[0] and f_list_r[0] != '[ ]':
            s[2] += 1
        if f_list_r[i*3+2] == f_list_r[2] and f_list_r[2] != '[ ]':
            s[3] += 1
    win = False
    for i in s:
        if i==3:
            win = True
            break
    return win

f_list = fild_reset()
i=1
while i>0:
    if i%2 == 0:
        var = '0'
    else:
        var = 'x'

    z=input(f"It's {var} move now. Continue(C) or Restart(R)? (C/R)")
    if z.lower() == 'c':
        row = move_input('row')
        column = move_input('column')
        f_list = fild_refresh(var, f_list, row, column)
        if f_list[len(f_list)-1] != '.':
            i+=1
    elif z.lower() == 'r':
        f_list = fild_reset()
        i = 1
    else:
        i = -1
    if result_check(f_list,row, column):
        print(f'Game over. The player {var} won.')
        z=input(f"Do you wont to Restart(R)?")
        if z.lower() == 'r':
            f_list = fild_reset()
            i = 1
        else:
            i = -1
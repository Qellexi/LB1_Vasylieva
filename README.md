The game

A game of Renju is played on 19x19 board by two players. One player uses black stones and the
other player uses white stones. The game begins on an empty board and two players alternate in
placing black stones and white stones. Black always goes first. There are 19 horizontal and 19
vertical lines on the board, and the stones are placed on the intersections of the lines.

Horizontal lines are marked 1,2,…19 from up to down, and vertical lines are marked 1,2,…19
from left to right as shown on Figure 1.

The objective of this game is to put five stones of the same color consecutively along a horizontal,
vertical and diagonal line. So, black wins in Fig. 1. But, a player does not win the game if more than
five stones of the same color were put consecutively.


Given a configuration of the game, write a program to determine whether white has won, or black
has won, or nobody has won yet. There will be no input data where the black and the white both
win at the same time. Also, there will be no input data where the white or the black wins in more
than one place.


Input

The first line of the input file contains a single integer (1<= x <= 11), the number of test cases,
followed by the input data for each test case. Each test case consists of 19 lines, each having 19
numbers. A black stone is denoted by 1, a white stone is denoted by 2, and 0 denotes no stone.

Output

There should be one or two lines per test case. In the first line of the test case output, you should
print 1 if black wins, 2 if white wins, and 0 if nobody wins yet. If black or white won, in the second
line print the horizontal line number and the vertical line number of the leftmost stone among the
five consecutive stones. (Select the uppermost stone if the five consecutive stones are located
vertically.)

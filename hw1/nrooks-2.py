#!/usr/bin/env python
# nrooks.py : Solve the N-Rooks problem!
# D. Crandall, 2016
# Updated by Zehua Zhang, 2017
#
# The N-rooks problem is: Given an empty NxN chessboard, place N rooks on the board so that no rooks
# can take any other, i.e. such that no two rooks share the same row or column.

import sys

# Count # of pieces in given row
def count_on_row(board, row):
    return sum( board[row] ) 

# Count # of pieces in given column
def count_on_col(board, col):
    return sum( [ row[col] for row in board ] ) 

# Count total # of pieces on board
def count_pieces(board):
    return sum([ sum(row) for row in board ] )

# Return a string with the board rendered in a human-friendly format
def printable_board(board):
    return "\n".join([ " ".join([ "R" if col else "_" for col in row ]) for row in board])

# Add a piece to the board at the given position, and return a new board (doesn't change original)
def add_piece(board, row, col):
    return board[0:row] + [board[row][0:col] + [1,] + board[row][col+1:]] + board[row+1:]

# Get list of successors of given board state
def successors(board):
    return [ add_piece(board, r, c) for r in range(0, N) for c in range(0,N) ]

def add_piece2(board, row, col):
    # print(board)
    if(board[row][col]==1 or (count_on_col(board,col)>0 or count_on_row(board,row)>0)): # validation for checking whether a rook is already placed the position and the validation for checking whether a rook is present in that row or column, which would ultimately handle the case wherein number of pieces exceedes N.
        return -1
    # if(count_pieces(board)>=N): # validation for number of rooks not exceeding N
    #     return -1
    
    return board[0:row] + [board[row][0:col] + [1,] + board[row][col+1:]] + board[row+1:]

def successors2(board):
    values = [ add_piece2(board, r, c) for r in range(0, N) for c in range(0,N) ]
    valid = list(filter(lambda a:a!=-1,values)) #remove the invalid states returned by add_piece2
    return valid

def add_piece3(board, row, col):
    # print(board)
    if(board[row][col]==1 or sum(board[row])!=0 or sum(row[col] for row in board)!=0):
        return -1
    # if(col!=0 and (sum(row[col-1] for row in board) == 0)): # validate that a rook is only added in order of the column
    #     return -1

    return board[0:row] + [board[row][0:col] + [1,] + board[row][col+1:]] + board[row+1:]

def successors3(board):
    # values = [ add_piece3(board, r, c) for r in range(0, N) for c in range(0,N) ]
    values = []
    for r in range(0,N):
        if(sum(board[r])==0 and True if r==0 else sum(board[r-1])!=0 ):
            for c in range(N):
                values.append(add_piece3(board,r,c))

    # print(list(filter(lambda a:a!=-1,values)))
    valid = list(filter(lambda a:a!=-1,values))
    return list(filter(lambda a:sum(map(sum,a))<=N,valid))

# check if board is a goal state
def is_goal(board):
    return count_pieces(board) == N and \
        all( [ count_on_row(board, r) <= 1 for r in range(0, N) ] ) and \
        all( [ count_on_col(board, c) <= 1 for c in range(0, N) ] )

# Solve n-rooks!
def solve(initial_board):
    count = 0
    fringe = [initial_board]
    while len(fringe) > 0:
        # if(count%50000 == 0):
            # print(str(len(fringe))+"\n\n")
        for s in successors3( fringe.pop() ):
            count = count+1
            if is_goal(s):
                return(s)
            fringe.append(s)
    return False

# This is N, the size of the board. It is passed through command line arguments.
N = int(sys.argv[1])

from time import time
# N=i
t0 = time()
# The board is stored as a list-of-lists. Each inner list is a row of the board.
# A zero in a given square indicates no piece, and a 1 indicates a piece.
initial_board = [[0]*N]*N
print ("Starting from initial board:\n" + printable_board(initial_board) + "\n\nLooking for solution...\n")
solution = solve(initial_board)
print (printable_board(solution) if solution else "Sorry, no solution found. :(")


# if time()-t0 <= 60 and solution!=False:
#     print(N)
# if time()-t0>60:
print(time()-t0)
#     break




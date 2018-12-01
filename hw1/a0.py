#!/usr/bin/env python3
import sys

algo = str(sys.argv[1]) # nqueen or nrook or nknight

N = int(sys.argv[2]) # size of board

no = int(sys.argv[3]) # number of unwanted positions

naPoints = [] # will store the list of unwanted coordinates

# store the unwanted coordinates
for i in range(no):
	naPoints.append([int(sys.argv[4+i*2]), int(sys.argv[5+i*2])])


# Return a string with the board rendered in a human-friendly format
def printable_board(board):
	return "\n".join([ " ".join([ ((("K" if algo=="nknight" else "R" if algo=="nrook" else "Q") if col==1 else ("X" if col==-1 else "_")) if col else "_") for col in row ]) for row in board])

# add 'val' to all the positions to which the knight at board[row][col] can reach in one step
def setKnight(board,row,col,val):
	global N
	r=row
	c=col
	r=r-2
	c=c-1

	# update the 2 positions to the top of board[row][col]
	while(r in range(0,N) and c in range(0,N)):
		if(board[r][c]!=-1):
			board[r][c]=board[r][c]+val
		c=col+1
		if(c in range(0,N) and (board[r][c]!=-1) ):
			board[r][c]=board[r][c]+val
		break;
	r=row
	c=col
	r=r+1
	c=c-2

	# update the 2 positions to the left of board[row][col]
	while(r in range(0,N) and c in range(0,N)):
		if(board[r][c]!=-1):
			board[r][c]=board[r][c]+val
		r=row-1
		if(r in range(0,N) and (board[r][c]!=-1) ):
			board[r][c]=board[r][c]+val
		break;
	r=row
	c=col
	r=r-1
	c=c+2

	# update the 2 positions to the right of board[row][col]
	while(r in range(0,N) and c in range(0,N)):
		if(board[r][c]!=-1):
			board[r][c]=board[r][c]+val
		r=row+1
		if(r in range(0,N) and (board[r][c]!=-1) ):
			board[r][c]=board[r][c]+val
		break;
	r=row
	c=col
	r=r+2
	c=c-1

	# update the 2 positions to the bottom of board[row][col]
	while(r in range(0,N) and c in range(0,N)):
		if(board[r][c]!=-1):
			board[r][c]=board[r][c]+val
		c=col+1
		if(c in range(0,N) and (board[r][c]!=-1) ):
			board[r][c]=board[r][c]+val
		break;

	return board

# add 'val' to all the positions to which the knight at board[a][b] can reach in one step
def setDiagonal(board,a,b,val): #add 'val' to all the elements to the diagonal of board[a,b]
	global N
	i=1
	j=1
	# update the 2 positions in the top-left of board[a][b]
	while(a-i>=0 and b-j>=0):
		if(board[a-i][b-j]!=-1):
			board[a-i][b-j] = board[a-i][b-j] + val
		i=i+1
		j=j+1

	i=1
	j=1
	# update the 2 positions in the bottom-left of board[a][b]
	while(a+i<N and b-j>=0):
		if(board[a+i][b-j]!=-1):
			board[a+i][b-j] = board[a+i][b-j] + val
		i=i+1
		j=j+1

	i=1
	j=1
	# update the 2 positions in the top-right of board[a][b]
	while(a-i>=0 and b+j<N):
		if(board[a-i][b+j]!=-1):
			board[a-i][b+j] = board[a-i][b+j] + val
		i=i+1
		j=j+1

	i=1
	j=1
	# update the 2 positions in the bottom-right of board[a][b]
	while(a+i<N and b+j<N):
		if(board[a+i][b+j]!=-1):
			board[a+i][b+j] = board[a+i][b+j] + val
		i=i+1
		j=j+1

	return board

# 'solve' is recursively called one by one for each row
def solve(board,row=0, rowTrack=[0]*N, colTrack=[0]*N):

	#rowTrack keeps the count of the number of rooks/queens in the ith row
	#colTrack keeps the count of the number of rooks/queens in the ith column

	global N
	i=row
	for j in range(N):
		# check if a rook/queen/knight can be placed at position board[i][j]
		# if a rook/queen/knight which is already placed, can attack the rook/queen/knight at board[i][j], the value of board[i][j] would be a multiple of -2
		# only if no other rook/queen/knight can attack at position board[i][j], can the value at board[i][j] be 0
		if(board[i][j]==0 and colTrack[j]==0):
			board[i][j] = 1
			# after placing a rook/queen/knight at board[i][j], we need to add -2 to all the positions where the rook/queen/knight can attack.(To indicate that in future nobody places a rook/queen/knight at those attacked positions)
			if(algo=="nknight"):
				board = setKnight(board,i,j,-2)
			else:
				if(algo=="nqueen"):
					board = setDiagonal(board,i,j,-2)
				rowTrack[i]=1
				colTrack[j]=1
			# print()
			# print(printable_board(board))

			# rook/queen/knight is placed in the last row also, so now it can return the goal board
			if(row==N-1):
				return board

			# recursively solve the board from the next row
			ans = solve(board,row+1,rowTrack, colTrack)

			# if a solution is not found we need to backtrack
			if(ans==False):
				board[i][j] = 0 # reverse value of board[i][j] from 1 to 0
				# revert the attacked positions on the board by adding 2 to those positions
				if(algo=="nknight"):
					board = setKnight(board,i,j,2)
				else:
					if(algo=="nqueen"):
						board = setDiagonal(board,i,j,2)
					rowTrack[i]=0
					colTrack[j]=0
			else:
				return board;

	return False # no solution found


initial_board = [[0]*N for i in range(N)]

for na in naPoints:
	initial_board[na[0]-1][na[1]-1] = -1

#rowTrack keeps the count of the number of rooks/queens in the ith row
#colTrack keeps the count of the number of rooks/queens in the ith column
rowTrack = [0] * N
colTrack = [0] * N

solution = solve(initial_board,0,rowTrack, colTrack)

print(printable_board(solution) if solution else "Sorry, no solution found. :(")



# Note: I have referred stackoverflow.com and docs.python.org for getting some insight into python syntax
# I have also referred piazza for queries relating to the assignment.

#The N Queen is the problem of placing N chess queens on an N×N chessboard so that no two queens attack each other.
def initialize(board,n):
	for key in ['queen','row','col','rhdia','lhdia']:
		board[key] = {}
	for i in range(n):
		board['queen'][i] = -1
		board['row'][i] = 0
		board['col'][i] = 0
	for i in range(-(n-1),n):
		board['rhdia'][i] = 0
	for i in range(2*n - 1):
		board['lhdia'][i] = 0
def printboard(board):
	for row in sorted(board['queen'].keys()):
		print((row,board['queen'][row]))
def free(i,j,board):
	return (board['row'][i]==0 and board['col'][j] == 0 and board['rhdia'][j-i] == 0 and board['lhdia'][i+j] == 0)
def addqueen(i,j,board):
	board['queen'][i] = j
	board['row'][i] = 1
	board['col'][j] = 1
	board['rhdia'][j-i] = 1
	board['lhdia'][j+i] = 1

def subtractqueen(i,j,board):
	board['queen'][i] = -1
	board['lhdia'][j+i] = 0
	board['col'][j] = 0
	board['rhdia'][j-i] = 0
	board['row'][i] = 0
def placequeen(board,i):
	n = len(board['queen'].keys())
	for y in range(n):
		if free(i,y,board):
			addqueen(i,y,board)
			if i == n-1:
				return(True)
			recurssion = placequeen(board,i+1)
			if recurssion:
				return(True)
			else:
				subtractqueen(i,y,board)
	else:
		return(False)
board = {}
n = int(input("Enter the board order to place Queens"))
initialize(board,n)
placequeen(board,0)
printboard(board)

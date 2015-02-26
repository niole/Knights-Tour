def isvalid(n,row,col,board):
    if board[col][row] == 0:
        return True
    return False

def findmoves(row,col,board):
    baserow = [row+y for y in [2,-2] if row+y < len(board) and row+y > -1]
    basecol = [col+x for x in [2,-2] if col+x < len(board) and col+x > -1]
    extendbasecol= [row+y for y in [1,-1] if row+y < len(board) and row+y > -1]
    extendbaserow = [col+x for x in [1,-1] if col+x < len(board) and col+x > -1]
    moves = [[x,y] for y in baserow for x in extendbaserow]+[[z,a] for z in basecol for a in extendbasecol]
    return moves

#B = [[0 for _ in range(5)] for _ in range(5)]
#B[2][2] = 1
#B = [[0 for _ in range(3)] for _ in range(3)]
#assert(findmoves(2,2,B) == [[0,1,0,1,0],[1,0,0,0,1],[0,0,1,0,0],[1,0,0,0,1],[0,1,0,1,0]]) #assert(findmoves(0,0,B) == [[0,0,0],[0,0,1],[0,1,0]]) 
def addmove(n,row,col,board):
    newboard = [[board[i][j] for j in range(len(board))] for i in range(len(board))]
    newboard[col][row] = n
    return newboard

def printboard(board):
    print '-'*20
    for row in board:
        print map(lambda x: "%2i" % x, row)

#assert(addmove(2,2,2,[[0,0,0],[0,0,0],[0,0,0]]) == [[0,0,0],[0,0,0],[0,0,2]])

def placeknight(n,row,col,board):
    """
    Press any key once a solution is outputted to ask
    the program to continue searching for solutions.
    """
    if n == len(board)**2:
        print printboard(board)
        raw_input() # pause on solution
    for m in filter(lambda x: isvalid(n,x[1],x[0],board), findmoves(row,col,board)):
        newboard = addmove(n+1,m[1],m[0],board)
        placeknight(n+1,m[1],m[0],newboard)

size = 5
b = [[0 for _ in range(size)] for _ in range(size)]
b[0][0] = 1
placeknight(1,0,0,b)

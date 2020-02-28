# check if square x,y is attaced by any queen on board
def attacked(x, y, board, N):
    #check row x
    for j in range(N):
        if board[x][j] == 1:
            #print("board", x, j, "is", board[x][j])
            #for i in range(N):
                #for j in range(N):
                    
                    #print(board[i][j], end = " ")
                #print()

            return True
    
    #check column x
    for i in range(N):
        if board[i][y] == 1:
            return True

    #check diagonals
    for i in range(N):
        j1 = x + y - i
        j2 = -x + y + i
        if j1 >= 0 and j1 < N and board[i][j1] == 1:
            return True
        if j2 >= 0 and j2 < N and board[i][j2] == 1:
            return True
        #for j in range(N):
            #if (x + y) == (i + j) and board[i][j] == 1:
                #return True
            #if (x - y) == (i - j) and board[i][j] == 1:
                #return True
    
    return False

def nQueens(board, N, queens, iset, jset):
    if queens == 0:
        return True

    for i in range(N):
        if i in iset:
            continue
        jsetcopy = set(jset)
        
        for j in jsetcopy:
            if attacked(i, j, board, N):
                continue
            board[i][j] = 1
            iset.add(i)
            jset.discard(j)
            if nQueens(board, N, queens - 1, iset, jset):
                #print("N", N, "i", i, "j", j)
                return True
            board[i][j] = 0
            iset.discard(i)
            jset.add(j)

N = int(input())
board = [[0 for j in range(N)] for i in range(N)]
iset = set()
jset = set(range(N))

if __name__ == '__main__':
    if nQueens(board, N, N, iset, jset):
        print("YES")
        for i in range(N):
            for j in range(N):
                print(board[i][j], end = " ")
            print()
    else:
        print("NO")

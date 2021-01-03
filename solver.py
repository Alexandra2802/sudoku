board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(bo):
    for i in range(len(bo)):
        if i%3==0 and i!=0:
            print('-----------------')
        for j in range(len(bo[0])):
            if j%3==0 and j!=0:
                print('|',end='')
            if j==8:
                print(bo[i][j])
            else:
                print(str(bo[i][j])+' ',end='')



def find_empty(bo):
    '''
    Gaseste un spatiu liber pe tabla
    :param bo: tabla
    :return: pozitia spatiului liber,tuplu incare primul element e linia si al doilea coloana
    sau None daca tabla e completa
    '''
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j]==0:
                return (i,j) #linia,coloana
    return None

#print(find_empty(board))

def check_valid(bo,nr,poz):
    '''
    Verifica daca numarul pus pe tabla e valid
    :param bo: tabla
    :param nr: numarul introdus
    :param poz: pozitia numarului introdus
    :return: True daca e valida si False altfel
    '''

    #verificare linie
    for i in range(9):
        if bo[poz[0]][i]==nr and poz[1]!=i:
            return False

    #verificare coloana
    for i in range(9):
        if bo[i][poz[1]]==nr and poz[0]!=i:
            return False

    #verificare careu mic
    box_x=poz[1]//3
    box_y=poz[0]//3

    for i in range(box_y*3,box_y*3+1):
        for j in range(box_x*3,box_x*3+1):
            if bo[i][j]==nr and (i,j)!=poz:
                return False
    return True


#print(check_valid(board,3,(0,2)))

def solve(bo):
    empty=find_empty(bo)
    if not empty:
        return True
    else:
        row,col=empty

    for i in range(1,10):
        if check_valid(bo,i,(row,col))==True:
            bo[row][col]=i

            if solve(bo):
                return True

            bo[row][col]=0

    return False






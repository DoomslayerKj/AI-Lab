#Vaccuumm Clean by VaradKJ

def clean(floor):
    cpy_floor = floor
    print(floor)
    i=0
    j=0
    rows = len(cpy_floor)
    cols = len(cpy_floor[0])

    for row_index, row in enumerate(cpy_floor):
        for col_index, item in enumerate(row):
            if cpy_floor[row_index][col_index]==1:
                print_floor(floor, row_index, col_index)
                cpy_floor[row_index][col_index] = 0

    print('Cleaned Floor = ')
    for x in cpy_floor:
        print (x,sep=', ')





def print_floor(floor, row, col): # row, col represent the current vacuum cleaner position
    cpy_floor=floor
    value=cpy_floor[row][col]
    print('\n')
    print('Floor= ',row)
    print('Tile= ',col)
    for row in cpy_floor:
        print(*row, sep=', ')




floor = [[1, 0, 0, 0],
         [0, 1, 0, 1],
         [1, 0, 1, 1]]

clean(floor)
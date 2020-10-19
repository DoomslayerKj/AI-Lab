import os,psutil
process = psutil.Process(os.getpid())

def bfs(src, target):
    arr = [src]
    c = 0
    count=0
    while arr:
        count+=1
        print("\nIteration = {}".format(count))
        print('Possible Moves for {} = \n{} '.format(arr[0],arr[0:]))
        print('\n')
        print('Took {} MB'.format(process.memory_info()[0]/1000000))

        if (target == arr[0]):
            print('Took {} MB'.format(process.memory_info()[0]/1000000))
            return("Took {} Iterations".format(count))



        arr+=possible_moves(arr[0])
        arr.pop(0)

    return 'Not Found'


    # for i in range(100):
        # temp=possible_moves(src)
        # print(temp)
        # states.append(temp)
        # if temp == target:
        #     print("Found")
        #     break


def possible_moves(state):
    b = state.index(-1)  # Find index of empty spot
    d = []  # 'd' : down, 'u': up ..... directions
    pos_moves = []  # if dir is possible to go then add to state to move

    if b <= 5:  # to go down, empty spot should be in the first 2 rows
        d.append('d')

    if b >= 3:  # to go up, empty spots should be in the bottom 2 rows
        d.append('u')

    if b % 3 > 0:  # to go left, empty spots should be in the right most 2 columns
        d.append('l')

    if b % 3 < 2:  # to go right, empty spots should be in the left most 2 columns
        d.append('r')

    for i in d:  # for i in "all possble directions"

        temp = gen(state, i, b)  # generate the state if slide empty spot to one of the directions

        pos_moves.append(temp)  # add temp to possible moves to check if

    return pos_moves
def gen(state, m, b):  # m(move) is direction to slide, b(blank) is index of empty spot
    temp = state.copy()  # create a copy of current state to test the move

    if m == 'l':  # if move is to slide empty spot to the left
        temp[b], temp[b - 1] = temp[b - 1], temp[b]  # switch postions so a = b and b = a

    if m == 'r':  # if move is to slide empty spot to the right
        temp[b], temp[b + 1] = temp[b + 1], temp[b]

    if m == 'u':  # if move is to slide empty spot to the top
        temp[b], temp[b - 3] = temp[b - 3], temp[b]

    if m == 'd':  # if move is to slide empty spot to the bottom
        temp[b], temp[b + 3] = temp[b + 3], temp[b]

    return temp

src = [1, 2, 3, 4, 5, 6, 7, 8, -1]
target = [-1, 8, 7, 6, 5, 4, 3, 2, 1]  # Only one position is changed(to Test)

depth = 1
print(bfs(src, target))
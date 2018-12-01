import numpy as np
import queue


class states(object):
    def __init__(self, cost, data, toReachCost):
        self.cost = cost
        self.data = data
        self.toReachCost = toReachCost
        return

    def __lt__(self, other):
        return self.cost < other.cost


def cost(mat, N):
    costsx = np.zeros((N, N))
    costsy = np.zeros((N, N))
    c = 0
    for i in range(N):
        for j in range(N):
            val = mat[i][j]
            valx = (int)((val - 0.1) / 4)
            valy = (val - 1) % 4
            dx = (valx - i)
            dy = (valy - j)
            if abs(dx) == 3:
                dx = dx / (-3)
            if abs(dy) == 3:
                dy = dy / (-3)
            if abs(dx) == 2:
                dx = 2
            if abs(dy) == 2:
                dy = 2
            costsx[i][j] = dx
            costsy[i][j] = dy

    ax = (np.amax(np.count_nonzero(costsx == 1), axis=0))
    by = (np.amax(abs(costsy), axis=1))

    xplusMax = xminusMax = yplusMax = yminusMax = 0
    for i in range(N):
        # if (1 in costsx[:,i] and -1 in costsx[:,i]):
        # 	ax[i] = 2
        # if (1 in costsy[i,:] and -1 in costsy[i,:]):
        # 	by[i] = 2
        xplusMax = max(xplusMax, np.count_nonzero(costsx[i, :] == 1))
        xminusMax = max(xminusMax, np.count_nonzero(costsx[i, :] == -1))
        yplusMax = max(yplusMax, np.count_nonzero(costsy[:, i] == 1))
        yminusMax = max(yminusMax, np.count_nonzero(costsy[:, i] == -1))

    xMax = xplusMax + xminusMax
    yMax = yplusMax + yminusMax

    xBool = 0
    yBool = 0
    for i in range(N):
        if (((np.count_nonzero(costsy[:, i] == 1) == yplusMax and yplusMax!=0) or (np.count_nonzero(
                costsy[:, i] == -1) == yminusMax and yminusMax!=0)) and np.count_nonzero(costsy[:, i] == 2) != 0):
            yBool = max(yBool, np.count_nonzero(costsy[:, i] == 2))
        if (((np.count_nonzero(costsx[i, :] == 1) == xplusMax and xplusMax!=0) or (np.count_nonzero(
                costsx[i, :] == -1) == xminusMax and xminusMax!=0)) and np.count_nonzero(costsx[i, :] == 2) != 0):
            xBool = max(xBool, np.count_nonzero(costsx[i, :] == 2))
    if xBool:
        xMax = xMax + xBool

    if yBool:
        yMax = yMax + yBool

    # c = max(max(ax)+np.count_nonzero(ax)-1, max(by)+np.count_nonzero(by)-1)
    # print(costsx)
    # print(ax)
    # print(costsy)
    # print(by)
    return xMax + yMax


def solve(state, N):
    mat = np.copy(state.data)
    global que
    global hashDict
    actual = np.copy(mat)

    for i in range(N):
        temp = mat[i][1]
        t2 = 0
        mat[i][1] = mat[i][0]
        t2 = mat[i][2]
        mat[i][2] = temp
        temp = mat[i][3]
        mat[i][3] = t2
        mat[i][0] = temp

        hashBoard = hash(str(mat))
        if hashBoard not in hashDict:
            que.put(states(cost(mat, 4) + state.toReachCost, np.copy(mat), state.toReachCost + 1))
            hashDict[hashBoard] = 1
        # print(np.array2string(mat, separator=', '))
        # print(cost(mat,4))
        # print()
        mat = np.copy(actual)

    for i in range(N):
        temp = mat[1][i]
        t2 = 0
        mat[1][i] = mat[0][i]
        t2 = mat[2][i]
        mat[2][i] = temp
        temp = mat[3][i]
        mat[3][i] = t2
        mat[0][i] = temp

        hashBoard = hash(str(mat))
        if hashBoard not in hashDict:
            que.put(states(cost(mat, 4) + state.toReachCost, np.copy(mat), state.toReachCost + 1))
            hashDict[hashBoard] = 1
        # print(np.array2string(mat, separator=', '))
        # print(cost(mat,4))
        # print()
        mat = np.copy(actual)

    for i in range(N):
        temp = mat[i][1]
        t2 = 0
        mat[i][1] = mat[i][2]
        t2 = mat[i][0]
        mat[i][0] = temp
        temp = mat[i][3]
        mat[i][3] = t2
        mat[i][2] = temp

        hashBoard = hash(str(mat))
        if hashBoard not in hashDict:
            que.put(states(cost(mat, 4) + state.toReachCost, np.copy(mat), state.toReachCost + 1))
            hashDict[hashBoard] = 1
        # print(np.array2string(mat, separator=', '))
        # print(cost(mat,4))
        # print()
        mat = np.copy(actual)

    for i in range(N):
        temp = mat[1][i]
        t2 = 0
        mat[1][i] = mat[2][i]
        t2 = mat[0][i]
        mat[0][i] = temp
        temp = mat[3][i]
        mat[3][i] = t2
        mat[2][i] = temp

        hashBoard = hash(str(mat))
        if hashBoard not in hashDict:
            que.put(states(cost(mat, 4) + state.toReachCost, np.copy(mat), state.toReachCost + 1))
            hashDict[hashBoard] = 1
        # print(np.array2string(mat, separator=', '))
        # print(cost(mat,4))
        # print()
        mat = np.copy(actual)


# print(actual)

# x = [[1,14,3,4],[8,2,6,7],[9,5,11,12],[13,10,15,16]]
# x = [[ 1, 14,  3,  4],
#  	[ 2,  6,  7,  8],
#  	[ 5, 11, 12,  9],
#  	[13, 10, 15, 16]]

# x = [[13,5,1,16],[2,9,10,3],[4,15,14,6],[12,8,11,7]]

x= [[5, 7, 8, 1],
[10, 2, 4, 3],
[6 ,9 ,11 ,12],
[15 ,13 ,14, 16]]

# x = [[1, 6, 3, 4],
#      [5, 9, 7, 8],
#      [12, 14, 10, 11],
#      [13, 2, 15, 16]]

# x = [[1, 13, 3, 8],
#      [5, 2, 7, 12],
#      [9, 6, 11, 14],
#      [15, 16, 10, 4]]

# x= [[15 ,13 ,3 ,8],
# [12 ,1, 2 ,7 ],
# [5 ,6, 11 ,14],
# [9 ,16, 10, 4]]

# x= [[1 ,2 ,3 ,13],
# [4 ,6, 12 ,16 ],
# [5 ,10, 11 ,7],
# [14 ,15, 8, 9]]


x = np.array(x)

hashDict = {}
hashDict[hash(str(x))] = 1

que = queue.PriorityQueue()

que.put(states(cost(x, 4) + 0, np.copy(x), 0))

count = 0

from time import time

start = time()
while not que.empty():
    # count = count + 1
    best = que.get()
    # print(best.toReachCost, best.cost)
    # if count % 100 == 0:
    #     print()
    # print(np.array2string(best.data, separator=', '))
    if cost(best.data, 4) <= 0:
        print('\n')
        print(best.toReachCost, count)
        break
    solve(best, 4)

print(time() - start)







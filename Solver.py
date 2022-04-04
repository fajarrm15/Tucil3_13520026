# Library algoritma

import copy
from heapq import heappush, heappop

def Reachable(arr):
    costCount = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            costG = 0
            for k in range(i,len(arr)):
                for l in range(j,len(arr[0])):
                    if(arr[i][j] < arr[k][l]):
                        costG += 1
            costCount += costG
            if(arr[i][j]==16):
                if(((i+1)%2!=0) and ((j+1)%2==0)):
                    costCount += 1
                elif(((i+1)%2==0) and ((j+1)%2!=0)):
                    costCount += 1
    if(costCount%2==0):
        return True
    else:
        return False

def calculateCost(mat, final):
    count = 0
    for i in range(len(mat)):
        for j in range(len(mat)):
            if ((mat[i][j] != final[i][j])):
                count += 1
                 
    return count

class PrioQueue:
    def __init__(self):
        self.pq = []

    def enqueue(self,item):
        heappush(self.pq, item)
        
    def dequeue(self):
        return heappop(self.pq)
        
    def isEmpty(self):
        if not self.pq:
            return True
        else:
            return False



def isSafe(x, y):
    return x >= 0 and x < 4 and y >= 0 and y < 4

def findBlankCoor(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(matrix[i][j]==16):
                return (i,j)

class node:
    def __init__(self,parent,matrix,cost,depth):
        self.parent = parent
        self.matrix = matrix
        self.cost = cost
        self.depth = depth

    def __lt__(self,other):
        return (self.cost+self.depth) < (other.cost+other.depth)

def newNode(parent,matrix,final,move):
    newMatrix = copy.deepcopy(matrix)
    blankCoor = findBlankCoor(matrix)
    x = blankCoor[0] + move[0]
    y = blankCoor[1] + move[1]
    newMatrix[x][y],newMatrix[blankCoor[0]][blankCoor[1]] = newMatrix[blankCoor[0]][blankCoor[1]],newMatrix[x][y]

    depth = parent.depth + 1
    newcost = calculateCost(newMatrix,final)
    return node(parent,newMatrix,newcost,depth)

def solvePuzzle(initial,final):
    move = [[1,0],[0,1],[-1,0],[0,-1]]
    pq = PrioQueue()
    cost = calculateCost(initial,final)
    root = node(None,initial,cost,0)
    pq.enqueue(root)

    while not pq.isEmpty():
        current = pq.dequeue()
        print(current.cost)
        if(current.cost==0):
            print("Solved")
        else:
            for i in range(len(move)):
                temp = findBlankCoor(current.matrix)
                x = temp[0] + move[i][0]
                y = temp[1] + move[i][1]
                if(isSafe(x,y)):
                    tempNode = newNode(current,current.matrix,final,move[i])
                    pq.enqueue(tempNode)


test = [[1,3,4,8],[5,2,7,12],[9,6,11,15],[13,10,14,16]]
final = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

solvePuzzle(test,final)
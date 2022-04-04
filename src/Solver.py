# Library algoritma

import copy
from heapq import heappop,heappush

def Reachable(arr):
    costCount = 0
    dict = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0}
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            costG = 0
            k = i
            l = j
            while(k<len(arr)):
                while(l<len(arr[0])):
                    if(arr[i][j] > arr[k][l]):
                        costG += 1
                    l += 1
                l = 0
                k += 1
            dict[arr[i][j]] = costG
            costCount += costG
    x,y = findBlankCoor(arr)
    if(((x+1)%2!=0) and ((y+1)%2==0)):
        costCount += 1
    elif(((x+1)%2==0) and ((y+1)%2!=0)):
        costCount += 1
    return costCount,dict

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

    def isEmpty(self):
        if not self.pq:
            return True
        else:
            return False

    def enqueue(self,item):
        heappush(self.pq, item)
        
    def dequeue(self):
        return heappop(self.pq)

def isSafe(x, y):
    return x >= 0 and x < 4 and y >= 0 and y < 4

def findBlankCoor(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(matrix[i][j]==16):
                return (i,j)

class node:
    totalNode = 0
    def __init__(self,parent,matrix,cost,depth):
        self.parent = parent
        self.matrix = matrix
        self.cost = cost
        self.depth = depth
        node.totalNode += 1
    
    def __lt__(self, nxt):
        return (self.cost + self.depth) < (nxt.cost + nxt.depth)

def newNode(parent,matrix,final,move):
    newMatrix = copy.deepcopy(matrix)
    blankCoor = findBlankCoor(matrix)
    x = blankCoor[0] + move[0]
    y = blankCoor[1] + move[1]
    newMatrix[x][y],newMatrix[blankCoor[0]][blankCoor[1]] = newMatrix[blankCoor[0]][blankCoor[1]],newMatrix[x][y]

    if(parent.parent is not None):
        if(parent.parent.matrix == newMatrix):
            return None
        else:
            cost = calculateCost(newMatrix,final)
            depth = parent.depth + 1
            return node(parent,newMatrix,cost,depth)
    else:
        cost = calculateCost(newMatrix,final)
        depth = parent.depth + 1
        return node(parent,newMatrix,cost,depth)

def solvePuzzle(initial,final):
    move = [[1,0],[0,1],[-1,0],[0,-1]]
    solved = False

    pq = PrioQueue()
    cost = calculateCost(initial,final)
    root = node(None,initial,cost,0)
    pq.enqueue(root)

    while (not pq.isEmpty() and not solved):
        current = pq.dequeue()
        if(current.cost==0):
            solved = True
        else:
            for i in range(len(move)):
                temp = findBlankCoor(current.matrix)
                x = temp[0] + move[i][0]
                y = temp[1] + move[i][1]
                if(isSafe(x,y)):
                    tempNode = newNode(current,current.matrix,final,move[i])
                    if(tempNode is not None):
                        pq.enqueue(tempNode)
    return current

def printMatrix(matrix):
    for i in range(len(matrix)):
        print("#----#----#----#----#")
        for j in range(len(matrix[0])):
            if(matrix[i][j]==16):
                print("|   ",end="")
            elif(matrix[i][j]>9):
                print("| "+str(matrix[i][j]),end="")
            else:
                print("| " + str(matrix[i][j]) + " ",end="")
            if(j==3):
                print(" |",end="")
            else:
                print(" ",end="")
        print()
    print("#----#----#----#----#")

def printPath(node):
    if(node.parent is not None):
        printPath(node.parent)
        print("\t  |")
        print("\t  |")
        print("\t  V")
    printMatrix(node.matrix)

def printKurangFunc(initial):
    flag,kurangDict = Reachable(initial)
    print("-----------------------------")
    print("|    i     |    kurang(i)   |")
    print("-----------------------------")
    for i in range(1,17):
        if(i<10):
            if(kurangDict[i]>9):
                print("|    "+str(i)+"     |        "+str(kurangDict[i])+"      |")
            else:
                print("|    "+str(i)+"     |        "+str(kurangDict[i])+"       |")
        else:
            if(kurangDict[i]>9):
                print("|    "+str(i)+"    |        "+str(kurangDict[i])+"      |")
            else:
                print("|    "+str(i)+"    |        "+str(kurangDict[i])+"       |")
            
    print("-----------------------------")
    print("Nilai fungsi kurang: ",flag)







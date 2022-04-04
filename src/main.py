import Solver as Sv
import os
import random
import time

if __name__ == "__main__":
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("|   Welcome to the 15-puzzle solver!   |")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("|                                      |")
    print("|                                      |")
    print("----------------------------------------")
    print("Choose your input:")
    initialMatrix = []
    finalMatrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    n = int(input("1. Random Generator\n2. From Text File\n"))
    if(n==1):
        randomlist2 = random.sample(range(1, 5), 4)
        randomlist3 = random.sample(range(5, 9), 4)
        randomlist = random.sample(range(9, 17), 8)
        initialMatrix.append(randomlist2)
        initialMatrix.append(randomlist3)
        k = 0
        for i in range(2):
            temp = []
            for j in range(4):
                temp.append(randomlist[k])
                k+=1
            initialMatrix.append(temp)
    else:
        tempMatrix = []
        print("Ket: file harus berada dalam folder test")
        fileName = input("Input your test file name (ex: test1.txt) : ")
        path = r'../test/'
        with open(path+fileName, 'r') as f:
            for line in f.readlines():
                tempMatrix.append(line.split(' '))
        
        for i in range(len(tempMatrix)):
            temp = []
            for j in range(len(tempMatrix[0])):
                temp.append(int(tempMatrix[i][j]))
            initialMatrix.append(temp)
    print("----------------------------------------")
    print("\nYour initial matrix: ")
    Sv.printMatrix(initialMatrix)
    print("\n")
    Sv.printKurangFunc(initialMatrix)
    value,_ = Sv.Reachable(initialMatrix)
    if(value%2==0):
        print("\nYour initial matrix is solvable!")
        print("Here is the steps to solve it:")
        start = time.time()
        solvedPuzzle = Sv.solvePuzzle(initialMatrix, finalMatrix)
        Sv.printPath(solvedPuzzle)
        end = time.time()
        print("\nElapsed Time for solving: ", end-start)
        print("\nTotal Node: ",solvedPuzzle.totalNode)
    else:
        print("\nYour initial matrix is not solvable!")

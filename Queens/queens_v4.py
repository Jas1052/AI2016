# most constrained, random
import time
import math
import heapq
from collections import deque
import copy
import random
from random import shuffle

class nQueens:
    def __init__(self, state=None, choices=None, n=None, parent=None):
        """ creates an nQueens board where state is a list of n integers,
            one per column,
            and choices is a list of sets,
            n is the size
            parent is the state predecessor in a search
        """

        if n is None:
            print "problem with n"
            self.n = 8
        else:
            self.n = n

        if state is None:
            self.state = []
            for i in range(self.n):
                self.state.append(-1)
        else:
            self.state = state

        if choices is None:
            self.choices = []
            sub = set([])
            for a in range(self.n):  # puts 0 through 7 inclusive into sub
                sub.add(a)
            for i in range(self.n):  # puts sub into choices
                self.choices.append(copy.copy(sub))
        else:
            self.choices = choices

        if parent is not None:
            self.parent = parent

    def assign(self, var, value):
        """ updates the state by setting state[var] to value
            also propgates constraints and updates choices
        """
        self.state[var] = value
        for column in self.choices:
            column.difference_update([value])  # removes row
        self.choices[var] = set([])  # removes column

        for xindex in range(len(self.choices)):              # iterate through sets in choice
            column = self.choices[xindex]                       # naming the set as column
            tempcol = copy.copy(column)
            for y in tempcol:                             # iterate through available rows in column
                if abs(y - value) == abs(xindex - var):    # check in y,x is a diagonal
                    column.difference_update([y])          # remove row val in column set

    def goal_test(self):
        """ returns True iff state is the goal state """
        if -1 in self.state:
            return False
        else:
            return True

    def get_next_unassigned_var(self):
        """ Returns the index of a column that is unassigned and
            has valid choices available """
        """
        i = 0
        mid = self.n//2
        if self.n%2 == 0:
            while mid - i > -1:
                randomVal = random.randint(0, self.n - 1)
                if self.state[randomVal] is -1:
                    return randomVal
        else:
            while mid + i < self.n:
                randomVal = random.randint(0, self.n - 1)
                if self.state[randomVal] is -1:
                    return randomVal"""

        pos = 0
        shortest = self.n
        for i in range(len(self.choices)):
            newpos = i
            newshortest = len(self.choices[i])
            if newshortest < shortest and newshortest != 0:
                shortest = newshortest
                pos = newpos
        return pos



    def get_choices_for_var(self, var):
        """ returns choices[var], the list of available values
             for variable var, possibly sorted """
        while(True):
            randomVal = random.randint(0, self.n - 1)
            if len(self.choices[randomVal]) != 0:
                return self.choices[randomVal]


    def __str__(self):
        """ returns a string representation of the object """
        return ''.join(str(e) + '  ' for e in self.state)

###---------------------------------------------------------------


def dfs_search(board):
    """ sets board as the initial state and returns a
        board containing an nQueens solution
        or None if none exists
    """
    count = 0
    goalcount = 0
    fringe = deque([])
    fringe.append(board)
    while(True):
        if len(fringe) is 0:
            print("Empty Fringe")
            return
        n = fringe.pop()
        # print(n)
        goalcount = goalcount + 1
        if n.goal_test():
            print goalcount
            print count
            return
        column = n.get_next_unassigned_var()
        tempcol = random.sample(n.choices[column], len(n.choices[column]))
        for val in tempcol:
            count = count + 1
            child = nQueens(copy.deepcopy(n.state), copy.deepcopy(n.choices), copy.deepcopy(n.n), n)
            child.assign(column, val)
            fringe.append(child)
# ----------------------------------------------------------------

for i in range(5,150,3):
    begin = time.time()
    print '\n'
    print i
    board = nQueens(n=i)
    dfs_search(board)
    end = time.time()

    timer = str(round(end - begin, 3))
    print timer

"""
/usr/bin/python2.7 "/home/jliu/Documents/Link to Senior/AI/Queens/queens_v4.py"


5
[2, 0, 3, 1, 4]
10
0.001


8
[0, 6, 3, 5, 7, 1, 4, 2]
53
0.01


11
[10, 7, 1, 4, 0, 8, 3, 9, 6, 2, 5]
404
0.07


14
[10, 3, 11, 9, 7, 4, 1, 12, 0, 6, 8, 5, 2, 13]
66
0.016


17
[13, 9, 14, 0, 7, 16, 2, 5, 12, 10, 4, 6, 11, 15, 1, 3, 8]
628
0.138


20
[6, 18, 0, 15, 8, 12, 7, 3, 17, 2, 5, 13, 4, 10, 19, 14, 16, 11, 9, 1]
280
0.081


23
[4, 13, 19, 14, 5, 7, 2, 16, 8, 15, 3, 21, 17, 20, 22, 0, 11, 1, 10, 18, 6, 9, 12]
161
0.069


26
[18, 22, 19, 23, 6, 10, 25, 21, 12, 7, 4, 0, 5, 16, 20, 24, 11, 2, 14, 3, 17, 9, 13, 15, 1, 8]
418
0.175


29
[28, 6, 21, 3, 18, 25, 9, 19, 17, 7, 1, 10, 8, 26, 20, 23, 11, 2, 0, 13, 4, 22, 14, 27, 5, 12, 15, 24, 16]
277
0.166


32
[28, 1, 16, 6, 10, 26, 14, 17, 19, 3, 9, 2, 29, 22, 12, 7, 5, 21, 30, 24, 27, 18, 8, 0, 25, 20, 11, 15, 4, 31, 23, 13]
406
0.256


35
[26, 8, 27, 32, 28, 5, 1, 24, 19, 10, 15, 17, 31, 4, 0, 30, 25, 7, 20, 23, 3, 13, 11, 21, 34, 12, 14, 9, 2, 22, 33, 16, 29, 6, 18]
659
0.412


38
[25, 15, 26, 6, 11, 2, 7, 20, 18, 1, 10, 34, 31, 21, 35, 37, 14, 29, 22, 5, 16, 23, 9, 32, 13, 8, 3, 12, 33, 28, 36, 4, 0, 27, 24, 19, 17, 30]
513
0.431


41
[36, 23, 27, 6, 19, 15, 22, 40, 0, 39, 12, 24, 31, 25, 4, 29, 3, 17, 13, 20, 5, 32, 11, 7, 30, 1, 14, 35, 37, 34, 16, 38, 28, 8, 33, 26, 9, 18, 21, 10, 2]
554
0.536


44
[39, 13, 29, 1, 30, 41, 34, 3, 19, 15, 31, 26, 0, 16, 18, 33, 40, 25, 17, 35, 37, 2, 23, 43, 38, 8, 4, 36, 21, 14, 6, 22, 32, 5, 24, 9, 11, 42, 27, 12, 20, 28, 10, 7]
4067
2.46


47
[1, 24, 6, 37, 22, 19, 31, 20, 4, 33, 3, 0, 7, 18, 35, 46, 38, 43, 17, 9, 28, 12, 16, 39, 26, 34, 10, 14, 2, 36, 41, 8, 13, 30, 40, 45, 21, 15, 5, 27, 32, 44, 42, 25, 23, 11, 29]
656
0.828


50
[35, 38, 9, 11, 2, 8, 47, 21, 44, 20, 0, 13, 36, 43, 40, 25, 22, 49, 18, 48, 45, 16, 42, 32, 10, 1, 4, 23, 41, 34, 29, 46, 14, 37, 15, 27, 7, 24, 3, 6, 17, 30, 5, 31, 28, 39, 12, 26, 33, 19]
833
1.162


53
[26, 32, 29, 37, 9, 14, 50, 39, 15, 28, 1, 31, 24, 52, 20, 10, 8, 27, 0, 49, 7, 43, 33, 46, 17, 4, 6, 35, 11, 23, 5, 44, 48, 51, 36, 25, 13, 41, 34, 38, 18, 42, 40, 2, 47, 45, 30, 19, 3, 12, 21, 16, 22]
821
1.314


56
[23, 42, 48, 50, 6, 15, 10, 25, 28, 18, 27, 53, 17, 4, 41, 44, 54, 30, 33, 14, 55, 45, 52, 49, 43, 46, 13, 35, 16, 1, 8, 37, 29, 9, 24, 21, 5, 40, 2, 7, 51, 39, 3, 20, 38, 12, 47, 22, 0, 11, 31, 36, 32, 26, 19, 34]
1134
1.808


59
[14, 56, 30, 52, 37, 28, 5, 46, 38, 21, 29, 40, 32, 53, 51, 57, 24, 11, 31, 12, 23, 55, 20, 2, 34, 36, 42, 33, 10, 18, 4, 49, 16, 58, 41, 0, 26, 8, 25, 54, 45, 9, 27, 44, 35, 22, 6, 43, 50, 15, 47, 3, 7, 48, 17, 1, 39, 13, 19]
1115
1.938


62
[22, 11, 23, 26, 45, 49, 51, 61, 38, 42, 46, 59, 18, 3, 0, 57, 21, 36, 10, 16, 14, 20, 60, 35, 9, 56, 1, 15, 32, 37, 25, 55, 41, 50, 54, 28, 12, 48, 5, 53, 40, 24, 8, 2, 47, 7, 33, 31, 27, 13, 19, 58, 43, 6, 17, 44, 52, 4, 39, 30, 34, 29]
1134
2.449


65
[31, 45, 64, 58, 5, 10, 17, 0, 50, 19, 40, 61, 24, 49, 11, 33, 38, 12, 25, 56, 29, 62, 41, 22, 6, 48, 30, 13, 57, 8, 2, 59, 15, 35, 23, 60, 42, 7, 53, 55, 34, 39, 63, 27, 9, 37, 21, 4, 36, 20, 46, 14, 52, 26, 1, 16, 32, 44, 18, 28, 51, 3, 47, 43, 54]
1252
3.734


68
[67, 5, 24, 57, 52, 29, 51, 46, 16, 30, 42, 12, 7, 62, 56, 43, 34, 19, 37, 50, 66, 64, 60, 6, 44, 0, 23, 36, 63, 22, 53, 15, 49, 59, 3, 65, 35, 4, 41, 39, 8, 47, 32, 54, 58, 17, 1, 18, 61, 10, 27, 25, 28, 13, 40, 9, 45, 38, 14, 2, 33, 55, 11, 21, 26, 31, 48, 20]
1383
3.39


71
[21, 23, 53, 50, 56, 61, 16, 18, 48, 27, 49, 35, 15, 66, 40, 32, 2, 31, 8, 20, 14, 28, 30, 65, 17, 13, 7, 68, 47, 63, 67, 54, 36, 45, 39, 9, 64, 5, 38, 24, 46, 57, 1, 70, 33, 6, 25, 34, 10, 58, 52, 43, 51, 4, 37, 12, 69, 55, 3, 11, 44, 19, 59, 26, 29, 0, 62, 42, 22, 60, 41]
1452
5.0


74
[21, 45, 73, 26, 51, 43, 59, 15, 39, 71, 4, 8, 44, 61, 16, 2, 55, 28, 46, 17, 11, 57, 68, 60, 64, 47, 53, 10, 0, 62, 19, 31, 66, 37, 1, 23, 48, 30, 22, 63, 56, 3, 34, 69, 25, 41, 6, 54, 33, 24, 65, 52, 7, 67, 40, 32, 12, 9, 5, 38, 50, 70, 27, 58, 13, 35, 72, 18, 14, 49, 29, 42, 20, 36]
2248
7.083


77
[11, 70, 62, 51, 17, 25, 47, 58, 65, 0, 60, 27, 76, 23, 8, 57, 1, 15, 48, 5, 3, 26, 29, 68, 4, 20, 50, 56, 28, 52, 49, 18, 14, 2, 71, 75, 6, 55, 22, 13, 74, 37, 45, 69, 53, 44, 73, 61, 63, 9, 43, 10, 16, 32, 66, 72, 24, 46, 19, 40, 64, 34, 38, 35, 54, 31, 41, 59, 7, 21, 67, 33, 12, 36, 39, 42, 30]
2480
8.03


80
[29, 5, 9, 16, 28, 13, 57, 67, 26, 76, 12, 58, 65, 74, 41, 25, 79, 18, 53, 14, 36, 40, 1, 21, 23, 64, 70, 75, 60, 35, 11, 7, 47, 19, 56, 69, 50, 54, 61, 42, 17, 8, 68, 0, 34, 27, 46, 78, 45, 24, 15, 71, 77, 62, 22, 66, 10, 37, 51, 48, 72, 52, 20, 4, 33, 3, 32, 59, 55, 43, 30, 49, 44, 2, 6, 31, 38, 73, 39, 63]
2101
7.95


83
[29, 4, 61, 71, 66, 81, 63, 48, 19, 34, 44, 28, 20, 6, 51, 11, 22, 65, 0, 21, 47, 52, 73, 56, 54, 25, 49, 62, 3, 12, 76, 46, 17, 13, 1, 57, 55, 14, 9, 5, 82, 40, 74, 53, 39, 43, 10, 15, 32, 8, 78, 60, 33, 41, 72, 68, 42, 2, 50, 38, 30, 75, 69, 36, 80, 7, 27, 79, 16, 18, 64, 58, 37, 31, 26, 35, 77, 24, 67, 70, 23, 59, 45]
1998
8.427


86
[39, 8, 52, 14, 12, 26, 69, 19, 64, 74, 57, 44, 9, 66, 73, 7, 3, 21, 41, 59, 48, 31, 15, 23, 53, 5, 10, 17, 65, 27, 81, 22, 84, 0, 70, 6, 82, 85, 58, 24, 72, 43, 28, 49, 62, 50, 63, 2, 18, 11, 80, 78, 29, 32, 36, 16, 13, 79, 30, 42, 75, 4, 76, 51, 67, 61, 47, 40, 77, 25, 83, 37, 71, 1, 68, 35, 45, 55, 46, 38, 54, 56, 33, 20, 60, 34]
4093
13.419


89
[70, 87, 58, 26, 54, 66, 34, 0, 77, 47, 5, 1, 64, 55, 14, 75, 7, 19, 24, 40, 61, 65, 69, 21, 79, 88, 12, 23, 6, 86, 81, 48, 52, 44, 63, 2, 13, 62, 17, 57, 83, 71, 68, 31, 43, 3, 16, 18, 4, 33, 84, 82, 11, 45, 73, 9, 80, 10, 20, 60, 41, 46, 67, 37, 30, 72, 74, 28, 78, 85, 50, 53, 76, 36, 42, 39, 49, 29, 15, 51, 25, 27, 22, 59, 8, 32, 35, 56, 38]
3262
11.27


92
[23, 13, 43, 56, 4, 73, 45, 41, 79, 22, 26, 42, 71, 64, 51, 29, 78, 46, 10, 89, 7, 25, 20, 68, 74, 80, 28, 5, 38, 55, 0, 39, 50, 8, 18, 14, 60, 81, 19, 75, 49, 88, 59, 17, 3, 52, 57, 72, 24, 84, 12, 48, 82, 11, 34, 87, 44, 47, 86, 15, 21, 66, 6, 58, 9, 30, 1, 63, 54, 40, 91, 53, 35, 2, 77, 27, 67, 16, 61, 32, 69, 31, 83, 76, 90, 70, 37, 33, 65, 36, 62, 85]
2437
13.459


95
[50, 87, 27, 88, 17, 51, 65, 45, 56, 80, 70, 64, 0, 89, 63, 34, 74, 62, 49, 75, 43, 16, 48, 1, 71, 92, 15, 57, 29, 9, 94, 42, 67, 3, 19, 10, 79, 41, 58, 44, 26, 18, 40, 12, 81, 61, 8, 69, 38, 36, 84, 78, 6, 59, 66, 76, 20, 4, 86, 22, 32, 93, 91, 55, 47, 82, 73, 2, 68, 5, 72, 52, 33, 31, 13, 85, 25, 23, 77, 35, 30, 54, 39, 24, 14, 28, 83, 53, 21, 60, 7, 46, 11, 37, 90]
2876
15.327


98
[94, 70, 90, 11, 15, 24, 72, 32, 34, 46, 20, 57, 64, 25, 4, 69, 83, 8, 97, 43, 53, 51, 23, 86, 22, 75, 26, 66, 93, 84, 19, 35, 28, 65, 41, 82, 14, 6, 31, 88, 62, 29, 37, 60, 10, 16, 91, 85, 5, 55, 47, 56, 13, 81, 68, 30, 50, 92, 61, 74, 96, 44, 12, 1, 87, 17, 21, 59, 40, 49, 7, 58, 71, 89, 36, 48, 78, 3, 18, 2, 45, 9, 42, 0, 54, 27, 95, 33, 73, 63, 38, 67, 39, 77, 80, 76, 52, 79]
3019
16.912


101
[91, 7, 64, 44, 68, 79, 84, 42, 55, 5, 15, 13, 71, 76, 48, 86, 77, 82, 38, 62, 99, 57, 4, 65, 50, 33, 45, 96, 83, 23, 25, 3, 21, 17, 27, 63, 10, 88, 90, 95, 73, 28, 1, 43, 97, 72, 31, 59, 0, 26, 87, 100, 16, 92, 11, 9, 70, 2, 69, 81, 40, 51, 20, 24, 85, 14, 19, 98, 34, 94, 37, 39, 8, 89, 18, 58, 32, 80, 93, 52, 56, 22, 61, 75, 46, 12, 74, 35, 6, 67, 60, 30, 78, 53, 41, 66, 36, 47, 49, 54, 29]
3312
18.3


104
[17, 32, 66, 16, 55, 25, 72, 98, 1, 45, 80, 64, 49, 0, 46, 95, 83, 5, 67, 62, 47, 27, 48, 51, 40, 100, 18, 22, 99, 54, 7, 85, 15, 75, 81, 36, 84, 52, 19, 101, 13, 96, 60, 93, 88, 34, 12, 57, 70, 94, 73, 41, 20, 77, 26, 90, 42, 65, 37, 35, 24, 30, 3, 68, 2, 4, 78, 10, 43, 31, 6, 82, 21, 92, 103, 71, 11, 29, 8, 38, 89, 79, 86, 14, 58, 69, 53, 9, 87, 74, 23, 33, 63, 56, 44, 39, 61, 97, 76, 102, 91, 28, 50, 59]
3123
20.589


107
[87, 106, 66, 85, 11, 25, 2, 93, 102, 31, 29, 56, 84, 7, 63, 39, 86, 1, 10, 75, 94, 58, 3, 76, 21, 92, 57, 44, 99, 34, 42, 70, 105, 47, 16, 83, 8, 0, 59, 100, 72, 64, 9, 17, 82, 71, 15, 89, 37, 74, 40, 95, 23, 6, 67, 101, 22, 12, 35, 60, 78, 13, 96, 48, 68, 41, 49, 62, 54, 4, 103, 69, 80, 30, 18, 91, 104, 14, 26, 5, 50, 81, 97, 61, 24, 43, 77, 33, 98, 20, 51, 90, 65, 32, 73, 55, 52, 46, 36, 79, 45, 88, 53, 28, 38, 19, 27]
3347
23.987


110
[92, 83, 106, 80, 36, 65, 74, 48, 45, 3, 26, 89, 17, 100, 23, 30, 70, 15, 63, 43, 8, 68, 105, 27, 19, 53, 34, 76, 21, 40, 61, 2, 88, 71, 96, 101, 82, 20, 18, 51, 59, 54, 109, 42, 78, 6, 98, 14, 81, 84, 22, 7, 69, 93, 12, 97, 104, 10, 13, 38, 46, 35, 31, 47, 1, 67, 11, 103, 58, 79, 24, 5, 99, 91, 95, 32, 41, 39, 56, 9, 55, 72, 85, 64, 90, 108, 37, 50, 73, 25, 66, 87, 62, 57, 94, 102, 44, 28, 0, 16, 77, 4, 29, 52, 86, 33, 107, 75, 60, 49]
3523
24.627


113
[111, 29, 89, 107, 109, 26, 94, 86, 33, 100, 95, 10, 34, 62, 59, 91, 60, 8, 0, 96, 68, 73, 16, 79, 104, 36, 45, 42, 99, 63, 71, 20, 18, 75, 21, 31, 24, 5, 40, 82, 12, 103, 55, 38, 101, 4, 106, 1, 102, 81, 70, 80, 66, 108, 14, 3, 7, 13, 37, 57, 22, 6, 92, 9, 48, 72, 83, 19, 65, 11, 97, 77, 27, 74, 52, 98, 46, 58, 39, 44, 90, 84, 2, 15, 93, 49, 112, 87, 41, 64, 61, 67, 50, 76, 25, 85, 88, 105, 78, 56, 43, 35, 23, 53, 28, 110, 69, 17, 30, 32, 54, 51, 47]
3702
31.296


116

"""
'''
TASK: You're in a climbing competition. You start with some stamina which is a positive integer number and you have obstacles in a list. Each number in the list represents obstacle height.
While climbing up you lose 2 stamina for up to 1 meter climb. So if you climb 1.8 meter you lose 4 stamina (2 for 1 meter and 2 for 0.8 meter) and so on.
While climbing down you lose 1 stamina for you up to 1 meter climbed. So, if you climb 0.5 meter you lose 1 stamina, if you climb 1.2 meter you lose 2 stamina (1 for 1 meter and 1 for 0.2 meter) etc.
You start by standing on the first obstacle in the list.
Given a stamina number and a list of obstacles, write a function that returns how many obstacles you can pass.

TEST CASE:
INPUT               | OUTPUT
9 //size of array   | 3    
5                   |       
4.2                 |       
3                   |       
3.5                 |       
6                   |       
4                   |       
6                   |       
8                   |       
1                   |       
5 //stamina         |       
----------------------------
4 //size of array   |       
0                   |       
1                   |       
2.5                 |       
0.8                 |       
5 //stamina         |   
----------------------------

NOTES:
-> In all test cases: Stamina is integer and greater than 0, all numbers in lists are positive floats or integers.
-> The result should be integer.
'''

from typing import list

def getCountOfObstacles(obstacles:list[float],stamina:int)->int:
    count = 0
    return count
climbingObstacles = []
sizeOfObstacles = int(input("Enter the number of obstacles: "))
for i in range(sizeOfObstacles):
    obstacleSize = float(input("Enter the size of {} obstacle: ".format(i+1)))
    climbingObstacles.append(obstacleSize)
stamina = int(input("Enter stamina amount: "))
print("You can pass {} out of {} with {}".format(getCountOfObstacles(climbingObstacles,stamina),sizeOfObstacles,stamina))
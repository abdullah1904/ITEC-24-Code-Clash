'''
TASK: You're given a 0-indexed integer array nums os size 3 which can form the sides of a triangle
A triangle is equilateral if it has all the sides of equal length
A triangle is isosceles if it has exactly two sides of equal length
A triangle is scalene if all its sides are of different lengths
Return a string representing the type of triangle that can be formed or 'none' if it cannot form a triangle

TEST CASES:
INPUT | OUTPUT
3     | Equilateral
3     | 
3     |
-------------------
3     | Scalene
4     | 
5     |

NOTES: 
-> nums.length == 3
-> 1<= nums[i] <= 100
'''

def typeOfTriangle(list)->str:
    if list[0] <= 0 or list[1] <= 0 or list[2] <= 0:
        return "none"
    elif list[0] + list[1] <= list[2]:
        return "none"
    else:
        if list[0] == list[1] == list[2]:
            return 'equilateral'
        elif list[0] == list[1] or list[1] == list[2] or list[2] == list[0]:
            return 'Isosceles'
        else:
            return 'scalene'

sidesOfTriangle = []
for i in range(3):
    side = int(input("Enter side {}: ".format(i+1)))
    sidesOfTriangle.append(side)
print("The given triangle is {}".format(typeOfTriangle(sidesOfTriangle)))

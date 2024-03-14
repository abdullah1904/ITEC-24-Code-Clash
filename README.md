<div align="center"><img src="UETCSLogo.png" width="35%"></div>
<h1 align="center">ITEC'24 Code Clash</h1>
<p>Had an amazing experience tackling challenging programming problems alongside <a href="https://github.com/ABDULAHAD118">Abdulahad Hussain</a> at the ITEC 2024 Code Clash! We put our problem-solving skills to the test and learned a ton. Big thanks to Software Square and the Department of Computer Science, UET Lahore for the fantastic event.</p>

<h2 align='center'>Problems</h2>
<h3>Pentagonal Number:</h3>
<p>Write a function that takes a positive integer number and calculates how many dots exist in a pentagonal shape around the center dot on the Nth iteration.<br/>First iteration is only a single dot. On the second, there are 6 dots. On the third, there are 16 dots and on the fourth there are 31 dots <br/>Return the number of dots that exist in the whole pentagon on the Nth iteration.</p>

<h4>TEST CASES:</h4>
<table>
  <thead>
    <th>Input</th>
    <th>Output</th>
  </thead>
  <tr>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>2</td>
    <td>6</td>
  </tr>
  <tr>
    <td>8</td>
    <td>141</td>
  </tr>
</table>

```py
def pentagonalNumber(num:int)->int:
    if num <= 0:
        return -1
    elif num == 1:
        return 1
    else:
        countofDots = 1
        for i in range(2,num+1):
            countofDots += (i-1) * 5
        return countofDots

numberOfPentagon = int(input("Enter the Number of Pentagon: "))
print(f"The number of dots in {numberOfPentagon} pentagons is {pentagonalNumber(numberOfPentagon)}")
```

<hr/>
<h3>Pentagonal Number:</h3>
<p>You're in a climbing competition. You start with some stamina which is a positive integer number and you have obstacles in a list. Each number in the list represents obstacle height.<br/>While climbing up you lose 2 stamina for up to 1 meter climb. So if you climb 1.8 meter you lose 4 stamina (2 for 1 meter and 2 for 0.8 meter) and so on.<br/>While climbing down you lose 1 stamina for you up to 1 meter climbed. So, if you climb 0.5 meter you lose 1 stamina, if you climb 1.2 meter you lose 2 stamina (1 for 1 meter and 1 for 0.2 meter) etc.<br/>You start by standing on the first obstacle in the list.<br/>Given a stamina number and a list of obstacles, write a function that returns how many obstacles you can pass.</p>

<h4>TEST CASES:</h4>
<table>
  <thead>
    <th>Input</th>
    <th>Output</th>
  </thead>
  <tr>
    <td>9 (Size of Array)<br/>5<br/>4.2<br/>3<br/>3.5<br/>6<br/>4<br/>6<br/>8<br/>1<br/>5 (Stamina)</td>
    <td>3</td>
  </tr>
  <tr>
    <td>4 (Size of Array)<br/>0<br/>1<br/>2.5<br/>0.8<br/>5 (Stamina)</td>
    <td>1</td>
  </tr>
</table>

<h4>NOTES:</h4>
<ul>
  <li>In all test cases: Stamina is integer and greater than 0, all numbers in lists are positive floats or integers.</li>
  <li>The result should be integer.</li>
</ul>

```py
from typing import List
import math

def getCountOfObstacles(obstacles:List[float],stamina:int)->int:
    count = 0
    for i in range(len(obstacles)-2):
        if obstacles[i] < obstacles[i+1]:
            staminaRequired = math.ceil(obstacles[i+1] - obstacles[i])*2
            if stamina >= staminaRequired:
                count += 1
                stamina -= staminaRequired
            else:
                break
        elif obstacles[i] > obstacles[i+1]:
            staminaRequired = math.ceil(obstacles[i] - obstacles[i+1])
            if stamina >= staminaRequired:
                count += 1
                stamina -= staminaRequired
            else:
                break
    return count
climbingObstacles = []
sizeOfObstacles = int(input("Enter the number of obstacles: "))
for i in range(sizeOfObstacles):
    obstacleSize = float(input("Enter the size of {} obstacle: ".format(i+1)))
    climbingObstacles.append(obstacleSize)
stamina = int(input("Enter stamina amount: "))
print("You can pass {} out of {} with {} stamina".format(getCountOfObstacles(climbingObstacles,stamina),sizeOfObstacles,stamina))
```

<hr/>
<h3>Type of Triangle:</h3>
<p>You're given a 0-indexed integer array nums of size 3 which can form the sides of a triangle<br/>A triangle is equilateral if it has all the sides of equal length<br/>A triangle is isosceles if it has exactly two sides of equal length<br/>A triangle is scalene if all its sides are of different lengths<br/>Return a string representing the type of triangle that can be formed or 'none' if it cannot form a triangle</p>

<h4>TEST CASES:</h4>
<table>
  <thead>
    <th>Input</th>
    <th>Output</th>
  </thead>
  <tr>
    <td>3<br/>3<br/>3</td>
    <td>Equilateral</td>
  </tr>
  <tr>
    <td>3<br/>4<br/>5</td>
    <td>Scalene</td>
  </tr>
</table>

<h4>NOTES:</h4>
<ul>
  <li>nums.length == 3</li>
  <li>1 <= nums[i] <= 100</li>
</ul>

```py
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
```

<hr/>
<h3>Ant on the Boundary:</h3>
<p>An ant is on the boundary. It sometimes goes left and sometimes right.<br/>You're given an array of non-zero integer nums. The ant starts reading nums from the first element of it to its end. At each step, it moves according to the value of the current element:</p>
<ul>
  <li>if nums[i] < 0, it moves left by -nums[i] units</li>
  <li>if nums[i] > 0, it moves right by nums[i] units</li>
</ul>
<p>Return the number of times the ant returns to the boundary</p>

<h4>TEST CASES:</h4>
<table>
  <thead>
    <th>Input</th>
    <th>Output</th>
  </thead>
  <tr>
    <td>3 (Size of Array)<br/>2<br/>3<br/>-5</td>
    <td>1</td>
  </tr>
  <tr>
    <td>4 (Size of Array)<br/>3<br/>2<br/>-3<br/>-4</td>
    <td>0</td>
  </tr>
</table>

<h4>NOTES:</h4>
<ul>
  <li>There is an infinite space on the both sides of the boundary.</li>
  <li>We check whether the ant is on the boundary only after it has moved nums[i] units. In the other words, if the ant crosses the boundary during its movement, it does not count.</li>
  <li>1 <= nums.length <= 100</li>
  <li>-10 <= nums[i] <= 10</li>
  <li>nums[i] != 0</li>
</ul>

```py
def boundaryTouch(list:int)->int:
    count = 0
    distance = 0
    for i in list:
        distance += i
        if distance == 0:
            count+=1
    return count

sizeOfSteps = []
countOfSteps = int(input("Enter how many times ant moves: "))
for i in range(countOfSteps):
    stepSize = int(input("Enter {} step size: ".format(i+1)))
    sizeOfSteps.append(stepSize)
print("The {} times ant touched the boundary.".format(boundaryTouch(sizeOfSteps)))
```
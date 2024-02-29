'''
TASK: An ant is on the boundary. It sometimes goes left and sometimes right.
You're given an array of non-zero integer nums. The ant starts reading nums from the first element of it to its end. At each step, it moves according to the value of the current element:
-> if nums[i] < 0, it moves left by -nums[i] units
-> if nums[i] > 0, it moves right by nums[i] units
Return the number of times the ant returns to the boundary

TEST CASE:
INPUT             | OUTPUT
3 //size of array | 1     
2                 |       
3                 |       
-5                |       
--------------------------
4 //size of array | 0    
3                 |       
2                 |       
-3                | 
-4                | 
--------------------------

Note:
-> There is an infinite space on the both sides of the boundary.
-> We check whether the ant is on the boundary only after it has moved nums[i] units. In the other words, if the ant crosses the boundary during its movement, it does not count. 
-> 1<= nums.length <=100
-> -10 <= nums[i] <= 10
-> nums[i] != 0
'''

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

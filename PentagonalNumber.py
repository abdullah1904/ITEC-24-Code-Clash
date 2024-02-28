'''
TASK: Write a function that takes a positive integer number and calculates how many dots exist in a pentagonal shape around the center dot on the Nth iteration.
First iteration is only a single dot. On the second, there are 6 dots. On the third, there are 16 dots and on the fourth there are 31 dots
Return the number of dots that exist in the whole pentagon on the Nth iteration

TEST CASES:
INPUT | OUTPUT
1     | 1
2     | 6
8     | 141
'''
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
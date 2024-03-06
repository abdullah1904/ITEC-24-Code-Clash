<div align="center"><img src="UETCSLogo.png" width="35%"></div>
<h1 align="center">ITEC'24 Code Clash</h1>
<p>Had an amazing experience tackling challenging programming problems alongside <a href="https://github.com/ABDULAHAD118">Abdulahad Hussain</a> at the ITEC 2024 Code Clash! We put our problem-solving skills to the test and learned a ton. Big thanks to Software Square and the Department of Computer Science, UET Lahore for the fantastic event.</p>

<h2 align='center'>Problems</h2>
<h3>Pentagonal Number:</h3>
<p>Write a function that takes a positive integer number and calculates how many dots exist in a pentagonal shape around the center dot on the Nth iteration.<br/>
First iteration is only a single dot. On the second, there are 6 dots. On the third, there are 16 dots and on the fourth there are 31 dots <br/>
Return the number of dots that exist in the whole pentagon on the Nth iteration.</p>

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

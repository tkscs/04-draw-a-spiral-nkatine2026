import turtle
from scipy.constants import golden as phi

"""
In a golden spiral, for every 90 degrees, the arm length of the spiral grows
by a factor of phi (which is approximately 1.618)

So if the spiral has so far turned 90 degrees i times, then the current arm
length will be:

initial_arm_length * (phi**i)
"""

### YOUR CODE STARTS HERE
turtle.speed(500)
for i in range(5):
    turtle.forward(10*phi**i)
    turtle.right(90)

### YOUR CODE ENDS HERE

turtle.exitonclick()
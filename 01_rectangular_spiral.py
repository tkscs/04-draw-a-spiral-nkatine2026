import turtle
from scipy.constants import golden as phi
"""
Make a rectangular spiral (see the README.md for an example)
"""

### YOUR CODE STARTS HERE
turtle.speed(500)
for i in range(5):
    turtle.forward(10*phi**i)
    turtle.right(90)


### YOUR CODE ENDS HERE

turtle.exitonclick()
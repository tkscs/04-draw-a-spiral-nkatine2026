import turtle
from scipy.constants import golden as phi

"""
The aloe polyphylla plant grows in a pattern with five golden spirals
eminating from the same center. Make a function that draws a single golden
spiral, and use that to draw a shape like the aloe polyphylla.

You may find these functions useful:

turtle.up()

turtle.down()

turtle.setposition(x, y)

turtle.setheading(degrees)

The turtle starts at position(0, 0) with heading 0 degrees.
"""

### YOUR CODE STARTS HERE
turtle.speed(1000)
ial=0.1
for i in range(500):
    turtle.forward(ial*(phi**(i/90)))
    turtle.right(1)
turtle.setposition(0,100)
for i in range(500):
    turtle.forward(ial*(phi**(i/90)))
    turtle.right(1)
turtle.setposition(0,-100)
for i in range(500):
    turtle.forward(ial*(phi**(i/90)))
    turtle.right(1)
turtle.setposition(100,0)
for i in range(500):
    turtle.forward(ial*(phi**(i/90)))
    turtle.right(1)
turtle.setposition(-100,0)
for i in range(500):
    turtle.forward(ial*(phi**(i/90)))
    turtle.right(1)
### YOUR CODE ENDS HERE

turtle.exitonclick()
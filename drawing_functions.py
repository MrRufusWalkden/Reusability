import turtle
# Initialise
t = turtle.Turtle()
# Configurations
t.pensize(10)
t.speed(1)

# Functions
def create_square(length):
    for c in ['red', 'green', 'yellow', 'blue']:
        t.color(c)
        t.forward(length)
        t.left(90)

def create_circle(radius):
    t.circle(radius)


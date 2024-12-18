import turtle

def draw_star(size):
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    
    for i in range(5):
        turtle.color(colors[i % len(colors)])  # Cycle through colors
        turtle.begin_fill()  # Start filling the color
        turtle.forward(size)
        turtle.right(144)  # Angle to create a star
        turtle.forward(size)
        turtle.left(72)  # Angle to create the star points
        turtle.end_fill()  # End filling the color

# Set up the screen
turtle.bgcolor("white")  # Background color
turtle.speed(3)  # Speed of drawing

# Move the turtle to starting position
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()

# Draw the star
draw_star(100)

# Hide the turtle and finish
turtle.hideturtle()
turtle.done()
import turtle as t

screen = t.Screen()  # show the screen 
screen.bgcolor("white") # background colour

t.shape("arrow") # shape of cursor
t.speed(1)

"""t.forward(100) # move forward 100 pixel
t.left(120)

t.forward(100)
t.left(120)

t.forward(100)"""

# through loop
screen.bgcolor('yellow')
t.fillcolor('red')  # define colour
t.begin_fill()      # start colouring 

for _ in range(3):
    t.forward(200)
    t.left(120)
    

t.end_fill()        # end colouring
t.done()
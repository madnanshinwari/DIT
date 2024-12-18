import turtle as t

t.Screen()

t.shape("arrow")
t.speed(1)

t.fillcolor('yellow')
t.begin_fill()

for i in range(4):
    t.forward(200)
    t.right(90)



t.end_fill()

t.done()

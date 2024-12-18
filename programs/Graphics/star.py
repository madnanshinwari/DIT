import turtle as t 

t.Screen()

t.shape("arrow")
t.speed(1)

t.fillcolor("orange")
t.begin_fill()

for _ in range(5):
    t.forward(200)
    t.left(144)

t.end_fill()

t.done()
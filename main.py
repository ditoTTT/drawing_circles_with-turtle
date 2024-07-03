import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed('fastest')
tim.pensize(1)
tim.hideturtle()
x = -250
y = -250
while y < 250 and x < 250  :
    def draw_circles():
        global y
        global x
        R = random.randint(0, 255)
        G = random.randint(0, 255)
        B = random.randint(0, 255)
        tim.color((R, G, B))
        tim.penup()
        tim.goto(x,y)
        tim.pendown()
        tim.begin_fill()
        tim.fillcolor((R, G, B))
        tim.circle(10)
        tim.end_fill()
        x += 50
        if x == 250:
            y += 50
            x = -250
    draw_circles()

scree = t.Screen()
scree.exitonclick()


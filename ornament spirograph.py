import turtle
screen=turtle.Screen()

x=turtle.Turtle()
x.speed(40)
x.color("yellowgreen")


for i in range(400):
    x.circle(100)
    x.left(10)

x.hideturtle()

screen=turtle.screen()
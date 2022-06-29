# Test

import math
import turtle
from turtle import *
import random

# --- Game Setup --- #

wn = Screen()

ball = Turtle()
paddle1 = Turtle()
paddle2 = Turtle()

ball.shape("circle")
ball.penup()

paddle1.shape("square")
paddle1.setheading(90)
paddle1.turtlesize(0.5, 6.5)
paddle1.penup()

paddle2.shape("square")
paddle2.setheading(90)
paddle2.penup()
paddle2.turtlesize(0.5, 6.5)

paddle1.setpos(-wn.window_width() / 2.5, 0)
paddle2.setpos(wn.window_width() / 2.5, 0)

x_vel = random.randint(1, 10)
y_vel = random.randint(1, 10)

theta = (random.randint(-45, 45))
ball.seth(theta)

print(paddle1.shapesize())
# --- Game Loop --- #
gameRunning = True
while gameRunning:
    print(theta)
    if ball.xcor() > 0:
        if ball.ycor() > paddle2.ycor():
            paddle2.forward(4.3)
        elif ball.ycor() + 40 < paddle2.ycor():
            paddle2.backward(4.3)
    if ball.xcor() >= (wn.window_width() / 2.5) and ((ball.ycor() <= paddle2.ycor() + 60) and (ball.ycor() >= paddle2.ycor() - 60)):
        ball.seth(-90)
    if ball.ycor() > (wn.window_height() / 2) or ball.ycor() < -(wn.window_height() / 2):
        ball.seth(ball.heading() * -1)

    ball.forward(6)
    wn.update()

turtle.exitonclick()

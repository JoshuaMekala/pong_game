from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
from lines import Lines

import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()
lines = Lines()

screen.listen()
screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")
screen.onkeypress(l_paddle.go_up,"w")
screen.onkeypress(l_paddle.go_down,"s")

lines.drawlines()

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with right paddle
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 and ball.x_move > 0 or ball.xcor() < -320 and ball.distance(l_paddle) < 50 and ball.x_move < 0:
        ball.bounce_x()
    
    # detect right paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detect left paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()



















screen.exitonclick()
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
scoreboard=Scoreboard()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
# paddle = Turtle()
# paddle.shape("square")
# paddle.color("white")
# paddle.penup()
# paddle.shapesize(stretch_wid=5,stretch_len=1)
# paddle.goto(360,0)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:   #collision with wall
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:   #collision with paddle
        ball.bounce_x()
    if ball.xcor() > 380:   #r_paddle misses
        ball.reset_pos()
        scoreboard.l_point()
    if ball.xcor() < -380:   #l_paddle misses
        ball.reset_pos()
        scoreboard.r_point()



screen.exitonclick()

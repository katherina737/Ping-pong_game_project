from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)
screen.onkey(key="s", fun=l_paddle.go_down)


game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with wall and bounce:
    if ball.ycor() > 270 or ball.ycor() <-270:
        ball.bounce_y()

    #detect collision with paddle:
    if ball.distance(r_paddle)<50 and ball.xcor() > 320 or ball.distance(l_paddle)<50 and ball.xcor() < -320:
        ball.bouce_x()

    #detect R paddle misses:
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    #detect L paddle misses:
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
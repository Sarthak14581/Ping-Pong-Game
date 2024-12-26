import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.title(titlestring="Ping Pong Game")
screen.bgcolor("black")

ball = Ball()
scoreboard = Scoreboard()
screen.tracer(0)  # turns off the animation


right_paddle = Paddle(350,0)
left_paddle = Paddle(-350, 0)

screen.listen()
screen.onkeypress(key="Up", fun=right_paddle.move_up)
screen.onkeypress(key="Down", fun=right_paddle.move_down)
screen.onkeypress(key="w", fun=left_paddle.move_up)
screen.onkeypress(key="s", fun=left_paddle.move_down)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with right and left paddle
    if ball.xcor() > 320 and ball.distance(right_paddle) < 50 or ball.xcor() < -320 and ball.distance(left_paddle) < 50:
        ball.bounce_x()
        ball.increase_speed()

    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.left_side_scores()

    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.right_side_scores()


screen.exitonclick()

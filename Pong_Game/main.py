from turtle import Turtle,Screen
from Paddle import Paddle
from Ball import Ball
import time
from Scoreboard import Scoreboard
logo="""\______   \____   ____    ____    /  _____/_____    _____   ____  
 |     ___/  _ \ /    \  / ___\  /   \  ___\__  \  /     \_/ __ \ 
 |    |  (  <_> )   |  \/ /_/  > \    \_\  \/ __ \|  Y Y  \  ___/ 
 |____|   \____/|___|  /\___  /   \______  (____  /__|_|  /\___  >
                     \//_____/           \/     \/      \/     \/ """
screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")



game_is_on=True
print(logo)
while game_is_on:
    time.sleep(ball.speed_increase)
    screen.update()
    scoreboard.instruction()
    ball.move()
    #detect collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    #detect collision with wall
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()
    #right paddle miss
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()
        #left side's point
     #left paddle miss

    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()
        #right side's point

    if scoreboard.l_score==10 or scoreboard.r_score==10:
        if(scoreboard.l_score>scoreboard.r_score):
            scoreboard.game_over()
            print("Left player wins")
            game_is_on=False
        else:
            scoreboard.game_over()
            print("Right player wins")
            game_is_on=False


screen.exitonclick()












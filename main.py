from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

serpiente = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=serpiente.up)
screen.onkey(key="Down", fun=serpiente.down)
screen.onkey(key="Left", fun=serpiente.left)
screen.onkey(key="Right", fun=serpiente.right)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    serpiente.move()

    if serpiente.head.distance(food) < 15:
        food.refresh()
        serpiente.extend()
        scoreboard.increase_score()

    if serpiente.head.xcor() > 280 or serpiente.head.xcor() < -280 or serpiente.head.ycor() > 280 or serpiente.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    for segment in serpiente.segments[1:]:
        if serpiente.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()

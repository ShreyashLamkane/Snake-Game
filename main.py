from turtle import Screen, Turtle
from snake import Snake
import time
import food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake 🐍 Game")
screen.tracer(0)
screen.listen()

snake = Snake()
score = Scoreboard()
eat = food.Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    # detecting collision with food
    if snake.head.distance(eat) < 13:
        eat.refresh()
        score.upgrade()
        snake.extend()

    # Detecting collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        is_game_on = False
        score.game_over()

    # Detecting collision with snake body
    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            is_game_on = False
            score.game_over()

screen.exitonclick()

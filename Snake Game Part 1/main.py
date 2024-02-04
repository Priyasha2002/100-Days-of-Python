from turtle import Turtle , Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width = 600,height = 600)
screen.bgcolor("black")
screen.title("Snake Ninja")

screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Score()



screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

is_game_on=True
while is_game_on:                  #Move Snakes
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) <15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with walls
    if snake.head.xcor() > 280 or snake.head.xcor()< -280 or  snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        is_game_on = False
        scoreboard.game_over()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(height=600, width=800)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        scoreboard.new_score()
        snake.extend_snake()
        food.food_refresh()
    
    if snake.segments[0].xcor() > 400 or snake.segments[0].xcor() < -400 or snake.segments[0].ycor() > 300 or snake.segments[0].ycor() < -300:
        game_is_on = False
        scoreboard.game_over()
    
    for segment in snake.segments:
        if segment == snake.segments[0]:
            pass
        elif snake.segments[0].distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()




screen.exitonclick()
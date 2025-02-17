from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)


snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on=True

while game_on:
    screen.update()
    time.sleep(snake.moving_speed)
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow_bigger()
        scoreboard.keep_track()
        snake.speed_up()

    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() <-280 or snake.head.ycor() <-280 or snake.head.ycor() > 280:
        game_on=False
        scoreboard.game_over()

    #detect collision with tail
    for bit in snake.snake_body[1:]:
        if snake.head.distance(bit) < 10:
            game_on=False
            scoreboard.game_over()




screen.exitonclick()
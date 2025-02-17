from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head=self.snake_body[0]
        self.moving_speed=.4

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.grow(position)

    def grow(self, position):
        new_bit = Turtle("square")
        new_bit.color("green")
        new_bit.penup()
        new_bit.goto(position)
        self.snake_body.append(new_bit)

    def grow_bigger(self):
        self.grow(self.snake_body[-1].position())

    def move(self):
        for bit_num in range(len(self.snake_body) -1, 0, -1):
            new_x = self.snake_body[bit_num - 1].xcor()
            new_y = self.snake_body[bit_num - 1].ycor()
            self.snake_body[bit_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def speed_up(self):
        self.moving_speed *= .9


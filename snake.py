from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POSITION:
            self.add_segments(pos)

    def add_segments(self, positions):
        new_turtle = Turtle(shape="square")
        self.segments.append(new_turtle)
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(positions)

    def extend(self):
        self.add_segments(self.segments[-1].position())

    def move(self):
        for t in range(len(self.segments) - 1, 0, -1):
            new_xcor = self.segments[t - 1].xcor()
            new_ycor = self.segments[t - 1].ycor()
            self.segments[t].goto(new_xcor, new_ycor)
        self.segments[0].forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)

        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

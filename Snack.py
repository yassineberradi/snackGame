from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_POSITION = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snack:
    def __init__(self):
        self.new_segment = None
        self.segments = []
        self.create_snack()
        self.head = self.segments[0]

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.new_segment = new_segment
        self.segments.append(self.new_segment)

    def create_snack(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def move(self):
        for segment_iter in range(len(self.segments)-1, 0, -1):
            self.segments[segment_iter].goto(self.segments[segment_iter-1].pos())
        self.head = self.segments[0]
        self.head.forward(MOVE_POSITION)

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

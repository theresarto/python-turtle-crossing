from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.seth(90)
        self.total_distance = 0

    def up(self):
        if self.ycor() + MOVE_DISTANCE <= 270:
            self.forward(MOVE_DISTANCE)
        else:
            self.goto(self.xcor(), self.ycor())

    def down(self):
        if self.ycor() - MOVE_DISTANCE >= -270:
            self.backward(MOVE_DISTANCE)
        else:
            self.goto(self.xcor(), self.ycor())


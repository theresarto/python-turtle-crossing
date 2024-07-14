from turtle import Turtle
from random import choice, randint, random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.starting_x = 300
        self.list_of_cars = []
        self.total_distance = 0
        self.move_speed = STARTING_MOVE_DISTANCE
        self.probability = 0.25
        self.finish_line_distance = 1200

    def create_car(self):
        if random() < self.probability:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(choice(COLORS))
            new_car.starting_y = randint(-280, 280)
            new_car.goto(self.starting_x, new_car.starting_y)
            self.list_of_cars.append(new_car)
            self.total_distance = 0

    def move_cars(self):
        for car in self.list_of_cars:
            car.backward(self.move_speed)

    def at_finish_line(self):
        if len(self.list_of_cars) == 0:
            return False
        self.total_distance = self.starting_x - self.list_of_cars[0].xcor()
        if self.total_distance == self.finish_line_distance:
            return True

    def collision(self, player_position):
        for car in self.list_of_cars:
            if car.distance(player_position) < 20:
                return True

    def reset_cars(self):
        for car in self.list_of_cars:
            car.clear()
            car.ht()
        self.list_of_cars = []
        self.total_distance = 0
        self.probability *= 1.1
        self.finish_line_distance *= 1.5
        self.create_car()
        self.move_speed += MOVE_INCREMENT
        self.move_cars()

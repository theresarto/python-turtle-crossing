import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()



screen.onkeypress(fun=player.up, key="Up")
screen.onkeypress(fun=player.down, key="Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    if car_manager.at_finish_line():
        car_manager.reset_cars()
        player.goto(0,0)
        scoreboard.update_score()
    elif car_manager.collision(player):
        game_is_on = False
        scoreboard.game_over()




screen.exitonclick()

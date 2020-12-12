from turtle import Screen
import time
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)

car_manager = CarManager()
player = Player()
score = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

loop_num = 0
game_on = True
while game_on:
    # Updates the screen and manages the speed
    time.sleep(0.05)
    screen.update()

    # Displays the score board
    score.display()

    car_manager.create_car()

    # Moves the cars on the screen
    car_manager.move_car()

    # Detects when the player has made it to the finish line
    if player.ycor() > 280:
        player.reset_player()
        score.level_up()
        car_manager.level_up()

    # Checks if the player has collided with the car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_on = False
            score.game_over()










screen.exitonclick()
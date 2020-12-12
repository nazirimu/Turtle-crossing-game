from turtle import Turtle
import random

COLORS = ["red", "purple", "yellow", "blue", "green"]
X_START = 300
START_MOVE_DISTANCE = 10

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_speed = START_MOVE_DISTANCE

    def create_car(self):
        random_number = random.randint(1,4)
        if random_number == 1:
            car = Turtle("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.goto(X_START, random.randint(-230, 250))
            self.all_cars.append(car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.move_speed)

        # Alternate way:
        # for car_num in range(len(self.cars_list)-1):
        #     new_x = self.cars_list[car_num].xcor() - 10
        #     self.cars_list[car_num].goto(new_x, self.cars_list[car_num].ycor())

    def level_up(self):
        self.move_speed += 5








from turtle import Turtle
MOVE_DISTANCE = 20
STARTING_POSITION = (0,-270)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    # Moves the player up when the up key is pressed
    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0, new_y)

    # Resets the player back to the starting position when they reach the end
    def reset_player(self):
        self.goto(STARTING_POSITION)


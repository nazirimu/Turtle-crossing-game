from turtle import Turtle
ALIGNMENT = "left"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.setposition(-280, 275)

    # Displays the level that the player is on
    def display(self):
        self.clear()
        self.write(f"Level: {self.level}", False, align=ALIGNMENT, font=FONT)

    # Increases the players level when they cross the finishing line
    def level_up(self):
        self.level += 1
        self.display()

    # Displays a game over message
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game over", False, align=ALIGNMENT, font=FONT)


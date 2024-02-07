FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 200)
        self.write(f"LEVEL:{self.level}", align="center", font=(FONT))

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def collide_car(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=(FONT))

from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(0, 280)
        self.color("white")
        self.show()

    def show(self):
        self.write(f"Score: {self.score}", move=False, align="center", font=("arial", 10, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", move=False, align="center", font=("arial", 13, "normal"))

    def upgrade(self):
        self.score += 1
        self.clear()
        self.show()

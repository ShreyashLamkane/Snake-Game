from turtle import Turtle


# file = open("highscore.txt", mode="r+")
# highscore = file.read()
# highscore = int(highscore)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("highscore.txt", mode="r") as file:
            high = file.read()
            self.highscore = int(high)
        self.score = 0

        self.hideturtle()
        self.goto(0, 280)
        self.color("white")
        self.show()

    def show(self):
        self.clear()
        self.write(f"Score: {self.score}    Highscore: {self.highscore}", move=False, align="center",
                   font=("arial", 10, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.show()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game Over!", move=False, align="center", font=("arial", 13, "normal"))

    def upgrade(self):
        self.score += 1

        self.show()




from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.pencolor("white")
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def inc_score(self):
        self.score += 1
        self.clear()
        self.pendown()
        self.update_scoreboard()
        self.penup()

    def update_scoreboard(self):
        self.write(arg=f"Your score is: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
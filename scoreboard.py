from turtle import Turtle
FONT = ("Courier", 13, "normal")
ALIGMENT = "center"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", align=ALIGMENT, font=FONT)


    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", align=ALIGMENT,font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

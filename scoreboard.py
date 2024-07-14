from turtle import Turtle

REG_FONT = ("Courier", 24, "normal")
LARGE_FONT = ("Courier", 48, "bold")
ALIGN = "Left"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.ht()
        self.goto(-280, 260)
        self.color("black")
        self.speed("fastest")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", align=ALIGN, font=REG_FONT)

    def update_score(self):
        self.clear()
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER.", align="Center", font=LARGE_FONT)

    # def get_ready(self):
    #     self.goto(0, 0)
    #     self.write("Get ready for the next level", align="Center", font=LARGE_FONT)

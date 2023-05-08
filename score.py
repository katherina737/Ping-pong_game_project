from turtle import Turtle
ALINGMENT = "center"

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_points = 0
        self.r_points = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100,200)
        self.write(f"{self.l_points}", move=False, align=ALINGMENT, font=(("Courier",80,"normal")))
        self.goto(100, 200)
        self.write(f"{self.r_points}", move=False, align=ALINGMENT, font=(("Courier",80,"normal")))

    def l_point(self):
        self.l_points += 1
        self.update_score()

    def r_point(self):
        self.r_points += 1
        self.update_score()
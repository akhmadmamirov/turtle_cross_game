from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        self.level = 1
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.draw_score()
    
    def draw_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align= "left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.draw_score()
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER" , align= "center", font=FONT)
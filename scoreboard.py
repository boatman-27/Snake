from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        with open ("Day_20/data.txt") as data:
            self.highscore = int(data.read())
        self.update_score()
    
    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score {self.highscore}", align = "center", font = ("Courier", 24, "normal"))

    def reset(self):
        if self.score > self.highscore:
            with open("Day_20/data.txt", "w") as data:
                data.write(str(self.score))
                self.highscore = self.score
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align = "center", font = ("Courier", 24, "normal"))
        
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "italic")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-5, 260)
        with open("data.txt") as file:
            file.seek(12, 0)
            self.high_score = int(file.read())
        self.update()

    def increase_score(self):
        self.score += 1

    def update(self):
        self.clear()
        self.write(arg=f"Score : {self.score} High Score : {self.high_score}",
                   move=False,
                   align=ALIGNMENT,
                   font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.seek(12, 0)
                file.write(f"{self.high_score}")
        self.score = 0
        self.update()
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

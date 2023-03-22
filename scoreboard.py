from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")

# creation of scoreboard class, again usage of super().__init__() to inherit methods from Turtle.
class Scoreboard(Turtle):
     
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,265)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  ", align=ALIGNMENT, font=FONT)   

    
    # clearing the score so that the numbers don't stack up on each other
    def increase_score(self):
        
        self.score += 1
        self.update_score()
    
    def game_over(self):
        self.goto(0, 0)   
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)
        
    





      
from turtle import Turtle
import random


# creation of food class, use super().__init__() to inherit the methods of Turtle.
class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len= 0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.new_position()


    def new_position(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x, random_y)

        


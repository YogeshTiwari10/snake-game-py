import random
from turtle import Turtle

class Food (Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.75, stretch_len=0.75)
        self.color("CadetBlue")
        self.speed("fastest")
        self.food_refresh()
        

    def food_refresh(self):
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        self.goto(x,y)

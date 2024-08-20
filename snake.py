from turtle import Turtle

STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
    
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
            
    
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("LightCoral")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    
    def extend_snake(self):
        self.add_segment(self.segments[-1].position())
    
    def move(self):
            for seg in range(len(self.segments)-1, 0, -1):
                new_x = self.segments[seg-1].xcor()
                new_y = self.segments[seg-1].ycor()
                self.segments[seg].goto(new_x,new_y)
            self.segments[0].forward(MOVE_DISTANCE)
    
    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
    
    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
        
    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
        
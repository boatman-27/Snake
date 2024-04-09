from turtle import Turtle
STARTING_POSTIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSTIONS:
            self.add_segment(position)
            
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)

    def up(self):
        self.head.setheading(90)
        
    def left(self):
        self.head.setheading(180)
       
    def right(self):
        self.head.setheading(0)

    def down(self):
        self.head.setheading(270)

    def add_segment(self, position):
        body = Turtle("square")
        body.color("white")
        body.penup()
        body.goto(position)
        self.segments.append(body)

    def extend(self):
        self.add_segment(self.segments[-1].position())
    
    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

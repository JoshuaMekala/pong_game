from turtle import Turtle
class Lines(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.goto(0,300)
        self.pensize(10)
        self.color("white")
    
    def drawlines(self):
        for i in range(20):
            self.pendown()
            self.setheading(270)
            self.forward(20)
            self.penup()
            new_y = self.ycor() - 20
            self.goto(0,new_y)


#Header
#Jackie Cywinski
#9/10/2024
#Line Drawing

#Initialize
import turtle
jackie=turtle.Turtle()

import turtle
jasmine=turtle.Turtle()


#Functions

#draws the triangular body of the frog
#coded by Jackie
def body():
    jackie.color("#39ac73")
    jackie.begin_fill()
    for i in range(3):
        jackie.forward(200)
        jackie.right(120)
    jackie.end_fill()

    jackie.pencolor("black")
    for i in range(3):
        jackie.forward(200)
        jackie.right(120)

#draws the frog's smile
#coded by Jackie
def smile():
    jackie.forward(50)
    jackie.right(90)
    jackie.penup()
    jackie.forward(25)
    jackie.pendown()
    jackie.circle(50,180)

#draw's the frogs rectangular front feet
#coded by Jackie
def frontFeet():
    jackie.color("#39ac73")
    jackie.begin_fill()
    jackie.right(180)
    jackie.forward(70)
    jackie.right(90)
    jackie.forward(10)
    jackie.left(90)
    jackie.forward(10)
    jackie.left(90)
    jackie.forward(38)
    jackie.left(90)
    jackie.forward(10)
    jackie.left(90)
    jackie.forward(10)
    jackie.right(90)
    jackie.forward(70)
    jackie.end_fill()

#draws the frogs spikey right foot
#coded by Jackie
def rightFoot():
    jackie.penup()
    jackie.goto(109,-160)
    jackie.pendown()
    jackie.right(90)
    jackie.color("#206040")
    jackie.begin_fill()
    jackie.forward(150)
    jackie.right(15)
    jackie.forward(15)
    jackie.right(130)
    jackie.forward(15)
    for i in range(2):
        jackie.left(130)
        jackie.forward(15)
        jackie.right(130)
        jackie.forward(15)
    jackie.right(45)
    jackie.forward(165)
    jackie.end_fill()

#draws the frogs spikey left foot
#coded by Jackie
def leftFoot():
    jackie.penup()
    jackie.goto(91,-160)
    jackie.pendown()
    jackie.left(10)
    jackie.color("#206040")
    jackie.begin_fill()
    jackie.forward(150)
    jackie.left(15)
    jackie.forward(15)
    jackie.left(130)
    jackie.forward(15)
    for i in range(2):
        jackie.right(130)
        jackie.forward(15)
        jackie.left(130)
        jackie.forward(15)
    jackie.left(45)
    jackie.forward(165)
    jackie.end_fill()

#draws the two eyes of the frog
#coded by Jasmine
def eye():
    jasmine.penup()
    jasmine.goto(40,0)
    jasmine.pendown()
    jasmine.circle(50,360)
    jasmine.penup()
    jasmine.goto(30,70)
    jasmine.pendown()
    jasmine.dot(20,"black")
    jasmine.penup()
    jasmine.goto(160,0)
    jasmine.pendown()
    jasmine.circle(50,360)
    jasmine.penup()
    jasmine.goto(160,30)
    jasmine.pendown()
    jasmine.dot(20,"black")

#turns the turtle around
#coded by Jasmine
def turnaround():
    jasmine.left(180)

#draws the thighs of the frog
#coded by Jasmine
def thighs():
    jasmine.color("#339966")
    jasmine.begin_fill()
    jasmine.penup()
    jasmine.goto(100,-171)
    jasmine.pendown()
    jasmine.right(30)
    jasmine.circle(100,120)
    jasmine.left(60)
    jasmine.circle(100,120)
    jasmine.end_fill()
    jasmine.color("black")
    jasmine.begin_fill()
    jasmine.left(120)
    jasmine.forward(90)
    turnaround()
    jasmine.forward(90)
    jasmine.end_fill()
    jasmine.color("#339966")
    jasmine.begin_fill()
    jasmine.right(120)
    jasmine.circle(100,120)
    jasmine.left(60)
    jasmine.circle(100,120)
    jasmine.end_fill()
    jasmine.color("black")
    jasmine.begin_fill()
    jasmine.left(120)
    jasmine.forward(90)
    jasmine.end_fill()
    
#draws the entire frog
    #coded by Jackie and Jasmine
def drawScene():
    eye()
    body()
    smile()
    thighs()
    rightFoot()
    leftFoot()
    jackie.penup()
    jackie.goto(115,-100)
    jackie.setheading(90)
    jackie.pendown()
    frontFeet()
    jackie.penup()
    jackie.goto(70,-100)
    jackie.setheading(90)
    jackie.pendown()
    frontFeet()
    
    
#Main
drawScene()

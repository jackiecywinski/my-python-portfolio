#Jackie Cywinski
#2/23/2024

#Initialize
#This code draws an underwater scene

import turtle
jackie=turtle.Turtle()
import turtle
grace=turtle.Turtle()
import random
jackie.speed(20)
grace.speed(20)

#Functions
def draw_fish(size, color,x,y): #draws the fish
    jackie.penup()
    jackie.goto(x,y)
    jackie.pendown()
    jackie.dot(size,color)
    jackie.penup()
    jackie.forward(10)
    jackie.pendown
    jackie.seth(330)
    jackie.color(color)
    jackie.begin_fill()
    for i in range(3):
        jackie.forward(size)
        jackie.left(120)
    jackie.end_fill()

def draw_seaweed(): #draws the seaweed
    jackie.seth(0)
    jackie.penup()
    jackie.goto(-125,-350)
    jackie.pendown()
    jackie.pensize(10)
    for i in range(5):
        jackie.circle(20,180)
        jackie.left(180)
        jackie.circle(20,-180)
        jackie.left(180)
    jackie.penup()
    jackie.goto(-50,-350)
    jackie.pendown()
    for i in range(3):
        jackie.circle(20,180)
        jackie.left(180)
        jackie.circle(20,-180)
        jackie.left(180)
        
def drawSeaUrchin(size,color,x,y): #draws the sea urchins
    grace.penup()
    grace.goto(x,y)
    grace.pendown()
    grace.color(color)
    grace.begin_fill()
    for i in range(36):
        grace.forward(size)
        grace.left(170)
    grace.end_fill()

def draw_all_element(): #draws the full scene
    draw_fish(100,"#fadbd8",100,50)
    draw_fish(50,"#e8daef", -200,-60)
    draw_fish(70,"#d0ece7",0,-120)
    draw_fish(40,"#d4e6f1",400,0)
    for i in range(4):
        drawSeaUrchin(40,"#ffb3ff",random.randint(-500,500),random.randint(-500,50))
        drawSeaUrchin(60,"#ffcc99",random.randint(-500,500),random.randint(-500,50))
        drawSeaUrchin(70,"#eb99ff",random.randint(-500,500),random.randint(-500,50))
    draw_seaweed()

#Main
draw_all_element()

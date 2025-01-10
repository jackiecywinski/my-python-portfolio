#initialize
import turtle 
jackie = turtle.Turtle()
jasmine = turtle.Turtle()
grace = turtle.Turtle()

jasmine.speed(0)
jackie.speed(0)
grace.speed(0)

#functions
def background():
     jackie.dot(5000, "#d4e2f7")

# parameters for dot
def draw_dot(size, color, x, y):
    jackie.penup()
    jackie.goto(x,y)
    jackie.pendown()
    jackie.dot(size, color)

def draw_pinkbackground():
      jackie.penup()
      jackie.goto(-60,0)
      jackie.pendown()
      jackie.color("pink")
      jackie.begin_fill()

      for i in range(2):
          jackie.forward(121)
          jackie.right(90)
          jackie.forward(1000)
          jackie.right(90)

      jackie.end_fill()

#draws blossom eyes and face
def draw_eyesAndFace():
    jackie.penup()
    jackie.left(90)
    jackie.forward(50)
    jackie.pendown()
    draw_dot(200,"#ffd9b3",0,60)
    draw_dot(90,"white",60,60)
    draw_dot(70,"pink",45,60)
    draw_dot(60,"black",42,60)
    draw_dot(20,"white",30,60)
    draw_dot(90,"white",-60,60)
    draw_dot(70,"pink",-45,60)
    draw_dot(60,"black",-42,60)
    draw_dot(20,"white",-30,60)

#draws blossom smile
def draw_blossomsmile():
    jackie.penup()
    jackie.goto(-2,15)
    jackie.right(90)
    jackie.pendown()
    jackie.color("black")
    jackie.width(3)
    jackie.circle(5,180)

#draws blossom bangs
def draw_bangs():
    jackie.penup()
    jackie.goto(-87,110)
    jackie.right(30)
    jackie.pendown()
    jackie.color("orange")
    jackie.begin_fill()
    jackie.circle(-100,125)
    jackie.right(115)
    jackie.forward(184)
    jackie.end_fill()
    jackie.penup()
    jackie.goto(0,95)
    jackie.pendown()
    jackie.color("#ffd9b3")
    jackie.begin_fill()
    for i in range(3):
        jackie.forward(20)
        jackie.right(120)
    jackie.end_fill()
    jackie.penup()
    jackie.goto(20,95)
    jackie.pendown()
    jackie.color("#ffd9b3")
    jackie.begin_fill()
    for i in range(3):
        jackie.forward(10)
        jackie.right(120)
    jackie.end_fill()

#draws blossom hair
def draw_hair():
    jackie.penup()
    jackie.goto(-60,20)
    jackie.pendown()
    jackie.color("orange")
    jackie.begin_fill()
    jackie.seth(-90)
    for i in range(4):
        jackie.forward(120)
        jackie.left(90)
    jackie.end_fill()
    jackie.penup()
    jackie.goto(-80,-90)
    jackie.seth(-45)
    jackie.pendown()
    jackie.color("orange")
    jackie.begin_fill()
    jackie.circle(110,90)
    jackie.seth(180)
    jackie.forward(155)
    jackie.end_fill()

#draws blossom bow
def draw_bow():
    jackie.penup()
    jackie.goto(4,160)
    jackie.pendown()
    jackie.color("pink")
    jackie.dot(30)
    jackie.penup()
    jackie.goto(-35,100)
    jackie.seth(45)
    jackie.pendown()
    jackie.color("pink")
    jackie.begin_fill()
    jackie.circle(100,100)
    jackie.left(90)
    jackie.circle(100,100)
    jackie.end_fill()
    jackie.goto(10,110)
    jackie.seth(20)
    jackie.pendown()
    jackie.color("pink")
    jackie.begin_fill()
    jackie.circle(100,100)
    jackie.left(90)
    jackie.circle(100,100)
    jackie.end_fill()

#draws blossom body
def body():
    jackie.penup()
    jackie.goto(-30,-20)
    jackie.seth(-90)
    jackie.color("pink")
    jackie.begin_fill()
    for i in range(4):
        jackie.forward(60)
        jackie.left(90)
    jackie.end_fill()
    jackie.penup()
    jackie.goto(-30,-50)
    jackie.seth(0)
    jackie.pendown()
    jackie.color("black")
    jackie.begin_fill()
    for i in range(2):
        jackie.forward(60)
        jackie.right(90)
        jackie.forward(20)
        jackie.right(90)
    jackie.end_fill()

# draws blossom legs
def legs():
    jackie.penup()
    jackie.goto(15,-80)
    jackie.pendown()
    jackie.color("white")
    jackie.dot(30)
    jackie.goto(0,-80)
    jackie.color("black")
    jackie.begin_fill()
    jackie.seth(270)
    jackie.circle(15,180)
    jackie.end_fill()
    
    jackie.penup()
    jackie.goto(-30,-80)
    jackie.pendown()
    jackie.seth(270)
    jackie.color("white")
    jackie.begin_fill()
    for i in range(4):
        jackie.forward(25)
        jackie.left(90)
    jackie.end_fill()
    jackie.penup()
    jackie.goto(-17.5,-105)
    jackie.dot(30)
    jackie.goto(-32,-105)
    jackie.color("black")
    jackie.begin_fill()
    jackie.seth(270)
    jackie.circle(15,180)
    jackie.end_fill()

#draws blossom arms
def arms():
    jackie.penup()
    jackie.goto(-50,-26)
    jackie.seth(225)
    jackie.pendown()
    jackie.color("#ffd9b3")
    jackie.width(20)
    jackie.forward(30)
    jackie.penup()
    jackie.goto(50,-26)
    jackie.seth(-45)
    jackie.pendown()
    jackie.color("#ffd9b3")
    jackie.width(20)
    jackie.forward(30)


def draw_greenbackground():
      jasmine.penup()
      jasmine.goto(235,0)
      jasmine.pendown()
      jasmine.color("#c6ecc6")
      jasmine.begin_fill()

      for i in range(2):
          jasmine.forward(125)
          jasmine.right(90)
          jasmine.forward(1000)
          jasmine.right(90)

      jasmine.end_fill()

#draws buttercup face
def draw_buttercupsface():
    jasmine.penup()
    jasmine.goto(300,0)
    jasmine.pendown()
    jasmine.dot(200.1,"#ffd9b3")


#draws buttercup hair
def draw_buttercupshair():
    jasmine.penup()
    jasmine.home()
    jasmine.goto(394,-30)
    jasmine.pendown()
    jasmine.color("black")
    jasmine.begin_fill()
    jasmine.left(20)
    jasmine.circle(70,100)
    
    jasmine.left(70)
    jasmine.forward(60)
    jasmine.right(5)
    jasmine.forward(60)
    jasmine.right(75)
    jasmine.forward(25)
    jasmine.left(145)
    jasmine.forward(25)
    
    jasmine.right(80)
    jasmine.forward(80)
    jasmine.right(5)
    jasmine.forward(38)
    jasmine.left(65)
    jasmine.circle(70,100)
    jasmine.left(-35)
    jasmine.circle(70,-56)
    jasmine.left(9)
    jasmine.circle(100,-179.7)
    jasmine.end_fill()

    
    jasmine.penup()
    jasmine.home()
    jasmine.goto(330,90)
    jasmine.left(90)
    jasmine.pendown()
    jasmine.color("black")
    jasmine.begin_fill()
    jasmine.forward(18)
    jasmine.right(150)
    jasmine.forward(13)
    jasmine.left(140)
    jasmine.forward(20)
    jasmine.right(165)
    jasmine.forward(10)
    jasmine.right(5)
    jasmine.forward(14)
    jasmine.end_fill()
    jasmine.penup()


#draws the parameter of the eyes
def draw_buttercupseye(size,color,x,y):
    jasmine.penup()
    jasmine.goto(x,y)
    jasmine.dot(size,color)

#draws the eyeballs
def draw_buttercupseyeballs():
    draw_buttercupseye(95,"white",235,15)
    draw_buttercupseye(77,"lightgreen",245,17)
    draw_buttercupseye(64,"black",252,19)
    draw_buttercupseye(25,"white",262,25)

    draw_buttercupseye(95,"white",365,15)
    draw_buttercupseye(77,"lightgreen",365,15)
    draw_buttercupseye(64,"black",348,19)
    draw_buttercupseye(25,"white",338,25)


#draws the bangs
def draw_buttercupsbangs():
    jasmine.penup()
    jasmine.home()
    jasmine.goto(405,60)
    jasmine.pendown()
    jasmine.color("black")
    jasmine.begin_fill()
    jasmine.left(190)
    jasmine.forward(40)
    jasmine.right(5)
    jasmine.forward(60)
    jasmine.right(75)
    jasmine.forward(25)
    jasmine.left(145)
    jasmine.forward(25)
    jasmine.right(80)
    jasmine.forward(85)
    jasmine.right(120)
    jasmine.circle(-100,100)
    jasmine.end_fill()

    
#draws angry eyebrows
def draw_eyebrows():
    jasmine.penup()
    jasmine.home()
    jasmine.goto(285,35)
    jasmine.pendown()
    jasmine.color("#ffd9b3")
    jasmine.begin_fill()
    jasmine.left(160)

    for i in range(3):
        jasmine.forward(50)
        jasmine.right(120)

    jasmine.end_fill()

    jasmine.penup()
    jasmine.home()
    jasmine.goto(366,51)
    jasmine.pendown()
    jasmine.color("#ffd9b3")
    jasmine.begin_fill()
    jasmine.right(160)

    for i in range(3):
        jasmine.forward(50)
        jasmine.right(120)

    jasmine.end_fill()


    jasmine.pencolor("black")
    jasmine.penup()
    jasmine.home()
    jasmine.goto(279,36)
    jasmine.pendown()
    jasmine.right(20)
    jasmine.forward(5)
    jasmine.left(135)
    jasmine.forward(7)

    jasmine.penup()
    jasmine.home()
    jasmine.goto(313,32)
    jasmine.pendown()
    jasmine.left(15)
    jasmine.forward(5)
    jasmine.left(180)
    jasmine.forward(5)
    jasmine.right(135)
    jasmine.forward(7)

#draws buttercup smile
def draw_buttercupsmile():
    jasmine.penup()
    jasmine.home()
    jasmine.goto(290,-50)
    jasmine.width(2)
    jasmine.pendown()
    jasmine.left(270)
    jasmine.circle(10,180)

#draws buttercup body
def draw_buttercupsbody():
    jasmine.penup()
    jasmine.home()
    jasmine.goto(270,-85)
    jasmine.pendown()
    jasmine.color("lightgreen")
    jasmine.begin_fill()
    
    for i in range(4):
        jasmine.forward(60)
        jasmine.right(90)

    jasmine.end_fill()

    jasmine.penup()
    jasmine.goto(270,-110)
    jasmine.pendown()
    jasmine.color("black")
    jasmine.begin_fill()

    for i in range(2):
        jasmine.forward(60)
        jasmine.right(90)
        jasmine.forward(20)
        jasmine.right(90)
        
    jasmine.end_fill()


    jasmine.penup()
    jasmine.goto(270,-85)
    jasmine.pencolor("black")
    jasmine.pendown()

    
    for i in range(4):
        jasmine.forward(60)
        jasmine.right(90)



    

#leg1 1
def draw_buttercupslegs():
    jasmine.penup()
    jasmine.home()
    jasmine.goto(270,-145)
    jasmine.color("white")
    jasmine.begin_fill()
    jasmine.pendown()
    jasmine.width(1)

    for i in range(2):
        jasmine.forward(30)
        jasmine.right(90)
        jasmine.forward(40)
        jasmine.right(90)

    jasmine.end_fill()

    jasmine.penup()
    jasmine.home()
    jasmine.goto(270,-145)
    jasmine.pencolor("black")
    jasmine.pendown()
    jasmine.width(1)

    for i in range(2):
        jasmine.forward(30)
        jasmine.right(90)
        jasmine.forward(40)
        jasmine.right(90)
    
                     
    jasmine.penup()
    jasmine.goto(270,-175)
    jasmine.pendown()
    jasmine.color("black")
    jasmine.begin_fill()
    jasmine.forward(30)
    jasmine.right(90)
    jasmine.forward(10)
    jasmine.circle(-15,180)
    jasmine.forward(10)
    jasmine.end_fill()


    jasmine.penup()
    jasmine.goto(280,-185)
    jasmine.pendown()
    jasmine.color("white")
    jasmine.begin_fill()
    jasmine.right(90)
    jasmine.forward(10)
    jasmine.right(90)
    jasmine.circle(-5,180)
    jasmine.end_fill()


#outline for leg 2
    jasmine.penup()
    jasmine.home()
    jasmine.left(90)
    jasmine.goto(300,-150)
    jasmine.pendown()
    jasmine.color("white")
    jasmine.begin_fill()
    jasmine.circle(-15,180)
    jasmine.forward(5)
    jasmine.right(90)
    jasmine.forward(30)
    jasmine.right(90)
    jasmine.forward(5)
    jasmine.end_fill()

    jasmine.penup()
    jasmine.home()
    jasmine.goto(300,-150)
    jasmine.left(90)
    jasmine.pendown()
    jasmine.pencolor("black")
    jasmine.circle(-15,180)
    jasmine.forward(5)
    jasmine.right(90)
    jasmine.forward(30)
    jasmine.right(90)
    jasmine.forward(5)
    
    jasmine.penup()
    jasmine.left(180)
    jasmine.forward(5)
    jasmine.pendown()
    jasmine.color("black")
    jasmine.begin_fill()
    jasmine.left(90)
    jasmine.forward(30)
    jasmine.right(90)
    jasmine.forward(10)
    jasmine.circle(-15,180)
    jasmine.forward(10)
    jasmine.end_fill()

    jasmine.penup()
    jasmine.goto(310,-165)
    jasmine.pendown()
    jasmine.color("white")
    jasmine.begin_fill()
    jasmine.right(90)
    jasmine.forward(10)
    jasmine.right(90)
    jasmine.circle(-5,180)
    jasmine.end_fill()


#draws arms
def draw_buttercupsarms():
#arm 1(left)
    jasmine.penup()
    jasmine.home()
    jasmine.goto(228,-70)
    jasmine.pendown()
    jasmine.width(1)
    jasmine.color("#ffd9b3")
    jasmine.begin_fill()
    jasmine.left(205)
    jasmine.circle(35,30)
    jasmine.right(60)
    jasmine.circle(-5,110)
    jasmine.left(5)
    jasmine.circle(-20,75)
    jasmine.end_fill()

#arm 2(right)
    jasmine.penup()
    jasmine.home()
    jasmine.goto(372,-69)
    jasmine.pendown()
    jasmine.color("#ffd9b3")
    jasmine.begin_fill()
    jasmine.right(190)
    jasmine.circle(35,-30)
    jasmine.left(60)
    jasmine.circle(-5,-110)
    jasmine.right(5)
    jasmine.circle(-20,-75)
    jasmine.end_fill()
    

#draws buttercup
def draw_buttercup():
    draw_greenbackground()
    draw_buttercupsbody()   
    draw_buttercupsface()
    draw_buttercupshair()
    draw_buttercupseyeballs()
    draw_eyebrows()
    draw_buttercupsbangs()
    draw_buttercupsmile()
    draw_buttercupslegs()
    draw_buttercupsarms() 
    jasmine.hideturtle()

#draws blossom
def draw_blossom():
    draw_pinkbackground()
    draw_hair()
    body()
    jackie.pendown()
    draw_eyesAndFace()
    draw_bow()
    jackie.seth(0)
    draw_blossomsmile()
    draw_bangs()
    legs()
    arms()
    jackie.hideturtle()


#functions


def drawHead():
    grace.penup()
    grace.goto(-300,0)
    grace.dot(200,"#ffd9b3")


def drawFace():
    grace.penup()
    grace.goto(-250,0)
    grace.pendown()
    grace.dot(90,'white')
    grace.goto(-260,5)
    grace.dot(70,'#b3e0ff')
    grace.penup()
    grace.goto(-265,5)
    grace.pendown()
    grace.dot(59,'black')
    grace.penup()
    grace.goto(-350,0)
    grace.pendown()
    grace.dot(90,'white')
    grace.goto(-340,5)
    grace.dot(70,'#b3e0ff')
    grace.goto(-335,5)
    grace.dot(59,'black')

def drawEyes(size,color,x,y):
    grace.penup()
    grace.goto(x,y)
    grace.pendown()
    grace.dot(size,color)
    
def drawFace():
    drawHead()
    drawEyes(90,'white',-250,0)
    drawEyes(70,'#b3e0ff',-260,5)
    drawEyes(59,'black',-265,5)
    drawEyes(18,'white',-275,5)
    drawEyes(90,'white',-350,0)
    drawEyes(70,'#b3e0ff',-340,5)
    drawEyes(59,'black',-335,5)
    drawEyes(18,'white',-325,5)
    grace.penup()
    grace.goto(-290,-60)
    grace.pendown()
    grace.left(90)
    grace.width(3)
    grace.circle(10,-180)
    grace.width(1)
    



def drawHair():
    grace.penup()
    grace.goto(-214,50)
    grace.fillcolor('#ffd11a')
    grace.begin_fill()
    grace.right(40)
    grace.pendown()
    grace.circle(-50,110)               #(x,y) x=the circle size y=how much of the circle it draws
    grace.left(110)
    grace.circle(-50,110)
    grace.right(75)
    grace.circle(-120,45)
    grace.right(9)
    grace.circle(-120,49)
    grace.end_fill()
    grace.left(10)
    grace.begin_fill()
    grace.circle(60,130)
    grace.left(130)
    grace.circle(-50,50)
    grace.right(20)
    grace.forward(40)
    grace.circle(60,90)
    grace.end_fill()
    grace.left(70)
    grace.fillcolor('#b3e0ff')
    grace.begin_fill()
    grace.circle(170,20)
    grace.circle(10,180)
    grace.circle(-170,20)
    grace.circle(10,180)
    grace.end_fill()
    grace.fillcolor('#ffd11a')
    grace.penup()
    grace.goto(-385,50)
    grace.pendown()
    grace.right(80)
    grace.begin_fill()
    grace.circle(-60,130)
    grace.right(130)
    grace.circle(50, 50)
    grace.left(20)
    grace.forward(40)
    grace.circle(-60,90)
    grace.end_fill()
    grace.right(70)
    grace.fillcolor('#b3e0ff')
    grace.begin_fill()
    grace.circle(-170,20)
    grace.circle(-10,180)
    grace.circle(170,20)
    grace.circle(-10,180)
    grace.end_fill()
    
def drawLine():
    grace.penup()
    grace.goto(-360,0)
    grace.pendown()
    grace.color("#b3e0ff")
    grace.begin_fill()
    for i in range(2):
          grace.forward(125)
          grace.right(90)
          grace.forward(1000)
          grace.right(90)
    grace.end_fill()
    grace.color("black")
    
    
def drawBubblesBody():
    jasmine.penup()
    jasmine.home()
    jasmine.goto(-325,-95)
    jasmine.pendown()
    jasmine.color("#b3e0ff")
    jasmine.begin_fill()
    
    for i in range(4):
        jasmine.forward(60)
        jasmine.right(90)

    jasmine.end_fill()

    jasmine.penup()
    jasmine.goto(-325,-115)
    jasmine.pendown()
    jasmine.color("black")
    jasmine.begin_fill()

    for i in range(2):
        jasmine.forward(60)
        jasmine.right(90)
        jasmine.forward(20)
        jasmine.right(90)
        
    jasmine.end_fill()


    jasmine.penup()
    jasmine.goto(-325,-95)
    jasmine.pencolor("black")
    jasmine.pendown()

    
    for i in range(4):
        jasmine.forward(60)
        jasmine.right(90)
        
def bubblesArms():
    jackie.penup()
    jackie.goto(-350,-70)
    jackie.seth(225)
    jackie.pendown()
    jackie.color("#ffd9b3")
    jackie.width(20)
    jackie.forward(30)
    jackie.penup()
    jackie.goto(-250,-70)
    jackie.seth(-45)
    jackie.pendown()
    jackie.color("#ffd9b3")
    jackie.width(20)
    jackie.forward(30)


def drawBubblesLegs():
    jasmine.penup()
    jasmine.home()
    jasmine.goto(-295,-145)
    jasmine.color("white")
    jasmine.begin_fill()
    jasmine.pendown()
    jasmine.width(1)

    for i in range(2):
        jasmine.forward(30)
        jasmine.right(90)
        jasmine.forward(40)
        jasmine.right(90)

    jasmine.end_fill()

    jasmine.penup()
    jasmine.home()
    jasmine.goto(-295,-145)
    jasmine.pencolor("black")
    jasmine.pendown()
    jasmine.width(1)

    for i in range(2):
        jasmine.forward(30)
        jasmine.right(90)
        jasmine.forward(40)
        jasmine.right(90)
    
                     
    jasmine.penup()
    jasmine.goto(-295,-175)
    jasmine.pendown()
    jasmine.color("black")
    jasmine.begin_fill()
    jasmine.forward(30)
    jasmine.right(90)
    jasmine.forward(10)
    jasmine.circle(-15,180)
    jasmine.forward(10)
    jasmine.end_fill()





#outline for leg 2
    jasmine.penup()
    jasmine.home()
    jasmine.left(90)
    jasmine.goto(-325,-150)
    jasmine.pendown()
    jasmine.color("white")
    jasmine.begin_fill()
    jasmine.circle(-15,180)
    jasmine.forward(5)
    jasmine.right(90)
    jasmine.forward(30)
    jasmine.right(90)
    jasmine.forward(5)
    jasmine.end_fill()

    jasmine.penup()
    jasmine.home()
    jasmine.goto(-325,-150)
    jasmine.left(90)
    jasmine.pendown()
    jasmine.pencolor("black")
    jasmine.circle(-15,180)
    jasmine.forward(5)
    jasmine.right(90)
    jasmine.forward(30)
    jasmine.right(90)
    jasmine.forward(5)
    
    jasmine.penup()
    jasmine.left(180)
    jasmine.forward(5)
    jasmine.pendown()
    jasmine.color("black")
    jasmine.begin_fill()
    jasmine.left(90)
    jasmine.forward(30)
    jasmine.right(90)
    jasmine.forward(10)
    jasmine.circle(-15,180)
    jasmine.forward(10)
    jasmine.end_fill()

 
def drawBubbles():
    drawLine()
    drawBubblesBody()
    drawFace()
    drawHair()
    drawBubblesLegs()
    bubblesArms()




#draws entire image
def draw_scene():
    background()
    draw_buttercup()
    draw_blossom()
    drawBubbles()

#main
draw_scene()

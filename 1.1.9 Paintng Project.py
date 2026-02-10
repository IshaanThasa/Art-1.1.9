# 1.1.9 Painting Project - Simple House
import turtle as trtl

# Creating the turtle 
t = trtl.Turtle()
t.speed(1)
t.pensize(6)
# drawing the house walls 
def draw_rectangle(width, height):
    for i in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

# Making the roof of the house
def draw_roof(size):
    for i in range(3):
        t.forward(size)
        t.left(120)

# Start position for the house
t.penup()
t.goto(-50, -50)
t.pendown()

# Draw the house walls (base)
t.pencolor("brown")
draw_rectangle(100, 100)




# Draw the roof
t.penup()
t.goto(-50, 50)
t.pendown()
t.pencolor("red")
draw_roof(100)

# Draw the door
t.penup()
t.goto(-15, -50)
t.pendown()
t.pencolor("orange")
for i in range(2):
    t.forward(30)
    t.left(90)
    t.forward(50)
    t.left(90)

# Draw windows
t.pencolor("cyan")
for window_pos in range(2):
    if window_pos == 0:
        t.penup()
        t.goto(-35, 0)
        t.pendown()
    else:
        t.penup()
        t.goto(15, 0)
        t.pendown()
    
    # Draw window square
    for i in range(4):
        t.forward(20)
        t.left(90)

# Making the stick figure
# Draw the head
t.penup()
t.goto(-80, 50)
t.pendown()
t.pencolor("black")
t.setheading(0)
t.circle(10)
# Draw the body (straight down)
t.penup()
t.goto(-80, 45)
t.pendown()
t.pencolor("black")
t.setheading(270)
t.forward(80)
# Draw the arms 
t.penup()
t.goto(-80, 20)
t.pendown()
t.setheading(135)
t.forward(30)
t.penup()
t.goto(-80, 20)
t.pendown()
t.setheading(45)
t.forward(30)
# Draw the legs 
t.penup()
t.goto(-80, -35)
t.pendown()
t.setheading(225)
t.forward(30)
t.penup()
t.goto(-80, -35)
t.pendown()
t.setheading(315)
t.forward(30)

# Drawing the sun
t.penup()
t.goto(100, 100)
t.pendown()
t.pencolor("yellow")
t.fillcolor("yellow")
t.begin_fill()
t.circle(40)
t.end_fill()







t.penup()
t.goto(0, -100)
t.pendown()
t.hideturtle()
wn = trtl.Screen()
wn.mainloop()
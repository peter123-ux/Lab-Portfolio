import turtle as p
p.showturtle()


p.pensize(10)#this line indicates the size or thickness of the cirle


p.color("blue") #This line prints out the color of circle as blue
p.penup()#This line arranges the circle in alignment upward
p.goto(-110,-25)#This line gives the range of alignment the circle must fall within
p.pendown()#This line arranges the circle in alignment downward
p.circle(45)#This line determines the angle of the circle

p.color("black")
p.penup()
p.goto(0, -25)
p.pendown()
p.circle(45)

p.color("red")
p.penup()
p.goto(110, -25)
p.pendown()
p.circle(45)

p.color("yellow")
p.penup()
p.goto(-55, -75)
p.pendown()
p.circle(45)

p.color("green")
p.penup()
p.goto(55, -75)
p.pendown()
p.circle(45)


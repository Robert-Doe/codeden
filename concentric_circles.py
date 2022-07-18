# Python program to demonstrate
# concentric circle drawing
  
  
import turtle
import random
    
      
t = turtle.Turtle()
  
# radius of the circle
r = 1
box=['red','blue','black','brown']
# Loop for printing concentric circles
for i in range(1000):
    t.circle(r * i)
    t.up()
    t.sety((r * i)*(-1))
    t.color(random.choice(box),random.choice(box))
    t.down()
    t.speed(20)

turtle.done()
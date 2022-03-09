import turtle
import random
l1=[10,20,30,40,50,60,70,80,90,100,110,120]
c1=["red","blue","green","purple","cyan","brown","yellow","grey","black","orange","pink"]
def draw_lines(l,c):
    for value in l:
        turtle.forward(value)
        turtle.pencolor(random.choice(c))
        turtle.stamp()
        turtle.backward(value)
        turtle.right(30)
        l.append(value+20)
        l.remove(value)
draw_lines(l1,c1)


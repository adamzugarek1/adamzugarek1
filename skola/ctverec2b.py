import turtle
from turtle import *

def ctverec2(A):

  for i in range(4):
    forward(A)
    left(90)

delka = int(input("Zadejte délku strany:"))

ctverec2(delka)
penup()
goto(x=200, y=0)
pendown()
ctverec2(delka)

done()
import turtle
from turtle import *

def ctverec4(A,B,C):

  for i in range(B):
    forward(A)
    left(C)

lenght = int(input("délka:"))
sides = int(input("počet stran:"))
degrees = 360/sides

ctverec4(lenght, sides, degrees)
done()
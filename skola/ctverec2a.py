import turtle
from turtle import *

def ctverec(A):

  for i in range(4):
    forward(A)
    left(90)

delka = int(input("Zadejte délku strany:"))

ctverec(delka)
left(125)
ctverec(delka)
left(125)
ctverec(delka)

done()
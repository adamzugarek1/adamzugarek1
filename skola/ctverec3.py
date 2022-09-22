import turtle
from turtle import *

def ctverec3(A):

  for i in range(3):
    forward(A)
    left(120)

delka = int(input("Zadejte délku strany:"))

for i in range(6):
    ctverec3(delka)
    left(60)

done()
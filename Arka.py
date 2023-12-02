'''
!pip3 install ColabTurtle
import ColabTurtle.Turtle as turtle
from turtle import*
turtle.initializeTurtle()
turtle.speed(10)
turtle.pen_width = 1
turtle.pen_color = "blue"
for i in range(72):
    for_in range(4):
        turtle.forward(90)
        turtle.right(90)
    turtle.right(5)



def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

def gcf(a,b):
    if a<b:
        (a,b) = (b,a)

    while a%b != 0:
        (a,b) = (b, a%b)
    return b
print(gcf(34,10))
#HAHA IT WORKED! See I am good at python. We dont talk about the first one tho which was the average calculater. I really did forget just like that even one.

def gcf2(x, y):
    if x > y:
        a = x
    else:
        b = y
    while x > 1:
        if x % a == 0 and y % a == 0:
            break
        a -= 1
    print(a)
print(gcf2(34, 10))

from test_arka import gcf_calc

x = int(input("Whats your first number? "))
y = int(input("Whats your second number? "))
z = gcf_calc(x, y)

print(int((x*y)/z))

def lcm(x, y):
    i = max(x,y)
    while(True):
        if i%x == 0 and i%y == 0:
            return i
        i += 1

print(f"{lcm(10, 9)=}")
'''

def factorial_calc(n):
    factorial = 1
    for i in range(1,n + 1):
       factorial = factorial*i
    return factorial
print(factorial_calc(6))
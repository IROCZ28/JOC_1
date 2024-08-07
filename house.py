import turtle

def triangle(len):  #len - distance per side
   for i in range(3):
      turtle.forward(len)
      turtle.left(120)

def square(len):    #len - distance per side
   for i in range(4):
      turtle.forward(len)
      turtle.right(90)

def house(len):
  square(len)
  triangle(len)

def move(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()

def main():
  move(100)
  turtle.color("red")
  house(120)
  move(-150)
  turtle.color("blue")
  house(70)

main()

import turtle

def octogon(len):  #len - distance per side
   for i in range(8):
      turtle.forward(len/2)
      turtle.left(360/8)

def post(len, wid):    #len - distance per side
      turtle.forward(wid)
      turtle.right(90)
      turtle.forward(len)
      turtle.right(90)
      turtle.forward(wid)
      turtle.right(90)
      turtle.forward(len)
      turtle.right(90)

def stopsign(len, wid):
  octogon(len)
  move(-(len/4)+(wid/2))
  post(len, wid)

def move(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()

def main():
  move(100)
  turtle.color("orange")
  stopsign(60, 12)
  move(-125)
  turtle.color("purple")
  stopsign(40,8)

main()

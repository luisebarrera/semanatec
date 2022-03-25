"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

from turtle import *
from random import randrange
from freegames import square, vector

isStarted = False
snake = [[10, 0]]
aim = [0, 0]
food = [60, 60]
interval = 100

def change(x, y):
  global isStarted # need this line to avoid error
  if not isStarted:
    isStarted = True
  aim[0] = x
  aim[1] = y

def draw_square(x, y, size, name):
  up()
  goto(x, y)
  down()
  color(name)
  begin_fill()

  for count in range(4):
    forward(size)
    left(90)

  end_fill()

def draw_bounding_box():
  up()
  goto(-200, -200)
  down()
  color('black')
  for count in range(4):
    forward(400)
    left(90)


def inside(head):
    return -200 < head[0] < 190 and -200 < head[1] < 190

def move():
  if isStarted:
    head = [snake[-1][0] + aim[0], snake[-1][1] + aim[1]]
    
    if head[0] > 190:
      head[0] = -200
    elif head[0] < -200:
      head[0] = 190
    elif head[1] > 190:
      head[1] = -200
    elif head[1] < -200:
      head[1] = 190
  
    if head in snake:
      draw_square(head[0], head[1], 9, 'red')
      up()
      goto(0, 0)
      write("Game Over", align="center", font=("Arial", 14, "bold"))
      update()
      return
    
    if head == food:
      food[0] = randrange(-15, 15) * 10
      food[1] = randrange(-15, 15) * 10
      global interval
      interval -= 5
    else:
      snake.pop(0)
      
    snake.append(head)
    
  clear()
  
  draw_bounding_box()
  
  draw_square(food[0], food[1], 9, 'green')
  
  for body in snake:
    draw_square(body[0], body[1], 9, 'black')

  update()
  Screen().ontimer(move, interval)

Screen().setup(420, 420, 370, 0)
hideturtle()
Screen().tracer(0, 0)

Screen().listen()
Screen().onkey(lambda: change(10, 0), 'Right')
Screen().onkey(lambda: change(-10, 0), 'Left')
Screen().onkey(lambda: change(0, 10), 'Up')
Screen().onkey(lambda: change(0, -10), 'Down')

move()

done()

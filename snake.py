"""
1.Mauricio Tumalán Castillo A01369288
2.Luis Emilio Barrera A01368759
3.Elias Yañez A01028482
"""
#Se importan funciones de librerias preestablecidas dentro de python
from turtle import *
from random import randrange
from freegames import square, vector

#Se inicializan variables que se utilizarán posteriormente
food = vector(0,0)
snake = [vector(10, 0)]
aim = vector(0,-10)

#Cambio de dirección de serpiente
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

#Se verifica que la cabeza entre dentro del tablero
def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

#Movimiento
def move():
    "Move snake forward one segment"
    head = snake[-1].copy()
    head.move(aim)
    
    if head.x > 190:
      head.x = -200
    elif head.x < -200:
      head.x = 190
    elif head.y > 190:
      head.y = -200
    elif head.y < -200:
      head.y = 190
  
    if head in snake:
      square(head.x, head.y, 9, 'red')
      update()
      return
    
    snake.append(head)
      
    #Se alarga la serpiente si come fruta y se añade puntaje
    if head == food:
        print('Snake:', len(snake))
        
        #Se cambia el spawn de fruta acorde al puntaje preestablecido
        if len(snake) > 0 and len(snake) < 10:
            food.x = randrange(-15, 15) * 10
            food.y = randrange(-15, 15) * 10
        elif len(snake) >= 10 and len(snake) < 20:
            food.x = randrange(-10, 10) * 10
            food.y = randrange(-10, 10) * 10
        elif len(snake) >= 20:
            food.x = randrange(-5, 5) * 10
            food.y = randrange(-5, 5) * 10
    else:
        snake.pop(0)

    clear()

    #Dibujo de snake
    for body in snake:
        square(body.x, body.y, 9, 'black')

    #Dibujo de fruta
    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()

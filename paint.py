"""
1.Mauricio Tumalán Castillo A01369288
2.Luis Emilio Barrera A01368759
3.Elias Yañez A01028482
"""

#Se importan funciones necesarias de librerías preestablecidas
import turtle
from math import hypot
from turtle import *
from freegames import vector

#Crear linea
def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

#Crear cuadrado
def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

#Crear circulo
def circle(start, end):
    "Draw circle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    turtle.circle(hypot(end.x - start.x, end.y - start.y))
    
    end_fill()

#Crear rectangulo
def rectangle(start, end):
    
    begin_fill()    

    for i in range(1,5):
        if i % 2 == 1:   
            d = 200
        else:
            d = 120
        forward(d)
        left(90)    
    end_fill()      

    pass  # TODO

#Crear triangulo
def triangle(start, end):
    "Draw triangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(3):
        forward(end.x - start.x)
        left(120)

    end_fill()

#Guardado de punto de inicio del dibujado de alguna de las figuras de arriba
def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

#guarda el valor de la tecla presionada
def store(key, value):
    "Store value in state at key."
    state[key] = value

#inicialización del programa y llamado de las funciones creadas arriba
state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
#valores establecidos para cambiar opciones dentro del juego
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('magenta'), 'M')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()

from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def render_frame(x, y):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    delay(0.1)

def run_circle():
    print('CIRCLE')

    cx, cy, r = 400, 300, 200
    for deg in range(0, 360, 5):
        x = r*math.cos(math.radians(deg))
        y = r*math.sin(math.radians(deg))

        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.1)

def run_rectangle():
    print('RECTANGLR')

    #bottom line
    for x in range(50, 750+1, 5):
        render_frame(x, 50)  #x, y위치에 캐릭터 그려줄 수 있는
    #top line
    for x in range(750, 50-1, -5):
        render_frame(x, 550)
    #right line
    for x in range(50, 550+1, 5):
        render_frame(750, y)
    #left line
    for x in range(550, 50-1, -5):
        render_frame(50, y)


        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.1)
    
while True:
    run_circle()
    run_rectangle()
    break

close_canvas()

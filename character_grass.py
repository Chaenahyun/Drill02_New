from pico2d import *
import math

open_canvas()

# fill here
grass = load_image('grass.png')
image = load_image('character.png')
image.draw_now(400, 300)
delay(1)

def run_circle():
    print('CIRCLE')

    cx, cy, r = 400, 300, 200
    for deg in range(0, 360, 5):
        x = r*math.cos(math.radians(deg))
        y = r*math.sin(math.radians(deg))
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)

    pass

def run_rectangle():
    print('RECTANGLR')
    pass

close_canvas()

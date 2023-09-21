from pico2d import *

open_canvas()

# fill here
grass = load_image('grass.png')

image = load_image('character.png')
image.draw_now(400, 300)
delay(1)

def run_circle():
    print('CIRCLE')
    pass

def run_rectangle():
    print('RECTANGLR')
    pass

close_canvas()

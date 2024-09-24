import os
import math
from pico2d import *

open_canvas()

os.chdir('C:\\tuk_GitHub\\2DGP-Drill-03')

grass = load_image('grass.png')
boy = load_image('character.png')

def run_circle():
    print('CIRCLE')
    
    clear_canvas_now()
    boy.draw_now(400,300)
    delay(0.01)

def run_rectangle():
    print('RECTANGLE')
    pass

while True:
    run_circle()
    run_rectangle()
    
    delay(5)
    break
    

import random
from pico2d import *

import game_framework
import game_world

from boy import Boy
from grass import Grass
from ball import Ball
from zombie import Zombie

boy = None

def handle_events():
    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global boy
    zombies = [Zombie() for i in range(4)]
    game_world.add_objects(zombies, 1)
    grass = Grass()
    game_world.add_object(grass, 0)
    game_world.add_collision_pair('grass:ball', grass, None)

    boy = Boy()
    game_world.add_object(boy, 1)

    # 바닥에 공 배치
    global balls
    balls = [Ball(random.randint(200, 1600), 60, 0) for _ in range(20)]
    game_world.add_objects(balls, 1)
    game_world.add_collision_pair('boy:ball',boy, None)   # boy 중복 방지
    for ball in balls:
        game_world.add_collision_pair('boy:ball', None, ball)
        #game_world.add_collision_pair('grass:ball', None, ball)




def update():
    game_world.update()
    game_world.handle_collisions()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def finish():
    game_world.clear()

def pause(): pass
def resume(): pass


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

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    # 바닥에 공 배치
    global balls
    balls = [Ball(random.randint(200, 1600), 60, 0) for _ in range(20)]
    game_world.add_objects(balls, 1)



def update():
    game_world.update()
    # boy와 ball 간의 충돌을 체크
    for ball in balls.copy():   # balls의 복사본
        if game_world.collide(boy, ball):
            print("COLLISION! ball")
            boy.ball_count += 1
            game_world.remove_object(ball)
            balls.remove(ball)   # 원본을 지우고, 그 다음에는 원본을 지운것을 copy하여 안전하게 삭제


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def finish():
    game_world.clear()

def pause(): pass
def resume(): pass


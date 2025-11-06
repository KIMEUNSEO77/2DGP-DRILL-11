world = [[] for _ in range(4)]

def add_object(o, depth = 0):
    world[depth].append(o)


def add_objects(ol, depth = 0):
    world[depth] += ol


def update():
    for layer in world:
        for o in layer:
            o.update()


def render():
    for layer in world:
        for o in layer:
            o.draw()

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return

    raise ValueError('Cannot delete non existing object')


def clear():
    global world

    for layer in world:
        layer.clear()


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True   # 충돌 발생

collision_pairs = {} # (a,b) 쌍의 충돌 상태를 저장하는 딕셔너리

def add_collision_pair(group, a, b):   # 충돌 정보, 객체 a, 객체 b
    if group not in collision_pairs:   # 처음 등록되는 그룹이면
        collision_pairs[group] = [[], []]   # 충돌 객체 리스트 쌍 생성

    collision_pairs[group][0].append(a)   # 첫 번째 리스트에 a 추가
    collision_pairs[group][1].append(b)   # 두 번째 리스트에 b 추가

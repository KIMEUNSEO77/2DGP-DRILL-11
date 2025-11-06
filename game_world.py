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
            remove_collision_object(o)   # collision 내의 정보도 제거
            return

    raise ValueError('Cannot delete non existing object')

def remove_collision_object(o):
    for pairs in collision_pairs.values():
        # 그룹에 따른 제거
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)
            
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
    if a:
        collision_pairs[group][0].append(a)   # 첫 번째 리스트에 a 추가 (None이 추가되는 것을 방지)
    if b:
        collision_pairs[group][1].append(b)   # 두 번째 리스트에 b 추가 (None이 추가되는 것을 방지)


# 등록된 모든 충돌 그룹에 대해 충돌 검사
def handle_collisions():
    for group, pairs in collision_pairs.items():
        for a in pairs[0]:   # 첫 번째 리스트의 모든 객체에 대해
            for b in pairs[1]:   # 두 번째 리스트의 모든 객체에 대해
                if collide(a, b):   # 충돌 검사
                    a.handle_collision(group, b)   # a가 충돌 처리
                    b.handle_collision(group, a)   # b가 충돌 처리
from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

def handle_events():

    global running, moving
    global x, y

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def draw_hand():
    global hand_x, hand_y
    hand_x = random.randint(0,800)
    hand_y = random.randint(0,600)
    hand.draw(hand_x,hand_y)
    update_canvas()
    pass

def move_character():
    global x, y
    t = 0
    frame = 0
    while t <= 1:
        x = (1-t) * character_x + t * hand_x
        y = (1-t) * character_y + t * hand_y

        make_background()

        if x <= character_x:
            character.clip_draw(frame * 100, 0, 100, 100, x, y)
        elif x >= character_x:
            character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()

        frame = (frame + 1) % 8
        t += 0.1
        delay(0.05)
    pass


def make_background():
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand.draw(hand_x, hand_y)


# 기본 변수값
running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0

# 일단 랜덤값으로 시작, 의미없는 더미변수
hand_x = random.randint(0, 800)
hand_y = random.randint(0, 600)
character_x = random.randint(0,800)
character_y = random.randint(0,600)

hide_cursor()

while running:
    moving = True
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    draw_hand()
    while moving:
        move_character()
        character_x = hand_x
        character_y = hand_y
        moving = False
        handle_events()
close_canvas()





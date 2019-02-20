import pygame

import random

import os

from pygame.locals import *

import sys

import time

import pyganim

pygame.init()

pygame.display.set_caption("Math Lesson")

size = width, height = 960, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


running = True

rect_width = 0
rect_x = 50
rect_y = 50
square_width = 130
square_height = 66
rect_color = (70, 70, 70)
rect_rect = ((rect_x, rect_y), (square_width, square_height))
x1 = x2 = y1 = y2 = 0


def load_image(name, colorkey=None):

    fullname = os.path.join(name)

    try:

        image = pygame.image.load(fullname)

    except pygame.error as message:

        print('Cannot load image:', name)

        raise SystemExit(message)

    image = image.convert_alpha()



    if colorkey is not None:

        if colorkey is -1:

            colorkey = image.get_at((0, 0))

        image.set_colorkey(colorkey)

    return image


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(all_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


spis = ['m.png', 'm1.png', 'm2.png', 'm3.png', 'm5.png']
a = random.randint(0, 4)
BackGround = Background(spis[a], (0, 0))

primer = ['12 + 12', '12 + 84', '16 + 58',
          '30 - 7',	'86 - 24', '34 + 16',
          '39 + 43', '10 + 5', '12 + 66',
          '98 - 72', '42 + 46', '98 - 80',
          '95 - 30', '15 + 58', '47 - 18',
          '38 + 32', '73 + 2', '86 - 14',
          '6 * 5', '21 : 7', '27 : 3',
          '4 * 3', '30 : 6', '8 * 8',
          '8 * 6', '7 * 7', '54 : 9',
          '18 : 9', '3 * 12', '5 * 7',
          '7 * 8', '56 : 7', '44 : 4',
          '8 : 2', '28 : 4', '39 : 3', '15 + 7', '68 - 7',
          '81 - 13', '32 - 13',	'87 - 25', '22 + 78',
          '51 - 8',  '78 - 65', '13 + 23', '6 + 85',
          '57 - 1',	'50 + 36', '83 - 69']

solutions = [24, 96, 74, 23, 62, 50,
             82, 15, 78, 26, 88, 18, 65, 73,
             29, 70, 75, 72, 30, 3, 9, 12,
             5, 64, 48, 49, 6, 2, 36, 35,
             56, 8, 11, 4, 7, 13, 22, 61, 69, 19, 62, 100, 43, 18, 36, 91, 56, 86, 14]

all_sprites = pygame.sprite.Group()

robot_image = load_image("robot.png")

robot = pygame.sprite.Sprite(all_sprites)

robot.image = robot_image

robot.rect = robot.image.get_rect()


def draw(b, c, d):

    global primer

    font = pygame.font.Font(None, 50)
    text = font.render(primer[b], 1, (100, 255, 100))
    text_x = width // 4 - 70
    text_y = height // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (255, 255, 255), (text_x - 10, text_y - 10,
                                           text_w + 20, text_h + 20), 3)


    text1 = font.render(primer[c], 1, (100, 255, 100))
    text_x1 = width // 2 - 70
    text_w1 = text1.get_width()
    text_h1 = text1.get_height()
    screen.blit(text1, (text_x1, text_y))
    pygame.draw.rect(screen, (255, 255, 255), (text_x1 - 10, text_y - 10,
                                           text_w1 + 20, text_h1 + 20), 3)


    text2 = font.render(primer[d], 1, (100, 255, 100))
    text_x2 = width // 2 + width // 4 - 70
    text_w2 = text2.get_width()
    text_h2 = text2.get_height()
    screen.blit(text2, (text_x2, text_y))
    pygame.draw.rect(screen, (255, 255, 255), (text_x2 - 10, text_y - 10,
                                           text_w2 + 20, text_h2 + 20), 3)

    left1 = text_x
    right1 = text_x + 0.15 * text_x
    left2 = text_x1
    right2 = text_x1 + 0.15 * text_x1
    left3 = text_x2
    right3 = text_x2 + 0.15 * text_x2

    top = text_y - 0.2 * text_y
    bottom = text_y + 0.2 * text_y

    return left1, right1, left2, right2, left3, right3, top, bottom


screen.fill(pygame.Color('black'))

screen.blit(BackGround.image, BackGround.rect)

b = random.randint(0, len(primer) - 1)

c = random.randint(0, len(primer) - 1)

d = random.randint(0, len(primer) - 1)

draw(b, c, d)

otvet = False

s = [d, b, c]

x = solutions[int(s[random.randint(0, 2)])]

o = 0

font = pygame.font.Font(None, 50)
text = font.render(str(x), 1, (100, 255, 100))
# textx = rect_x + 45
# texty = rect_y + 20
# text_w = 30
# text_h = 45
# screen.blit(text, (textx, texty))

x1 = 0
y1 = 0

f = False

robot = AnimatedSprite(load_image('robot.png'), 13, 2, 131, 150)

boltAnim = pyganim.PygAnimation([('testimages/bolt_strike_0001.png', 0.1),
                                 ('testimages/bolt_strike_0002.png', 0.1),
                                 ('testimages/bolt_strike_0003.png', 0.1),
                                 ('testimages/bolt_strike_0004.png', 0.1),
                                 ('testimages/bolt_strike_0005.png', 0.1),
                                 ('testimages/bolt_strike_0006.png', 0.1),
                                 ('testimages/bolt_strike_0007.png', 0.1),
                                 ('testimages/bolt_strike_0008.png', 0.1),
                                 ('testimages/bolt_strike_0009.png', 0.1),
                                 ('testimages/bolt_strike_0010.png', 0.1)])
boltAnim.play() # there is also a pause() and stop() method

mainClock = pygame.time.Clock()


while running:

    screen.fill(pygame.Color('black'))

    screen.blit(BackGround.image, BackGround.rect)


    pygame.draw.rect(screen, rect_color, rect_rect, rect_width)


    left1, right1, left2, right2, left3, right3, top, bottom = draw(b, c, d)




    if left1 <= rect_x <= right1 and top <= rect_y <= bottom:
        if x == solutions[int(b)]:
            otvet = True
    elif left2 <= rect_x <= right2 and top <= rect_y <= bottom:
        if x == solutions[int(c)]:
            otvet = True
    elif left3 <= rect_x <= right3 and top <= rect_y <= bottom:
        if x == solutions[int(d)]:
            otvet = True

    if otvet:
        o += 1


    if o == 10:

        b = random.randint(0, len(primer) - 1)

        c = random.randint(0, len(primer) - 1)

        d = random.randint(0, len(primer) - 1)

        s = [d, b, c]

        x = solutions[int(s[random.randint(0, 2)])]

        otvet = False

        o = 0

        rect_y = 200
        rect_x = 400

        f = False



    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()


            if event.type == pygame.MOUSEBUTTONDOWN:
                x1, y1 = event.pos
                f = True

    if x1 > rect_x and f:
        rect_x += 1
    elif x1 < rect_x and f:
        rect_x -= 1
    
    if y1 > rect_y and f:
        rect_y += 1
    elif y1 < rect_y and f:
        rect_y -= 1

    text = font.render(str(x), 1, (100, 255, 100))
    textx = rect_x
    texty = rect_y - 20
    screen.blit(text, (textx, texty))

    rect_rect = ((rect_x - 50, rect_y - 50), (square_width, square_height))

    pygame.draw.rect(screen, (169, 169, 169), (0, 0, 960, 600), 10)

    boltAnim.blit(screen, (rect_x - 50, rect_y - 70))

    pygame.display.flip()

    clock.tick(50)

pygame.quit()

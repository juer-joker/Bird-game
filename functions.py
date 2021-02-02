import sys

import pygame
from blocks import Block
from time import sleep


def check_keydown(event, bird):
    if event.key == pygame.K_UP:
        bird.moving_up = True
    if event.key == pygame.K_DOWN:
        bird.moving_down = True


def check_key_up(event, bird):
    if event.key == pygame.K_UP:
        bird.moving_up = False
    if event.key == pygame.K_DOWN:
        bird.moving_down = False


def check_events(bird):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, bird)
        elif event.type == pygame.KEYUP:
            check_key_up(event, bird)


def create_blocks(sets, screen, blocks, bird):
    """创建柱子群"""
    block = Block(sets, screen)
    block_width = block.rect.width

    for block_number in range(15):
        block_1 = Block(sets, screen)
        block_2 = Block(sets, screen)
        block_1.x = 4 * bird.rect.x + 2.5 * block_width * block_number
        block_2.x = 4 * bird.rect.x + 2.5 * block_width * block_number
        block_1.y = 200#random.randint(150, 350)
        block_1.rect.x = block_1.x
        block_2.rect.x = block_2.x  #block_1.rect.left
        block_1.rect.bottom = block_1.y
        block_2.rect.top = block_1.rect.bottom + 150
        blocks.add(block_1)
        blocks.add(block_2)


def update_blocks(sets, stats, bird, screen, blocks):
    blocks.update()

#    #检测碰撞
    if pygame.sprite.spritecollideany(bird, blocks):
        game_stop(sets, stats, screen, bird, blocks)


def game_stop(sets, stats, screen, bird, blocks):
    if stats.bird_left > 1:
        """游戏结束"""
#        #将birdleft -1
        stats.bird_left -= 1
        blocks.empty()
        bird.center()
        create_blocks(sets, screen, blocks, bird)
        sleep(1)

    else:
        stats.game_active = False


def update_screen(sets, screen, bird, blocks):
    screen.fill(sets.bg_color)
    bird.blitme()
    blocks.draw(screen)

    pygame.display.flip()

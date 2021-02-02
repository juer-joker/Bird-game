import pygame
from pygame.sprite import Group
from settings import Set
from bird import Bird
import functions as f
from game_stats import GameStats


def run():
    pygame.init()
    sets = Set()
    screen = pygame.display.set_mode((sets.width, sets.height))
    stats = GameStats(sets)
    bird = Bird(sets, screen)
    blocks = Group()
    pygame.display.set_caption("小鸟闯关")

    f.create_blocks(sets, screen, blocks, bird)

    while True:
        f.check_events(bird)
        if stats.game_active:
            bird.update()
            f.update_blocks(sets, stats, bird, screen, blocks)
        f.update_screen(sets, screen, bird, blocks)


run()

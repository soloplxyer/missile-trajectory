import os
import sys
import pygame as pg
from pygame.locals import *
from missile import *

# config
CAPTION = "Missile Trajectory Simulation"
SCREEN_SIZE = (1080, 720)
BACKGROUND = pg.image.load('assets/img/background.png')

class Simulation(object):
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.clock = pg.time.Clock()
        self.fps = 60
        self.done = False
        self.missile = missile(45, 20, 900, 10, 5, 90, 0)

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True

    def update(self, dt):
        self.missile.update(dt)
        
    def render(self):
        self.screen.blit(BACKGROUND, (0,0))
        self.missile.draw(self.screen)
        pg.display.update()

    def main_loop(self):
        dt = 0
        self.clock.tick(self.fps)
        while not self.done:
            dt = self.clock.tick(self.fps)/1000.0
            self.event_loop()
            self.update(dt)
            self.render()
            
def main():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pg.init()
    pg.display.set_caption(CAPTION)
    pg.display.set_mode(SCREEN_SIZE)
    Simulation().main_loop()
    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()
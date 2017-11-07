import os
import sys
import pygame as pg
from pygame.locals import *
from missile import *
#import matplotlib.pyplot as plt

# config
CAPTION = "Missile Trajectory Simulation"
SCREEN_SIZE = (1080, 720)
BACKGROUND = pg.image.load('assets/img/background.png')

class Simulation(object):
    """
    Class responsible for program control flow.
    """
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.clock = pg.time.Clock()
        self.fps = 60
        self.done = False
        self.missile = missile(45, 20, 900, 10, 5, 90, 0)

    def event_loop(self):
        """
        Basic event loop.
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True

    def update(self, dt):
        """
        Update must acccept and pass dt to all elements that need to update.
        """
        self.missile.update(dt)
        
    def render(self):
        """
        Render all needed elements and update the display.
        """
        self.screen.blit(BACKGROUND, (0,0))
        self.missile.draw(self.screen)
        pg.display.update()

    def main_loop(self):
        """
        We now use the return value of the call to self.clock.tick to
        get the time delta between frames.
        """
        
        dt = 0
        self.clock.tick(self.fps)
        while not self.done:
            dt = self.clock.tick(self.fps)/1000.0
            self.event_loop()
            self.update(dt)
            self.render()
            
def main():
    """
    Initialize; create an App; and start the main loop.
    """
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pg.init()
    pg.display.set_caption(CAPTION)
    pg.display.set_mode(SCREEN_SIZE)
    Simulation().main_loop()
    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()
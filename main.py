# Project: Youtube Converter Application
# Author: Mitchell Devlin
# Date: 08/22/17

import pygame
from pygame.locals import *
import threading
import time
from math import *
from numpy import *
from random import *

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)

colors = [(255,0,0),(0,255,0),(0,0,255),(255,255,0),(255,51,255)]

class Particle(pygame.sprite.Sprite):
    def __init__(self, scr, color, pos):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.screen = scr
        self.acc = 10
        self.speed = 0
        self.pos = pos
        self.time = 0
        self.surface = pygame.Surface((8,8))
        self.surface.fill(self.color)
        self.rect = self.surface.get_rect()
        self.mask = pygame.mask.from_surface(self.surface)

    def set_array(self, array):
        self.array = array

    def start_fall(self):
        self.speed = 0

    def update(self, time, angle):
        self.time = time
        self.speed = self.acc * self.time
        self.speed = int(self.speed)
        self.pos = (self.pos[0] + int(self.speed*math.cos(math.radians(angle))), 
            self.pos[1] + int(self.speed*math.sin(math.radians(angle))))
        self.mask = pygame.mask.from_surface(self.surface)
        self.screen.blit(self.surface, self.pos)


def main():
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption('Particle Simulation')
    pygame.time.delay(300)
    pygame.draw.rect(screen, white, (0,0,1000,600), 0)
    start_time = time.time()   
    pygame.draw.rect(screen, white, (0,0,1000,600), 0)
    rampSurf = pygame.Surface((100,4))
    rampSurf.fill(white)
    ramp = pygame.draw.rect(rampSurf, black, (0,0,100,4), 0)
    #rampSurf = pygame.transform.rotate(rampSurf, -45)

    p = Particle(screen, colors[0], (260, 300))
    while True:
        screen.blit(rampSurf, (300, 450))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        if p.rect.contains(ramp):
            p.update(time.time()-start_time, -45)
        else:
            p.update(time.time()-start_time, 90)

        pygame.display.update()

    
def quit():
    pygame.quit()
    sys.exit()

main()

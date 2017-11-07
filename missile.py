from __future__ import division
import pygame as pg
from pygame.locals import *
from math import *
from utils import *
from athmosphere import *
import matplotlib.pyplot as plt
import numpy as np

# constants
FORCE_KG = 40000
FUEL_WEIGHT = 1 # 1kg/L

class missile(object):
    def __init__(self, angle, fuel, mass, fueluse, width, length, thrustangle):
        self.sprite = pg.image.load('assets/img/missile.png').convert_alpha()

        self.x = 0;
        self.y = 0;
        self.area = pi * (width/2)**2

        self.width = width
        self.length = length

        self.thrust_angle = thrustangle
        self.angle = angle

        self.vx = 0
        self.vy = 0

        self.fuel = fuel
        self.mass = mass

        self.fueluse = fueluse

        self.airDensity = []
        self.airPressure = []
        self.xArray = []
        self.yArray = []
        self.fuelArray = []
        self.massArray = []
        self.fDragX = []
        self.fDragY = []
        self.vxArray = []
        self.vyArray = []
        self.angleArray = []

    def draw(self, screen):
        surf = pg.transform.rotozoom(self.sprite, -(90 - self.angle), 1)
        screen.blit(surf, (self.x, 624 - self.y))

    def update(self, DELTA_T):
        if self.y >= 0:
            if self.fuel >= (self.fueluse * DELTA_T):
              self.fuel -= (self.fueluse * DELTA_T)
              self.mass -= self.fueluse * FUEL_WEIGHT * DELTA_T

              f_missile_x = FORCE_KG * self.fueluse * cos(radians(self.angle - self.thrust_angle))
              f_missile_y = FORCE_KG * self.fueluse * sin(radians(self.angle - self.thrust_angle))
            else:
              f_missile_x = 0
              f_missile_y = 0

            f_gravity = Gravity(self.y) * self.mass

            f_drag_communal = 1/2 * getAirDensity(self.y) * self.area * speed(self.vx, self.vy)**2 * 0.63
            f_drag_x = cos(radians(self.angle)) * f_drag_communal
            f_drag_y = sin(radians(self.angle)) * f_drag_communal

            self.vx += ((f_missile_x - f_drag_x) / self.mass) * DELTA_T
            self.vy += ((f_missile_y - f_drag_y - f_gravity) / self.mass) * DELTA_T

            self.x += self.vx * DELTA_T
            self.y += self.vy * DELTA_T

            #print("<tr><td>" + str(getAirDensity(self.y)) + "</td><td>" + str(getAirPressure(self.y)) + "</td></tr>")

            print(getAirPressure(self.y))
            self.angle = angleToPoint(self.x, self.y, self.x + self.vx, self.y + self.vy)
            self.airPressure.append(getAirPressure(self.y))
            self.airDensity.append(getAirDensity(self.y))
            self.xArray.append(self.x)
            self.yArray.append(self.y)
            self.fuelArray.append(self.fuel)
            self.massArray.append(self.mass)
            self.fDragX.append(f_drag_x)
            self.fDragY.append(f_drag_y)
            self.vxArray.append(self.vx)
            self.vyArray.append(self.vy)
            self.angleArray.append(self.angle)
            self.key = False
        else:
            if self.key == False:

                print("Media densidade do ar: " + str(np.mean(self.airDensity)))
                print("Media pressao do ar: " + str(np.mean(self.airPressure)))

                self.key = True

                plt.plot(self.airPressure)
                plt.ylabel('Pressao do ar')
                plt.show()

                plt.plot(self.airDensity)
                plt.ylabel('Densidade do ar de acordo com a altitude')
                plt.show()

                plt.plot(self.xArray)
                plt.ylabel('Posicao X')
                plt.show()

                plt.plot(self.yArray)
                plt.ylabel('Posicao Y')
                plt.show()

                plt.plot(self.fuelArray)
                plt.ylabel('Combustivel')
                plt.show()

                plt.plot(self.fuelArray)
                plt.ylabel('Combustivel')
                plt.show()

                plt.plot(self.massArray)
                plt.ylabel('Massa')
                plt.show()

                plt.plot(self.fDragX)
                plt.ylabel('Forca de arrasto na horizontal')
                plt.show()

                plt.plot(self.fDragY)
                plt.ylabel('Forca de arrasto na vertical')
                plt.show()

                plt.plot(self.vxArray)
                plt.ylabel('Velocidade do missel na horizontal')
                plt.show()

                plt.plot(self.vyArray)
                plt.ylabel('Velocidade do missel na vertical')
                plt.show()

                plt.plot(self.angleArray)
                plt.ylabel('Angulo')
                plt.show()

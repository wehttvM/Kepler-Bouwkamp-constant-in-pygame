import math
import os
import platform
import sys
import time
from datetime import datetime

from win32api import GetSystemMetrics

import numpy
import pygame

pygame.init()

# size of screen
#size = width, height = 1366, 768
size = width, height = 500, 500
HalfSizeFloat = HalfSizeWidthFloat, HalfSizeHeightFloat = width / 2, height / 2
HalfSizeInteger = HalfSizeWidthInteger, HalfSizeHeightInteger = (
    width // 2,
    height // 2,
)


# fill color
Black = (0, 0, 0)
PrettyYellow = 255, 255, 0
# select display mode which is fullscreen and the size of screen
screen = pygame.display.set_mode(size, pygame.RESIZABLE)

# Regular Polygon Code.


def polygon(sides, radius=1, rotation=0, translation=None):
    one_segment = math.pi * 2 / sides

    points = [
        (math.sin(one_segment * i + rotation) * radius,
         math.cos(one_segment * i + rotation) * radius)
        for i in range(sides)]

    if translation:
        points = [[sum(pair) for pair in zip(point, translation)]
                  for point in points]

    return points


PolygonFloat = (height / 2)
PolygonInteger = int(PolygonFloat)
# the polygon sides value controls the amount of sides that the initial polygon will have.
PolygonSides = 3
PolygonRadius = PolygonFloat
PolygonRotation = 0
PolygonTranslation = 0
PolygonList = polygon(PolygonSides, PolygonRadius, PolygonRotation, PolygonTranslation)
PolygonListFloat = numpy.add(PolygonList, PolygonFloat)
# the n value is the number of seqences between cirlce and polygons to end the definition so it doesnt lag
n = 0
NumberOfPolygons = 5


def PolygonRepeater(n, PolygonListFloat, PolygonSides):
    PolygonListFloat = PolygonListFloat
    PolygonSides = PolygonSides
    n = n
    # the value that is greater than n in this value can be adjusted to increase the amount of sequences that your would like.
    if n < NumberOfPolygons:
        n = n + 1
        # find the first 2 points in the initial list of polygon
        x1, y1 = PolygonListFloat[0]
        x2, y2 = PolygonListFloat[1]
        # find the mid point of the 2 first points in the list of polygon points
        MidPoint = MidPointx, MidPointy = ((x1 + x2) / 2, (y1 + y2) / 2)
        # find the distance from the center of the width and hieght to the midpoint of the first 2 points in the polygon list.
        DisRadius = int(math.sqrt((MidPointx - HalfSizeWidthFloat) ** 2 + (MidPointy - HalfSizeHeightFloat) ** 2))
        # find the points for the next polygon using the radius of the previous circle and the polygon sides of the initial polygon adding one side.
        PolygonSides = PolygonSides + 1
        PolygonList = polygon(PolygonSides, DisRadius, PolygonRotation, PolygonTranslation)
        # create a numpy array and also add half the height to make the polygon proportional.
        PolygonListFloat = numpy.add(PolygonList, PolygonFloat)
        # first circle in the sequence
        pygame.draw.circle(screen, Black, HalfSizeInteger, DisRadius, 2)
        # fist PolyGon is Sequence
        pygame.draw.polygon(screen, Black, PolygonListFloat, 2)
        # run this same function over again with the declared value that are stated in this function.
        PolygonRepeater(n, PolygonListFloat, PolygonSides)
    return


while 1:
    # if user clicks the X button quit program
    # if user presses escape button quit program
    for event in pygame.event.get():
        if event.type in [pygame.QUIT, pygame.K_ESCAPE]:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

    # print initial frame screen
    screen.fill(PrettyYellow)

    # initial Polygon
    # Draw a Black Polygon with hte initial polygon list points to the screen
    pygame.draw.polygon(screen, Black, PolygonListFloat, 2)
    # initial Circle
    # Draw a Black Circle with an origin of the width or hegiht divided by 2 and that has radius of width or height divided by 2 with a perimiter out line of black.
    pygame.draw.circle(screen, Black, HalfSizeInteger, PolygonInteger, 2)
    # using the PolygonRepeater Function that is defined in the near begining of the code we input the n and polygon side value declared in the setup aswell as inputing the PolygonList in float type
    PolygonRepeater(n, PolygonListFloat, PolygonSides)

    pygame.display.flip()
    pygame.image.save(screen, "screenshot.jpeg")

    # delay next frame screen for 5 sec
    pygame.time.delay(1000)

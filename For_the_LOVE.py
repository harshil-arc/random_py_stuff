import pygame
import math
import random
import sys

pygame.init()
W,H=800,800
screen=pygame.display.set_mode((W,H))
pygame.display.set_caption("For_the_LOVE")
clock=pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)

TEXT="love you"
PINK=(255,77,109)
BG=(5,5,5)

def heart_points():
    points=[]
    cx,cy=W//2,H//2
    scale=min(W,H)//45

    def make_points(x,y,target):
        return{
            "x":x,
            "y":y,
            "target":target,
            "alpha":0,
            "delay":random.uniform(0,7000)

        }
    for i in range(180):
        t=(i/180)*math.pi*2
        x=16*math.pow(math.sin(t),3)
        y=-(13*math.cos(t)-5*math.cos(2*t)-2*math.cos(3*t)-math.cos(4*t))
        points.append(make_points(cx+x*scale,cy+y*scale,random.uniform(80,180)))

    for s in[0.2,0.4,0.6,0.8]:
        for i in range(80):
            t = (i / 80) * math.pi * 2
            x = 16 * math.pow(math.sin(t), 3)
            y = -(13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3*t) - math.cos(4*t))
            points.append(make_points(cx + x * scale*s, cy + y * scale*s, random.uniform(80, 180)))

    return points
points=heart_points()
start_trick=pygame.time.get_ticks()

while True:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:

            points=heart_points()
            start_trick=pygame.time.get_ticks()

    elapsed_time=pygame.time.get_ticks()-start_trick
    screen.fill(BG)

    for p in points:
        if elapsed_time>p["delay"]:
            p["alpha"] +=(p["target"]-p["alpha"])*.004

        alpha=int(p["alpha"])
        if alpha>0:
            surface=font.render(TEXT,True,PINK)
            surface.set_alpha(alpha)
            screen.blit(surface,(p["x"]-surface.get_width()//2,p["y"]-surface.get_height()//2))



    pygame.display.flip()
    clock.tick(60)


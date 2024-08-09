import pygame
from pygame.locals import *
import sys
import time
from datetime import date
import os

os.environ["DISPLAY"] = ":0.1"

pygame.init()
screen = pygame.display.set_mode((1920, 1080), pygame.NOFRAME)
pygame.display.set_caption('Clock')
font = pygame.font.Font(None, 120)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    title = 'Alistairs test clock'
    current_time = time.strftime("%H:%M:%S")
    today = date.today().strftime("%d-%m-%Y")
    
    time_text = font.render(current_time, True, (255, 255, 255))
    date_text = font.render(str(today), True, (255, 150, 150))
    title_text = font.render(str(title), True, (150, 150, 150))
    screen.blit(time_text, (800, 400))
    screen.blit(date_text, (730, 300))
    screen.blit(title_text,(600, 200))
    pygame.display.flip()
    time.sleep(1)

import pygame
from pygame.constants import K_ESCAPE, KEYDOWN, QUIT
import random
import time
from math import *
import pandas as pd

pygame.init()
window = pygame.display.set_mode((600,600))

sound_1 = pygame.mixer.Sound("C:\\Users\\SWAPNIL\\Desktop\\my project\\codeing challenge\\my game\\sound_2.mp3")

arrow_color = (0,0,0)
shooter_color = (0,0,0)
circle_color = (0,0,0)
text_color = (255,0,0)
background_color = (255,255,255)
level_number = 1
arrow_list = [180,25]

cen_x = 300
cen_y = 200
r = 100


window.fill(background_color)
pygame.draw.circle(window,((circle_color)),(cen_x,cen_y),100)
pygame.draw.circle(window,(shooter_color),(cen_x,cen_y+350),25)
pygame.display.flip() 

def circle_list():
    position_list = []
    for i in range(360):
        x = cen_x + r * sin(i*(pi/180))
        y = cen_y + r * cos(i*(pi/180)) * (-1) 
        position_list.append((x,y))
    line_position = []
    r_line = r + 50
    for i in range(360):
        x = cen_x + r_line * sin(i*(pi/180))
        y = cen_y + r_line * cos(i*(pi/180)) * (-1) 
        line_position.append((x,y))
    return position_list,line_position


position_list,line_position = circle_list()
x_1 = position_list[180][0]
y_1 = position_list[180][1]

arrow_list = [180]

def game_over():
    global running
    list_1 = arrow_list
    list_2 = []
    for i in range(len(list_1)):
        for j in range(2,6):
            list_2.append(list_1[i]+j)
            list_2.append(list_1[i]-j)
        if(list_1[i] in list_2):
            font = pygame.font.SysFont('arial',60)
            score = font.render("GAME OVER",True,(255,0,0))
            window.blit(score,(100,250))
            pygame.display.flip()  
            time.sleep(1)
            running= False
#comment
def game_win():
    global running
    if(counter == 0):
        font = pygame.font.SysFont('arial',60)
        score = font.render(f"YOU ARE WIN",True,(255,0,0))
        window.blit(score,(100,250))
        pygame.display.flip()  
        time.sleep(1)
        running = False

def rotate_circle(rotation):
    global start_pos
    if(rotation == 1):
        position_list.insert(0,position_list[359])
        line_position.insert(0,line_position[359])
        del position_list[-1]
        del line_position[-1]
        start_pos = position_list.index((x_1,y_1))
    else:
        position_list.insert(359,position_list[0])
        line_position.insert(359,line_position[0])
        del position_list[0]
        del line_position[0]
        start_pos = position_list.index((x_1,y_1))
    
    window.fill(background_color)
    pygame.draw.circle(window,((circle_color)),(cen_x,cen_y),100)
    pygame.draw.circle(window,(shooter_color),(cen_x,cen_y+350),25)
    font = pygame.font.SysFont('arial',50)
    score = font.render(f"{counter}",True,(text_color))
    window.blit(score,(cen_x-25,cen_y-25))
    for i in range(len(arrow_list)):
        pygame.draw.circle(window,(arrow_color),((position_list[arrow_list[i]][0],position_list[arrow_list[i]][1])),1)
        pygame.draw.circle(window,(arrow_color),((line_position[arrow_list[i]][0],line_position[arrow_list[i]][1])),5)
        pygame.draw.line(window,(arrow_color),[position_list[arrow_list[i]][0],position_list[arrow_list[i]][1]],[line_position[arrow_list[i]][0],line_position[arrow_list[i]][1]])
    pygame.display.flip()


counter = 15
FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if(pygame.mouse.get_pressed()[0]):  
                x,y = pygame.mouse.get_pos()
                if(window.get_at((x,y))==(shooter_color) and y >=475):
                    arrow_list.append(start_pos)
                    counter = counter - 1
                    sound_1.play()
    
    time.sleep(0.02)
    rotate_circle(rotation=1)
    game_over()
    game_win()
    pygame.display.flip()
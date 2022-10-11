import random
import pygame
from snake import SnakeGame

environment = SnakeGame()

@environment.register_ai
def super_ai():

    apple = environment.get_apple_position()
    snake = environment.get_snake_head_position()

    if(snake[0] < apple[0]): #Go right if move is legal
        if environment.is_legal('right'): #Check if move is legal
            return 'right'
    if(snake[0] > apple[0]): #Go left if move is leg  al
        if environment.is_legal('left'): #Check if move is legal
            return 'left'
    if(snake[1] > apple[1]): #Go up if move is leg  al
        if environment.is_legal('up'): #Check if move is legal
            return 'up'
    if(snake[1] < apple[1]): #Go down if move is leg  al
        if environment.is_legal('down'): #Check if move is legal
            return 'down'
    
    if environment.is_legal('right'): #Check if move is legal
            return 'right'
    if environment.is_legal('left'): #Check if move is legal
            return 'left'
    if environment.is_legal('up'): #Check if move is legal
            return 'up'
    if environment.is_legal('down'): #Check if move is legal
            return 'down'
    

    

environment.start(use_ai=True)



#import pygame
#from ikt111_games import Snake
#import random

#env = Snake()
#@environment.register_ai
#def super_ai():
#    apple = env.get_apple_position()
#    snake = env.get_snake_head_position()
#    
#    if(snake[0]<apple[0]): #Go right if move is legal
#        if environment.is_legal('right')): #Check if move is legal
#            return 'right'
#    
#environment.start(use_ai=True)
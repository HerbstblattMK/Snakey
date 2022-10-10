import random
from snake import SnakeGame

snake = SnakeGame()

@snake.register_ai
def super_ai():
    return [random.choice(['up', 'down', 'left', 'right'])]

snake.start(use_ai=True)



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
import  pygame
from math import inf

class Node():
    def __init__(self,x,y,length,height,x_i=None,y_i=None):
        self.rect = pygame.Rect(x,y,length,height)
        self.wall = False
        self.is_start = False
        self.is_end = False
        self.x = x_i
        self.y = y_i
        self.neighbours = []
        self.visited = False
        self.heuristic = inf
        self.prev_node = None
        self.in_path = False
    
    def __repr__(self):
        return f'heuristic: {self.heuristic}'


    def detect_clicked_mouse_collision(self, mouse_pos, is_clicked):
        if self.rect.collidepoint(mouse_pos) and is_clicked:
            return True
   
    def find_neighbours(self,grid):
        # adding horizontal neighbours
        if self.x - 1 >= 0:
            # left
            self.neighbours.append(grid[self.y][self.x-1])
        else:
            self.neighbours.append(None)
        if self.x + 1 < len(grid[0]):
            # right
            self.neighbours.append(grid[self.y][self.x+1])
        else:
            self.neighbours.append(None)
        # adding vertical neighbours
        if self.y - 1 >= 0:
            # up
            self.neighbours.append(grid[self.y-1][self.x])
        else:
            self.neighbours.append(None)
        if self.y + 1 < len(grid):
            # down
            self.neighbours.append(grid[self.y+1][self.x])
        else:
            self.neighbours.append(None)

        

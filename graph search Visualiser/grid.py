import pygame, time
from node import Node
from options_menu import OptionsMenu
from search import Search
import datetime



# colours: 
grey_blue = (104,118,129)
light_grey_blue = (119,136,153)
slategrey = (112,128,140)
dark_slategrey = (110,125,135)
ivory = (255,255,240)
dark_ivory = (250,250,235)
red = (255,0,0)
green = (0,255,0)
grey = (128,128,128)
white = (255,255,255)
teal = (0,128,128)
aquamarine = (127,255,212)
mediumseagreen = (60,179,113)



# setting up the grid
    # need to be done:
        # mouse collision to toggle wall on/off on a node -- DONE -> improve functionality once project finished

class Grid():
    def __init__(self,screen):
        self.screen = screen        
        self.grid = []
        self.menu = None
        self.player_node = None
        # initilaising grid
        y_i = 0
        for y in range(70,600,15):
            row = []
            x_i = 0
            for x in range(0,600,15):
                row.append(Node(x,y,15,15,x_i,y_i))
                x_i += 1
            self.grid.append(row)
            y_i += 1
        self.is_clicked = False
        self.start_node = None
        self.end_node = None
        self.visulise = False

    def find_neighbours(self):
        for row in self.grid:
            for node in row:
                node.find_neighbours(self.grid)

    def draw_grid(self):
        for row in self.grid:
            for node in row:
                if node.is_start:
                    pygame.draw.rect(self.screen,red,node)
                elif node.is_end:
                    pygame.draw.rect(self.screen, green, node)
                elif node.wall:
                    pygame.draw.rect(self.screen,white,node)
                elif node.in_path:
                    pygame.draw.rect(self.screen,aquamarine,node)
                elif node.visited:
                    pygame.draw.rect(self.screen,teal,node)
                if self.player_node != None:
                    pygame.draw.rect(self.screen, mediumseagreen, self.player_node)
                

                pygame.draw.rect(self.screen,slategrey,node,width=1)  
        pygame.display.flip() 

    def build_wall(self):
        for row in self.grid:
            for node in row:
                if node.detect_clicked_mouse_collision(pygame.mouse.get_pos(), self.is_clicked):
                    node.wall = True

    def remove_wall(self):
         for row in self.grid:
            for node in row:
                if node.detect_clicked_mouse_collision(pygame.mouse.get_pos(), self.is_clicked):
                    node.wall = False

    def clear(self):
        for row in self.grid:
            for node in row:
                node.wall = False
    
    def set_start_point(self):
        for row in self.grid:
            for node in row:
                if node.detect_clicked_mouse_collision(pygame.mouse.get_pos(),self.is_clicked):
                    node.is_start = True
                    if self.start_node:
                        self.start_node.is_start = False
                    self.start_node = node 
                    self.menu.setting_start = False      
            
    def set_end_point(self):
        for row in self.grid:
            for node in row:
                if node.detect_clicked_mouse_collision(pygame.mouse.get_pos(),self.is_clicked):
                    node.is_end = True
                    if self.end_node:
                        self.end_node.is_end = False
                    self.end_node = node 
                    self.menu.setting_end = False

    def return_selected_node(self):
        for row in self.grid:
            for node in row:
                if node.detect_clicked_mouse_collision(pygame.mouse.get_pos(), self.is_clicked):
                    return node

    def user_solve(self):
        finished = False
        self.player_node = self.start_node
        
        t_start = datetime.datetime.now()
        t_end = None
        while not finished:
            if type(self.player_node )is None:
                break
            self.player_node.visited = True
            for event in pygame.event.get():
                if event.type == pygame.quit:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.player_node = None
                        finished = True
                if self.player_node.is_end:
                    t_end = datetime.datetime.now()
                    finished = True
                    self.player_node = None
                    print(f'took you {t_end-t_start} to complete the maze')
                    return t_end - t_start
                    
                # movement logic
                # neighbours order: [0]Left [1]Right [2]Up [3]Down
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if self.player_node.neighbours[2] != None  and not self.player_node.neighbours[2].wall:
                            self.player_node =  self.player_node.neighbours[2]
                    elif event.key == pygame.K_DOWN:
                        if self.player_node.neighbours[3] != None  and not self.player_node.neighbours[3].wall:
                            self.player_node = self.player_node.neighbours[3]
                    elif event.key == pygame.K_LEFT:
                        if self.player_node.neighbours[0] != None and not self.player_node.neighbours[0] .wall:
                            self.player_node = self.player_node.neighbours[0]
                    elif event.key == pygame.K_RIGHT :
                        if self.player_node.neighbours[1] != None and not self.player_node.neighbours[1] .wall:
                            self.player_node = self.player_node.neighbours[1]

            self.menu.render_menu()
            self.draw_grid()
        

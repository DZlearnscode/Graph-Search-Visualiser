import pygame
from node import Node
import time
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

# Visualiser options

# Visualiser menu rect:
    # search options:
        #bfs_toggler = pygame.Rect((bfs_toggler_loc),bfs_length,bfs_hight)
        #dfs_toggler = pygame.Rect((bfs_toggler_loc),bfs_length,bfs_hight)
        #a_star_toggler = pygame.Rect((bfs_toggler_loc),bfs_length,bfs_hight))
    # build wall toggler -- DONE
    # auto generated maze -- 
    # search visualiser toggler --> show the process of finding the path -- increases the time taken if on
    # set start and end point -- DONE
    # clear walls -- DONE
    
class OptionsMenu():
    def __init__(self,screen,grid,font):
        self.screen = screen
        self.font = font  
        self.grid = grid

        self.options_rect = pygame.Rect(0,0,600,70)  
    # clear
        self.clear_walls_node = Node(500,15,15,15)
        self.clear_walls_text = self.font.render('clear walls', False, ivory)
    # build
        self.build_maze_node = Node(500,35,15,15)
        self.build_maze_text = self.font.render('build maze', False, ivory)
    # set start
        self.set_start_node = Node(350,15,15,15)
        self.set_start_text = self.font.render('set starting point', False, ivory)
        self.setting_start = False
    # set end 
        self.set_end_node = Node(350,35,15,15)
        self.set_end_text = self.font.render('set end point', False, ivory)
        self.setting_end = False
    # build wall
        self.build_walls_node = Node(220,15,15,15)
        self.build_walls_text = self.font.render('build walls', False, ivory)
        self.build = False
    # build walls
        self.rm_walls_node = Node(220,35,15,15)
        self.rm_walls_text = self.font.render('remove walls', False, ivory)
        self.remove = False
    # bfs
        self.BFS_node = Node(160,15,15,15)
        self.BFS_text = self.font.render('BFS', False, ivory)
        self.BFS = False
    # dfs
        self.DFS_node = Node(160,35,15,15)
        self.DFS_text = self.font.render('DFS', False, ivory)
        self.DFS = False
    # A star
        self.A_star_node = Node(80,15,15,15)
        self.A_star_text = self.font.render('A star', False, ivory)
        self.A_star = False
    # visulise
        self.visulise_node = Node(80,35,15,15)
        self.visulise_text = self.font.render('visulise', False, ivory)
    # run
        self.run_node = Node(15,15,15,15)
        self.run_text = self.font.render('RUN', False, ivory)
        self.running = False
    # let user solve the maze
        self.solve_node = Node(15,35,15,15)
        self.solve_text = self.font.render('SOLVE', False, ivory)



    def render_menu(self):
        # rendering menu bar
        pygame.draw.rect(self.screen, light_grey_blue, self.options_rect)
        # rendering clear walls
        pygame.draw.rect(self.screen, dark_ivory, self.clear_walls_node)
        self.screen.blit(self.clear_walls_text, (520,10))
        # rendering build maze
        pygame.draw.rect(self.screen, dark_ivory, self.build_maze_node)
        self.screen.blit(self.build_maze_text, (520,30))
        # rendering set start point
        if self.setting_start:
            pygame.draw.rect(self.screen, grey, self.set_start_node)
        else:
            pygame.draw.rect(self.screen, dark_ivory, self.set_start_node)
        self.screen.blit(self.set_start_text, (370,10))
        # rendering set end point 
        if self.setting_end:
            pygame.draw.rect(self.screen, grey, self.set_end_node)
        else:
            pygame.draw.rect(self.screen, dark_ivory, self.set_end_node)
        self.screen.blit(self.set_end_text, (370,30))
        # rendring build walls 
        if self.build:
            pygame.draw.rect(self.screen, grey, self.build_walls_node)
        else:
            pygame.draw.rect(self.screen, dark_ivory, self.build_walls_node)
        self.screen.blit(self.build_walls_text, (240,10))
        # rendering remove walls
        if self.remove:
            pygame.draw.rect(self.screen, grey, self.rm_walls_node)
        else:
            pygame.draw.rect(self.screen, dark_ivory, self.rm_walls_node)
        self.screen.blit(self.rm_walls_text, (240,30))
        # render search options
        if self.BFS:
            pygame.draw.rect(self.screen, grey, self.BFS_node)
            pygame.draw.rect(self.screen, dark_ivory, self.DFS_node)
            pygame.draw.rect(self.screen, dark_ivory, self.A_star_node)
        elif self.DFS:
            pygame.draw.rect(self.screen, grey, self.DFS_node)
            pygame.draw.rect(self.screen, dark_ivory, self.BFS_node)
            pygame.draw.rect(self.screen, dark_ivory, self.A_star_node)
        elif self.A_star:
            pygame.draw.rect(self.screen, grey, self.A_star_node)
            pygame.draw.rect(self.screen, dark_ivory, self.BFS_node)
            pygame.draw.rect(self.screen, dark_ivory, self.DFS_node)
        else:
            pygame.draw.rect(self.screen, dark_ivory, self.A_star_node)
            pygame.draw.rect(self.screen, dark_ivory, self.BFS_node)
            pygame.draw.rect(self.screen, dark_ivory, self.DFS_node)
        # render search option text    
        self.screen.blit(self.BFS_text,(180,10))
        self.screen.blit(self.DFS_text,(180,30))
        self.screen.blit(self.A_star_text,(100,10))
        # render run button
        pygame.draw.rect(self.screen, dark_ivory, self.run_node)
        self.screen.blit(self.run_text, (35,12))
        # render visuliser button
        if self.grid.visulise:
            pygame.draw.rect(self.screen, grey, self.visulise_node)
        else:
            pygame.draw.rect(self.screen, dark_ivory, self.visulise_node)
        self.screen.blit(self.visulise_text, (100,30))
        # render human solve option
        if self.grid.player_node != None:
            pygame.draw.rect(self.screen, grey, self.solve_node)
        else:
            pygame.draw.rect(self.screen, dark_ivory, self.solve_node)
        self.screen.blit(self.solve_text, (35,32))




    def visulise(self):
        if self.visulise_node.detect_clicked_mouse_collision(pygame.mouse.get_pos(), self.grid.is_clicked):
            self.grid.visulise = not self.grid.visulise
            self.grid.is_clicked = False
            self.warnning()
        
    def solve(self):
        if self.solve_node.detect_clicked_mouse_collision(pygame.mouse.get_pos(), self.grid.is_clicked):
            self.grid.continue_clicked = False
            return True

    def warnning(self):
        pygame.draw.rect(self.screen, grey_blue, self.options_rect)
        text = self.font.render("Visulising the algorithm's search steps might hurt performance...",False,dark_ivory)
        self.screen.blit(text,(75,25))
        pygame.display.flip()
        self.grid.draw_grid()
        time.sleep(2)
        
        

    def run(self):
        if self.run_node.detect_clicked_mouse_collision(pygame.mouse.get_pos(), self.grid.is_clicked):
            print("running...")
            return True

    def choose_serach(self):
        if self.A_star_node.detect_clicked_mouse_collision(pygame.mouse.get_pos(), self.grid.is_clicked):
            self.A_star = not self.A_star 
            self.DFS = False
            self.BFS = False
            self.grid.is_clicked = False
        elif self.DFS_node.detect_clicked_mouse_collision(pygame.mouse.get_pos(), self.grid.is_clicked):
            self.DFS = not self.DFS
            self.BFS = False   
            self.A_star = False 
            self.grid.is_clicked = False
        elif self.BFS_node.detect_clicked_mouse_collision(pygame.mouse.get_pos(), self.grid.is_clicked):
            self.BFS = not self.BFS
            self.A_star = False 
            self.DFS = False
            self.grid.is_clicked = False

    def build_maze(self):
        if self.build_maze_node.detect_clicked_mouse_collision(pygame.mouse.get_pos(), self.grid.is_clicked):
            self.grid.continue_clicked = False
            return True

    def clear_clicked(self):
        if self.clear_walls_node.detect_clicked_mouse_collision(pygame.mouse.get_pos(),self.grid.is_clicked):
            for row in self.grid.grid:
                for node in row:
                    node.wall = False
                    node.is_start = False
                    node.is_end = False 
                    node.visited = False
                    node.in_path = False

    def set_start(self):
        if self.set_start_node.detect_clicked_mouse_collision(pygame.mouse.get_pos(),self.grid.is_clicked):
            self.setting_start = not self.setting_start
            self.setting_end = False
            self.grid.is_clicked = False 
            return

    def set_end(self,):
        if self.set_end_node.detect_clicked_mouse_collision(pygame.mouse.get_pos(),self.grid.is_clicked):
            self.setting_end = not self.setting_end 
            self.setting_start = False
            self.grid.is_clicked = False
            return

    def build_walls(self):
        if self.build_walls_node.detect_clicked_mouse_collision(pygame.mouse.get_pos(), self.grid.is_clicked):
            self.build = not self.build
            self.remove = False
            self.grid.is_clicked = False

    def remove_walls(self):
        if self.rm_walls_node.detect_clicked_mouse_collision(pygame.mouse.get_pos(),self.grid.is_clicked):
            self.remove = not self.remove  
            self.build = False
            self.grid.is_clicked = False

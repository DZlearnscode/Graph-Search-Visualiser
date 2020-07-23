import  pygame
from node import Node
from grid import Grid
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

# pygame initialisations 
pygame.init()
pygame.font.init()
pygame.display.set_caption('Graph Search Visualiser')

screen = pygame.display.set_mode((600,610))
screen.fill((250,250,250))

grid = Grid(screen)
grid.find_neighbours()
menu = OptionsMenu(screen, grid, pygame.font.SysFont('Comic Sans MS',13))
grid.menu = menu
search = Search(grid)


def user_solve():

        finished = False
        grid.player_node = grid.start_node
        t_start = datetime.datetime.now()
        t_end = None
        while not finished:
            grid.player_node.visited = True
            for event in pygame.event.get():
                if event.type == pygame.quit:
                    #pygame.quit()
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        grid.player_node = None
                        finished = True
                        return
                if grid.player_node.is_end:
                    t_end = datetime.datetime.now()
                    finished = False
                    grid.player_node = None
                # movement logic
                # neighbours order: [0]Up [1]Down [2]Left [3]Right
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        grid.player_node = grid.player_node.neighbours[2]
                    elif event.key == pygame.K_RIGHT:
                        grid.player_node = grid.player_node.neighbours[3]
                    elif event.key == pygame.K_UP:
                        grid.player_node =  grid.player_node.neighbours[0]
                    elif event.key == pygame.K_DOWN:
                        grid.player_node = grid.player_node.neighbours[1]
            menu.render_menu()
            #grid.draw_grid()
        print(f'took you {t_end-t_start} to complete the maze')


on = True

while on:
    screen.fill((grey_blue))
    menu.render_menu()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                grid.is_clicked = False  
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                grid.is_clicked = True   
         
    if menu.setting_start:
        grid.set_start_point()

    elif menu.setting_end:
        grid.set_end_point()

    if menu.build:
        grid.build_wall()

    elif menu.remove:
        grid.remove_wall()

    if menu.run():
        for row in grid.grid:
            for node in row:
                node.visited = False
                node.in_path = False 
        if menu.BFS:
            search.BFS(grid.start_node, grid.end_node)
        elif menu.DFS:
            search.DFS(grid.start_node, grid.end_node)
        elif menu.A_star:
            search.a_star(grid.start_node, grid.end_node)
            
            

# call back function for menu options
    menu.choose_serach()
    menu.build_walls()
    menu.remove_walls()
    menu.set_start()
    menu.set_end()
    menu.visulise()
    menu.clear_clicked()
    menu.choose_serach()

    if menu.solve():
        grid.user_solve()
        
    if menu.build_maze():
        start_node, end_node = search.build_maze()
        grid.start_node = start_node
        grid.end_node = end_node
    

    grid.draw_grid()



    pygame.display.flip()



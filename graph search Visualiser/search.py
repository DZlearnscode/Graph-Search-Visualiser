from math import sqrt
from min_heap import Heap
from random import randint
import sys
import datetime 
import time

# increasing recursion limit 
sys.setrecursionlimit(5000)

class Search():
    def __init__(self, grid):
        self.grid = grid
        self.heap = Heap()

    def heuristic(self, current, target):
        start = self.grid.start_node
        x_distance_to_end = abs(current.x - target.x)
        y_distance_to_end = abs(current.y - target.y)
        distance_to_end = sqrt(x_distance_to_end**2 + y_distance_to_end**2)
        x_distance_from_start = abs(current.x - start.x)
        y_distance_from_start = abs(current.y - start.y)
        distance_from_start = sqrt(x_distance_from_start + y_distance_from_start)
        return distance_to_end + distance_from_start

    def build_maze(self):
        # prapring grid for carving a maze
        for row in self.grid.grid:
            for node in row:
                node.wall = True
                node.is_start = False
                node.is_end = False
                node.visited = False
                node.in_path = False
        # choose random starting point
        start_node = self.grid.grid[randint(0, (len(self.grid.grid)-1))][randint(0, (len(self.grid.grid[0])-1))]
        end_node = self.grid.grid[randint(0, (len(self.grid.grid)-1))][randint(0, (len(self.grid.grid[0])-1))]
        start_node.wall = False
        start_node.is_start = True
        end_node.wall = False
        end_node.is_end = True  
        # recursive call trigger to remove walls and create paths in the maze
        self.remove_walls(start_node)
        return start_node, end_node 

    def remove_walls(self,node): 
        # neighbours order: [0]Up [1]Down [2]Left [3]Right
        directions = ["U","D","L","R"]
        while (len(directions) > 0):
            direction = directions.pop(randint(0, len(directions)-1))    
            if direction == 'L':
                if node.y - 2 < 0:
                    continue
                elif self.grid.grid[node.y - 2][node.y].wall:
                    self.grid.grid[node.y - 1][node.x].wall = False
                    self.grid.grid[node.y - 2][node.x].wall = False
                    self.remove_walls(self.grid.grid[node.y-2][node.x])
            elif direction == 'R':
                if node.y + 2 >= len(self.grid.grid):
                    continue
                elif self.grid.grid[node.y + 2][node.x].wall:
                    self.grid.grid[node.y + 1][node.x].wall = False
                    self.grid.grid[node.y + 2][node.x].wall = False
                    self.remove_walls(self.grid.grid[node.y + 2][node.x])
            elif direction == 'U':
                if node.x - 2 < 0:
                    continue
                elif self.grid.grid[node.y][node.x-2].wall:
                    self.grid.grid[node.y][node.x-1].wall = False
                    self.grid.grid[node.y][node.x-2].wall = False
                    self.remove_walls(self.grid.grid[node.y][node.x - 2])
            else:
                if node.x + 2 >= len(self.grid.grid[0]):
                    continue
                elif self.grid.grid[node.y][node.x+2].wall:
                    self.grid.grid[node.y][node.x+1].wall = False
                    self.grid.grid[node.y][node.x+2].wall = False
                    self.remove_walls(self.grid.grid[node.y][node.x + 2])
        
    def BFS(self,start_node,end_node):
        bfs_queue = [start_node]
        t_start = datetime.datetime.now()
        while bfs_queue:
            node = bfs_queue.pop(0)
            node.visited = True
            if self.grid.visulise:
                self.grid.draw_grid()
            if node.is_end:
                t_end = datetime.datetime.now()
                print(f'it took BFD {t_end-t_start} seconds to find the target node')
                self.reconstract_path(end_node)
                return t_end - t_start
            for neighbour in node.neighbours:
                if neighbour != None:
                    if not neighbour.wall and not neighbour.visited:
                        bfs_queue.append(neighbour)
                        neighbour.prev_node = node
                
                    
    def DFS(self,start_node,end_node):
        dfs_stack = [start_node]
        t_start = datetime.datetime.now()
        while dfs_stack:
            node = dfs_stack.pop()
            node.visited = True
            if self.grid.visulise:
                self.grid.draw_grid()
            if node.is_end:
                t_end = datetime.datetime.now()
                print(f'it took DFD {t_end-t_start} seconds to find the target node')
                self.reconstract_path(end_node)
                return t_end - t_start
            for neighbour in node.neighbours:
                if neighbour != None:
                    if not neighbour.wall and not neighbour.visited:        
                        dfs_stack.append(neighbour) 
                        neighbour.prev_node = node


    def a_star(self,start_node,end_node):
        heap = Heap()
        for neighbour in start_node.neighbours:
            if not neighbour.wall and neighbour != None:
                neighbour.heuristic = self.heuristic(neighbour,end_node)
                heap.push(neighbour)
                neighbour.prev_node = start_node
        t_start = datetime.datetime.now()
        while heap.count > 0:
            current_node = heap.pop()
            current_node.visited = True
            if self.grid.visulise:
                self.grid.draw_grid()
            if current_node.is_end:
                t_end = datetime.datetime.now()
                print(f'it took A* {t_end-t_start} seconds to find the target node')
                self.reconstract_path(end_node)
                return t_end-t_start
            for neighbour in current_node.neighbours:
                if neighbour != None:
                    if not neighbour.wall and not neighbour.visited:
                        neighbour.heuristic = self.heuristic(neighbour,end_node)
                        heap.push(neighbour)
                        neighbour.prev_node = current_node
                    

    # start node and end node are linked via a linked list (each node is pointing
    # to the next node in the path) - to find the shortest path, traverse backwards 
    # from the end node to the start node.
    def reconstract_path(self, node, n_steps = 0):
        prev_node = node.prev_node
        steps = n_steps
        if prev_node.is_start:
            print(f'it took {n_steps}')
            return
        prev_node.in_path = True
        steps += 1
        #time.sleep(0.05)
        self.grid.draw_grid()
        self.reconstract_path(prev_node, steps)
    
  

       
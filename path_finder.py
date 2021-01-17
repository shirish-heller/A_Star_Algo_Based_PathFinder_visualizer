import pygame
import sys
import os
import CONFIG
from queue import PriorityQueue
import math

WIN = pygame.display.set_mode((CONFIG.DIMENSION, CONFIG.DIMENSION))
pygame.display.set_caption("A* Path Finding Algo visualizer")

def make_grid():
    CONFIG.GAP = CONFIG.DIMENSION//CONFIG.ROWS
    for row in range(CONFIG.ROWS):
        for col in range(CONFIG.ROWS):
            pygame.draw.rect(WIN, CONFIG.GRAY, (row*CONFIG.GAP,col*CONFIG.GAP,CONFIG.GAP,CONFIG.GAP), 1)

def draw_start_end_and_barriers(startNodeLocation, endNodeLocation, barriersLocation):
    # drawing startNode
    if startNodeLocation:
        pygame.draw.rect(WIN, CONFIG.YELLOW, (startNodeLocation[0]*CONFIG.GAP,startNodeLocation[1]*CONFIG.GAP,CONFIG.GAP,CONFIG.GAP))
    # drawing endNode
    if endNodeLocation:
        pygame.draw.rect(WIN, CONFIG.GREEN, (endNodeLocation[0]*CONFIG.GAP,endNodeLocation[1]*CONFIG.GAP,CONFIG.GAP,CONFIG.GAP))
    # drawing barriers
    if(barriersLocation and len(barriersLocation)>0):
        for node in barriersLocation:
            pygame.draw.rect(WIN, CONFIG.BLACK, (node[0]*CONFIG.GAP,node[1]*CONFIG.GAP,CONFIG.GAP,CONFIG.GAP))

def heuristic(fromNode, toNode):
    x1,y1 = fromNode
    x2,y2 = toNode
    return math.sqrt(math.pow((abs(x2-x1)), 2) + math.pow((abs(y2-y1)), 2))

def find_neighbours(node, barriersLocation):
    x, y = node
    neighbours = []
    if((x+1, y) not in barriersLocation):
        neighbours.append((x+1, y))
    if((x-1, y) not in barriersLocation):
        neighbours.append((x-1, y))
    if((x, y+1) not in barriersLocation):
        neighbours.append((x, y+1))
    if((x, y-1) not in barriersLocation):
        neighbours.append((x, y-1))
    return neighbours

def highlight_visitedNodes(visitedNodes):
    for node in visitedNodes:
        pygame.draw.rect(WIN, CONFIG.ORANGE, (node[0]*CONFIG.GAP,node[1]*CONFIG.GAP,CONFIG.GAP,CONFIG.GAP))

def construct_optimal_path(cameFrom, endingNode, optimal_path):
    currentNode = endingNode
    while(currentNode!=None):
        parentNode = cameFrom.get(currentNode)
        if(parentNode!=None):
            optimal_path.append(parentNode)
        currentNode = parentNode


def find_optimal_path_with_AStar(startNodeLocation, endNodeLocation, barriersLocation, optimal_path):
    print("find_optimal_path_with_AStar")
    q = PriorityQueue()
    q.put((heuristic(startNodeLocation, endNodeLocation), startNodeLocation))
    visitedNodes = {}
    cost = {}
    present_in_queue_dict = {}
    cost[startNodeLocation] = 0
    cameFrom = {}
    while(not q.empty()):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        currentNodeData = q.get()
        currentNode = currentNodeData[1]
        # cost[currentNode] = (cost.get(currentNode) if cost.get(currentNode)!=None else 0) + 1
        visitedNodes[currentNode] = True
        if(currentNode == endNodeLocation):
            print("solution found")
            print(cost.get(currentNode))
            construct_optimal_path(cameFrom, currentNode, optimal_path)
            break

        neighbours = find_neighbours(currentNode, barriersLocation)
        for neighbour in neighbours:
            if(visitedNodes.get(neighbour)==None and present_in_queue_dict.get(neighbour)==None):
                q.put(( (cost.get(currentNode) + 1 + heuristic(neighbour, endNodeLocation)), neighbour) )
                present_in_queue_dict[neighbour] = True
                cameFrom[neighbour] = currentNode
                cost[neighbour] = cost.get(currentNode) + 1
        highlight_visitedNodes(visitedNodes)
        pygame.display.update()
    return False

def draw_optimal_path(optimal_path):
    for node in optimal_path:
        pygame.draw.rect(WIN, CONFIG.INDIGO, (node[0]*CONFIG.GAP,node[1]*CONFIG.GAP,CONFIG.GAP,CONFIG.GAP))

def main():
    grid = make_grid()
    isSearching = False
    startNodeLocation = False
    endNodeLocation = False
    barriersLocation = []
    optimal_path = []
    run = True
    while run:
        WIN.fill(CONFIG.WHITE)
        make_grid() # Draws the grid
        if(not isSearching):
            if pygame.mouse.get_pressed()[0]:       # Detects left mouse click
                x,y = pygame.mouse.get_pos()    # mouse coordinates where click happened
                node_coordinates = (x//CONFIG.GAP, y//CONFIG.GAP)   # x and y coordinate of grid node
                if (not startNodeLocation):
                    startNodeLocation = node_coordinates
                elif (not endNodeLocation and node_coordinates!=startNodeLocation):
                    endNodeLocation = node_coordinates
                elif node_coordinates!=startNodeLocation and node_coordinates!=endNodeLocation:
                    if node_coordinates not in barriersLocation:
                        barriersLocation.append(node_coordinates)

            if pygame.mouse.get_pressed()[2]: # Detects right mouse click
                x,y = pygame.mouse.get_pos()
                node_coordinates = (x//CONFIG.GAP, y//CONFIG.GAP)
                if startNodeLocation == node_coordinates:   # reseting start node if right clicked
                    startNodeLocation = False
                elif endNodeLocation == node_coordinates:   # reseting end node if right clicked
                    endNodeLocation = False
                elif node_coordinates in barriersLocation:  # reseting barrier node if right clicked
                    barriersLocation.remove(node_coordinates)
        
        draw_start_end_and_barriers(startNodeLocation, endNodeLocation, barriersLocation)   # Draws the start, end and barrier nodes
        # pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif(startNodeLocation and endNodeLocation and event.type == pygame.KEYDOWN and isSearching==False):
                if(event.key == pygame.K_RETURN):
                    isSearching = True
                    print(" Finding the optimal path!")
                    find_optimal_path_with_AStar(startNodeLocation, endNodeLocation, barriersLocation, optimal_path)
            elif (isSearching==True and event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_SPACE):
                    startNodeLocation = False
                    endNodeLocation = False
                    isSearching = False
                    barriersLocation = []
                    optimal_path = []

        draw_optimal_path(optimal_path)
        pygame.display.update()
    pygame.quit()

main()
import pygame
import sys
import os
import CONFIG

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

def main():
    grid = make_grid()
    isSearching = False
    startNodeSet = False
    endNodeSet = False
    startNodeLocation = None
    endNodeLocation = None
    barriersLocation = []
    run = True
    while run:
        WIN.fill(CONFIG.WHITE)
        make_grid() # Draws the grid
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:       # Detects left mouse click
                x,y = pygame.mouse.get_pos()    # mouse coordinates where click happened
                node_coordinates = (x//CONFIG.GAP, y//CONFIG.GAP)   # x and y coordinate of grid node
                if not startNodeSet:
                    startNodeSet = True
                    startNodeLocation = node_coordinates
                elif not endNodeSet:
                    endNodeSet = True
                    endNodeLocation = node_coordinates
                elif node_coordinates!=startNodeLocation and node_coordinates!=endNodeLocation:
                    barriersLocation.append(node_coordinates)

        if pygame.mouse.get_pressed()[2]: # Detects right mouse click
            x,y = pygame.mouse.get_pos()
            node_coordinates = (x//CONFIG.GAP, y//CONFIG.GAP)
            if startNodeLocation == node_coordinates:   # reseting start node if right clicked
                startNodeSet = False
                startNodeLocation = None
            elif endNodeLocation == node_coordinates:   # reseting end node if right clicked
                endNodeSet = False
                endNodeLocation = None
            elif node_coordinates in barriersLocation:  # reseting barrier node if right clicked
                barriersLocation.remove(node_coordinates)

        draw_start_end_and_barriers(startNodeLocation, endNodeLocation, barriersLocation)   # Draws the start, end and barrier nodes
        pygame.display.update()
    pygame.quit()
    sys.exit

main()
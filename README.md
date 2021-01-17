This is a visualizer tool where you can create a path in a grid and find shortest distance finding using the A* algo with heuristics and visualize it.
# DESIGN

## Making the visualizer and path constructor tool


## Implementing A* path finding
1. Find the valid neighbours of start node (ignore barriers).
2. Calculate the G(n) value for each neighbour (which will be 1 + heuristic value).
3. Add all the valid neighbours to priority queue with their G value.
4. Pop the top node from priority queue (will have smallest G). Repeat steps 2, 3,4 thereafter.
5. For each node save where you came from to that node (this will help to reconstruct path later)
6. Stop if you find the goal node in between.
7. Reconstruct the optimal path using the came from info and return
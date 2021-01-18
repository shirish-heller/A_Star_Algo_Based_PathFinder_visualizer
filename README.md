This is a visualizer tool where you can create a path in a grid and find shortest distance finding using the A-Star algo with heuristics and visualize it.
# Screenshots
<div>
<span>
<img src="https://user-images.githubusercontent.com/16266951/104873816-637c4180-5977-11eb-92f2-4dedcf6a01b1.png" data-canonical-src="https://gyazo.com/eb5c5741b6a9a16c692170a41a49c858.png" width="280" height="280" />
<img src="https://user-images.githubusercontent.com/16266951/104873240-0e8bfb80-5976-11eb-9a48-fc404fda20d2.png" data-canonical-src="https://gyazo.com/eb5c5741b6a9a16c692170a41a49c858.png" width="280" height="280" />
<img src="https://user-images.githubusercontent.com/16266951/104873612-efda3480-5976-11eb-9390-35b9afdc436c.png" data-canonical-src="https://gyazo.com/eb5c5741b6a9a16c692170a41a49c858.png" width="280" height="280" />
</span>
<img src="https://user-images.githubusercontent.com/16266951/104874339-b73b5a80-5978-11eb-84b8-5b57632ed3fb.png" data-canonical-src="https://gyazo.com/eb5c5741b6a9a16c692170a41a49c858.png" width="280" height="280" />
</span> 
</div>

# INSTRUCTIONS TO USE
    1. Click anywhere on the grid to selet your Start Node (Yellow)
    2. Click again anywhere on the grid to select the Goal Node (Green)
    3. All the click after this will make Barriers on the grid (Black)
    4. If you want to change any node (start, goal or barrier) just right click on the same to erase
    5. Once you are happy, Press ENTER to trigger the A-Star path finding process
    6. Press ** SPACE ** to clear all and restart

# TRY IT HERE
   [Run It here!!](https://repl.it/@ShivanshRajolia/A)

# DESIGN

## Making the visualizer and path constructor tool
1. Code a game loop (this code will run every frame)
2. Setup a quit mechanism to exit from game loop (cross button)
3. Draw a grid with the config dimensions/rows (should be configurable)
4. On 1st left click we will get the start Node pos. Save it and make sure it glows on each game loop
5. Do the same for the 2nd left click but this time save it as Goal Node. This will also glow each game loop
6. Each left click after that is a barrier so store the pos in some arr and make sure it glows each GL
7. On right click it should be able to erase the selected node (start/end/barrier) to white and reset it.
8. Setup listeners for ENTER and SPACE to start algo and clear all respectively

## Implementing A* path finding
1. Find the valid neighbours of start node (ignore barriers).
2. Calculate the G(n) value for each neighbour (which will be 1 + heuristic value).
3. Add all the valid neighbours to priority queue with their G value.
4. Pop the top node from priority queue (will have smallest G). Repeat steps 2, 3,4 thereafter.
5. For each node save where you came from to that node (this will help to reconstruct path later)
6. Stop if you find the goal node in between.
7. Reconstruct the optimal path using the came from info and return

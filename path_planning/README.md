# Path Planning Algorithms Implementation

This file contains Python implementations of both the breadth-first search (BFS) and depth-first search (DFS) algorithms for path planning on a 2D grid.

## Files

- `BFS.py`: Python script containing the BFS algorithm implementation.
- `DFS.py`: Python script containing the DFS algorithm implementation.
- `README.md`: Documentation file explaining the codes and usage.

## Breadth-First Search (BFS) Algorithm

### Overview

The BFS algorithm finds the shortest path between a specified start and end point on a 2D grid, considering only horizontal and vertical movements.

### Implementation Details

#### Grid Traversal

- A 5x5 grid is used to represent a maze or terrain with open spaces and obstacles.
- The start and end points are marked on the grid.

#### BFS Algorithm

1. **is_valid Function:**
   - Checks if a given cell is a valid and open space on the grid.

2. **bfs Function:**
   - Performs breadth-first search to find the shortest path.
   - Utilizes a queue to explore cells in a breadth-first manner.
   - Keeps track of visited cells and records the path.

3. **print_grid Function:**
   - Prints the grid, start, end, obstacles, open spaces, and the path.

### Example

- An example grid with obstacles, start, and end points is provided.

   ![Grid map ](/imgs/BFS-GRID.jpg)


- The BFS algorithm is applied to find and print the shortest path.

   ![Grid map ](/imgs/BFS-PATH.png)

## Depth-First Search Path Planning Algorithm Implementation



### Implementation Details

#### Grid Traversal

- A 5x5 grid is used to represent a maze or terrain with open spaces and obstacles.
- The start and end points are marked on the grid.

#### DFS Algorithm

1. **is_valid Function:**
   - Checks if a given cell is a valid and open space on the grid.

2. **dfs Function:**
   - Performs depth-first search to find a path.
   - Utilizes recursion to explore neighboring cells in a depth-first manner.
   - Returns the path from the start to the end if one is found.

3. **print_grid Function:**
   - Prints the grid, start, end, obstacles, open spaces, and the path.

### Example

- An example grid with obstacles, start, and end points is provided.

    ![Grid map ](/imgs/DFS-GRID.png)

- The DFS algorithm is applied to find and print the path.

    ![Grid map ](/imgs/DFS-PATH.png)

## How to Use

1. Clone the repository:

   ```bash
   git clone https://github.com/Ibrahim-Elsayed1/ROS_Tasks.git
   ```
2. Navigate to the code directory:
   ```bash
   cd path/to/the/directory
   ```

3. Run the algorithm script:

   ```bash
   python3 BFS.py
   ```
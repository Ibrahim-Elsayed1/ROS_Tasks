from collections import deque
#This function checks whether a given cell (x, y) is a valid and open space on the grid.
def is_valid(x, y, grid):
    rows, cols = len(grid), len(grid[0])
    return 0 <= x < rows and 0 <= y < cols and grid[x][y] == 0


#This function performs a breadth-first search on the grid to find the shortest path from the start point to the end point. 
#It uses a queue to explore cells in a breadth-first manner
def bfs(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)] #The visited matrix is used to keep track of visited cells
    queue = deque([(start[0], start[1], 0, [])])  # (x, y, distance, path), The path list records the path from the start to the current cell.

    while queue:
        x, y, distance, path = queue.popleft()

        if (x, y) == end: 
            return path + [(x, y)]

        if not visited[x][y]:
            visited[x][y] = True

            # Explore neighboring cells
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny, grid):
                    queue.append((nx, ny, distance + 1, path + [(x, y)]))

    return None  # No path found

#This function is used to print the grid, start point ('S'), end point ('E'), obstacles ('#'), open spaces ('.'), and the path ('*') if provided.
def print_grid(grid, path=None):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) == start:
                print("S", end=" ")
            elif (i, j) == end:
                print("E", end=" ")
            elif path and (i, j) in path:
                print("*", end=" ")
            elif grid[i][j] == 1:
                print("#", end=" ")  
            else:
                print(".", end=" ")  
        print()

# Example grid (0 represents open space, 1 represents obstacle)
grid = [
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]

start = (0, 4)
end = (4, 4)

#Prints grid map
print("Grid:")
print_grid(grid)


path = bfs(grid, start, end)

if path:
    print("\nShortest Path:") 
    print_grid(grid, path)
else:
    print("\nNo path found.")

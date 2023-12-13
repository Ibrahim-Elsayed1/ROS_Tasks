#This function checks whether a given cell (x, y) is a valid and open space on the grid.
def is_valid(x, y, grid):
    rows, cols = len(grid), len(grid[0])
    return 0 <= x < rows and 0 <= y < cols and grid[x][y] == 0

#The dfs function is a recursive implementation of depth-first search. 
#It explores neighboring cells in a depth-first manner, backtracking when needed. 
def dfs(grid, current, end, visited, path):
    x, y = current

    if current == end:
        return path + [current]

    if not visited[x][y]:
        visited[x][y] = True

        # Explore neighboring cells in a depth-first manner
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, grid):
                result = dfs(grid, (nx, ny), end, visited, path + [current])
                if result:
                    return result

    return None

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
                print("#", end=" ")  # obstacle
            else:
                print(".", end=" ")  # open space
        print()

# Example grid (0 represents open space, 1 represents obstacle)
grid = [
    [0, 0, 0, 1, 0],
    [1, 0, 0, 1, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [0, 1, 0, 0, 0]
]

start = (0, 0)
end = (4, 4)

print("Grid:")
print_grid(grid)

visited = [[False] * len(grid[0]) for _ in range(len(grid))]
path = dfs(grid, start, end, visited, [])

if path:
    print("\nPath Found:")
    print_grid(grid, path)
else:
    print("\nNo path found.")

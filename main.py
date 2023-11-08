import random
import copy
import time

# Constants
WALL = "▓"
OPEN_SPACE = "◌"
START = "S"
END = "E"
PATH = "◍"


def generate_maze(n):
    maze = [[WALL if random.random() < 0.3 else OPEN_SPACE for _ in range(n)] for _ in range(n)]
    # maze = [[WALL if random.randrange(1, n, 1) < n/3 else OPEN_SPACE for _ in range(n)] for _ in range(n)]
    maze[0][0] = START
    maze[n - 1][n - 1] = END
    return maze


def print_maze(maze):
    for row in maze:
        print("\t".join(row))


def find_path(maze):
    def is_valid(x, y):
        return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != WALL

    stack = [(0, 0)]
    visited = set()

    while stack:
        x, y = stack[-1]

        if x == len(maze) - 1 and y == len(maze[0]) - 1:
            return stack

        found = False

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in visited and is_valid(nx, ny):
                stack.append((nx, ny))
                visited.add((nx, ny))
                found = True
                break

        if not found:
            stack.pop()

    return None


def mark_path(maze, path):
    for x, y in path:
        if maze[x][y] not in [START, END]:
            maze[x][y] = PATH


def get_user_input(prompt):
    return input(prompt)


def main():
    print("Terminal-Based Maze Solver")

    while True:
        n = int(input("Enter the size of the maze (n): "))
        # wall_percentage = float(input("Enter the wall percentage (0.0 to 1.0): "))

        maze = generate_maze(n)
        print("\nGenerated Maze:")
        print_maze(maze)

        print("\nOptions:")
        print("1. Print the path")
        print("2. Generate another puzzle")
        print("3. Exit the Game")

        option = get_user_input("Enter your choice (1/2/3): ")

        if option == '1':
            path = find_path(copy.deepcopy(maze))
            if path is not None:
                print("\nMaze with Path:")
                mark_path(maze, path)
                maze[0][0] = START
                maze[n - 1][n - 1] = END
                print_maze(maze)
            else:
                print("\nNo path found!")
        elif option == '2':
            continue
        else:
            print("Goodbye!")
            break
        print()


if __name__ == "__main__":
    main()

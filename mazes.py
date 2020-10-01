import random
import queue
class Maze:
    """
    Defines the Maze class
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = []

        for h in range(self.height):
            row = []
            for w in range(self.width):
                row.append('#')
            self.maze.append(row)

    def simple_mazes(self):
        print('Enter the width of the maze:', end=" ")
        width = int(input())
        print('Enter the height of the maze:', end=" ")
        height = int(input()) 

        if(height % 2 == 0):
            print('Height should be odd. \n\n')
            self.simple_mazes()
            return
        if(height < 5):
            print('Height should not be less than 5.\n\n')
            self.simple_mazes()
            return
        if(width < 5):
            print('Width should not be less than 5.\n\n')
            self.simple_mazes()
            return

        left = 1
        right = 1
        for h in range(height):
            for w in range(width - 1):
                if(h % 2 != 0):
                    if(w == 0 and h != 1):
                        print('#', end=" ")            
                    else:
                        print(' ', end=" ")

                if(h % 2 == 0):
                    if(h ==  (2 + (left - 1) * 4) and w == width - 2):
                        left = left + 1
                        print(' ', end=" ")
                    elif(h ==  (4 + (right - 1) * 4) and w == 1):
                        right = right + 1
                        print(' ', end=" ")
                    else:
                        print('#', end=" ")

            print('#', end=" ") 

            print('')


    def draw_maze(self):
        '''
        Draw a maze
        '''
        for h in range(self.height):
            for w in range(self.width):
                print(self.maze[h][w], end=" ")
            print()

    def generate_maze(self):
        '''
        1. Choose the initial cell, mark it as visited and push it to the stack
        2. While the stack is not empty
           1.  Pop a cell from the stack and make it a current cell
           2.  If the current cell has any neighbours which have not been visited
               1. Push the current cell to the stack
               2. Choose one of the unvisited neighbours
               3. Remove the wall between the current cell and the chosen cell
               4. Mark the chosen cell as visited and push it to the stack        
        '''

        print('Enter the width of the maze:', end=" ")
        self.width = int(input())
        print('Enter the height of the maze:', end=" ")
        self.height = int(input())

        if(self.height % 2 == 0):
            print('Height should be odd. \n\n')
            self.generate_maze()
            return
        if(self.height < 5):
            print('Height should not be less than 5.\n\n')
            self.generate_maze()
            return
        if(self.width < 5):
            print('Width should not be less than 5.\n\n')
            self.generate_maze()
            return       

        self.maze = [] 

        for h in range(self.height):
            row = []
            for w in range(self.width):
                row.append('#')
            self.maze.append(row)

        stack = []

        x = random.randint(1, self.width - 2)
        y = random.randint(1, self.height - 2)

        self.maze[y][x] = ' '
        # i = 0

        stack.append([y, x])
        self.maze[y][x] = ' '

        while(len(stack) != 0):
            y , x = stack.pop() 
            # self.maze[y][x] = ' '   
            temp_list = []
                  

            if(y - 1 >= 1 and self.maze[y - 1][x] == '#'):
                temp_list.append([y -1, x])
            if(x - 1 >= 1 and self.maze[y][x - 1] == '#'):
                temp_list.append([y , x - 1])
            if( (y + 1) < (self.height - 1) and self.maze[y + 1][x] == '#'):
                temp_list.append([y + 1 , x ])
            if( (x + 1) < (self.width - 1) and self.maze[y][x + 1] == '#'):
                temp_list.append([y , x + 1])
            
            if(len(temp_list) > 1):
                stack.append([y,x])
                y,x = temp_list[random.randint(0, len(temp_list) - 1)]
            
                self.maze[y][x] = ' '  
                stack.append([y,x])

            # self.draw_maze()
            print("")


    def maze_solver(self):
        store = queue.Queue()
        store.put("")
        add = ""
        
        self.maze[1][1] = "x"
        self.maze[self.height - 2][self.width - 2] = "o"
        maze = self.maze
        self.draw_maze()
        print("")
        while not self.find_exit(add):
            add = store.get()
            for j in ["L", "R", "U", "D"]:
                put = add + j
                if self.is_path_valid( put):
                    store.put(put)


    def create_maze(self):
        self.maze = []
        self.maze.append(["#", "#", "#", "#", "#", "#", "#"])
        self.maze.append(["x", " ", "#", " ", " ", " ", "#"])
        self.maze.append(["#", " ", "#", " ", " ", " ", "#"])
        self.maze.append(["#", " ", " ", " ", " ", " ", "#"])
        self.maze.append(["#", " ", "#", "#", "#", " ", "#"])
        self.maze.append(["#", " ", " ", " ", "#", "o", "#"])
        self.maze.append(["#", "#", "#", "#", "#", "#", "#"])
        # return maze

    def print_solved_maze(self, path=""):
        i,j = 0,0
        for h, row in enumerate(self.maze):
            for x , value in enumerate(row):
                if(value == 'o'):
                    i = x
                    j = h

        pos = set()
        for move in path: 
            if move == "L":
                i -= 1 
            elif move == "R":
                i += 1
            elif move == "U":
                j -= 1
            elif move == "D":
                j += 1
            pos.add((j, i))
            
        for j, row in enumerate(self.maze):
            for i, col in enumerate(row):
                if(j, i) in pos:
                    print("+ ",end="")
                else:
                    print(col + " ", end="")
            print()
        

    def is_path_valid(self, moves):
        i,j = 0,0
        for h, row in enumerate(self.maze):
            for x , value in enumerate(row):
                if(value == 'o'):
                    i = x
                    j = h

        for move in moves: 
            if move == "L":
                i -= 1 
            elif move == "R":
                i += 1
            elif move == "U":
                j -= 1
            elif move == "D":
                j += 1
            if not(0 <= i < len(self.maze[0]) and 0 <= j < len(self.maze)):
                return False
            elif (self.maze[j][i] == "#"):
                return False
        return True

    def find_exit(self, moves):
        i,j = 0,0
        for h, row in enumerate(self.maze):
                for x , value in enumerate(row):
                    if(value == 'o'):
                        i = x
                        j = h

        for move in moves: 
            if move == "L":
                i -= 1 
            elif move == "R":
                i += 1
            elif move == "U":
                j -= 1
            elif move == "D":
                j += 1
        if self.maze[j][i] == "x":

            self.print_solved_maze(moves)
            return True

        return False 





    def menu(self):
        '''
        Maze Game loop
        '''
        print("                                                                         ")
        print("                                                                         ")
        print(" █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ ")
        print("                                                                         ")
        print("    ██╗   ██╗██╗   ██╗    ███╗   ███╗ █████╗ ███████╗███████╗███████╗    ")
        print("    ██║   ██║██║   ██║    ████╗ ████║██╔══██╗╚══███╔╝██╔════╝██╔════╝    ")
        print("    ██║   ██║██║   ██║    ██╔████╔██║███████║  ███╔╝ █████╗  ███████╗    ")
        print("    ██║   ██║██║   ██║    ██║╚██╔╝██║██╔══██║ ███╔╝  ██╔══╝  ╚════██║    ")
        print("    ╚██████╔╝╚██████╔╝    ██║ ╚═╝ ██║██║  ██║███████╗███████╗███████║    ")
        print("     ╚═════╝  ╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝    ")
        print("                                                                         ")
        print(" █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ ")
        print("                                                                         ")
        print("                                                                         ")

        print('                       [1] Printing simple mazes')
        print('                       [2] Printing random mazes')
        print('                       [3] Solving mazes')
        print('                       [4] Quit')
        print("                                                                         ")       
        print(" █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ ")
        selection = int(input('\n                          Select part: '))
        if selection == 1:
            maze.simple_mazes()
            # maze.menu()
            again = input('\n                          Simple maze again(y/n): ')
            while(again.lower() == 'y'):
                maze.simple_mazes()
                again = input('\n                       Simple maze again(y/n): ')
            else:
                maze.menu()
            # maze.draw_maze()
        elif selection == 2:
            maze.generate_maze()
            maze.draw_maze()
            again = input('\n                          Generate again(y/n): ')
            while(again.lower() == 'y'):
                maze.generate_maze()
                maze.draw_maze()
                again = input('\n                          Generate again(y/n): ')
            else:
                maze.menu()
        elif selection == 3:
            maze.generate_maze()
            maze.maze_solver()
            again = input('\n                          Solve again(y/n): ')
            while(again.lower() == 'y'):
                maze.generate_maze()
                maze.maze_solver()
                again = input('\n                          Solve again(y/n): ')
            else:
                maze.menu()
        elif selection == 4:
            exit()
        else:
            print('Invalid input')
            menu()


# width = 20
# height = 11
maze = Maze(10, 5)
# maze.generate_maze()
# maze.draw_maze()
maze.menu()

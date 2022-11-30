import random

RIGHT = (1, 0)
DOWN = (0, 1)
RIGHT_DOWN = (1, 1)
RIGHT_UP = (1, -1)
DIRECTIONS = (RIGHT, DOWN, RIGHT_DOWN, RIGHT_UP)

ALPHABETS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", 
             "j", "k", "l", "m", "n", "o", "p", "q", "r", 
             "s", "t", "u", "v", "w", "x", "y", "z"]

def get_size(grid):
    
    """ 
    
    Returns the size of the grid 

    """
    
    width = len(grid[0])
    length = len(grid)
    size = (width, length)
    return (size)

def print_word_grid(grid): 

    """ Prints grid directly to user """

    print_grid = ""
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            print(grid[row][column], end="")
        print()
        

def copy_word_grid(grid):

    """ Makes independant copy of grid """

    copy_of_grid = []
    for row in grid:
            copy_of_grid.append(row.copy())
    return copy_of_grid

def extract(grid, position, direction, max_len):

    """ 

        grid: nested list of letters
        position: (tuple) (x, y) position of word (str)
        direction: (tuple) direction of the word (str) going no more than max len (int) letters.

        extract a string from the grid of letters starting
        at the given position, moving in the given direction 
        containing no more than max len letters. 

        Returns the word
        
    """

    word = ""
    x = position[1]
    y = position[0]
    lim_x = len(grid[0])
    lim_y = len(grid)
    while len(word) < max_len and y < lim_x and 0 <= x < lim_y:
        word = word + grid[x][y]
        x = x + direction[1]
        y = y + direction[0]
    return (word)
    
def show_solution(grid, word, solution):
    
    """ 
        grid: nested list of letters 
        word: word that needs to be found in the grid (str)
        solution: a nested tuple that contains both position and direction of the word
    
        Looks for (word), makes the (word) bigger case 
        if it is there, otherwise, says its not there 
        
    """
       
    copy_of_grid = copy_word_grid(grid)
   
    if solution == False:
        print(word, "is not found in this word search")
    else:
        position = solution[0]
        direction = solution[1]
        x = position[1]
        y = position[0]
        for letter in word:         
            copy_of_grid[x][y] = letter.capitalize()
            x = x + direction[1]
            y = y + direction[0]
        print(word.upper(), "can be found as below")
        print_word_grid(copy_of_grid)

def find_right(grid, word):

    """ 
        grid: nested list of letters
        word: the word that needs to be found in the grid

        Helper function for the find function. Makes a sublist of each row,
        adds letter by letter until the word is found. Otherwise returns false

        Returns either a tuple of the positiona and direction of the word
        or False if it is not found
        
    """

    row_num = 0
    column_num = 0
    for row in grid:
        each_row = ""
        row_num += 1
        for letter in row: 
            each_row += letter
            if word in each_row:
                return ((column_num-len(word) + 1, row_num - 1), (1, 0))
            column_num += 1
            if column_num >= len(grid[0]):
                column_num = 0
    return False

def find_down(grid, word):

    """ 
        grid: nested list of letters
        word: the word that needs to be found in the grid

        Helper function for the find function. Makes a sublist of each column,
        adds letter by letter until the word is found. Otherwise returns false

        Returns either a tuple of the positiona and direction of the word
        or False if it is not found
    
    """

    row_num = 0
    column_num = 0
    each_column = ""
    while column_num < len(grid[0]):
        if len(each_column) == len(grid):
            each_column = ""
        each_column += grid[row_num][column_num]
        if word in each_column:
            return ((column_num, row_num -len(word)+1), (0, 1))
        row_num += 1
        if row_num >= len(grid):
            row_num = 0
            column_num += 1
    return False

def find_right_down(grid, word):

    """
        grid: nested list of letters
        word: word (str) that needs to be founf in grid

        Helper function for the find function. Makes a sublist going in the right_down direction,
        adds letter by letter until the word is found. Otherwise returns false

        Starts of the sublists: starting at the bottom left corner, then going up
        to the top left corner, then finally going to the right top corner.

        Returns either a tuple of the positiona and direction of the word
        or False if it is not found

    
    """

    direction = (1, 1)
    row_num = len(grid)-1
    column_num = 0
    each_diagonal = ""
    len_each_diag = 1

    # len_each_diag starts at 1 because the length of the first sublist will be 1

    while column_num < len(grid[0]) and 0 <= row_num < len(grid):
        if len(each_diagonal) >= len_each_diag:
        
            # Testing if length of each_diagonal is less than len_each_diag
            # to make sure it stays in range of the grid. Otherwise empty the sublist
    
            each_diagonal = ""
        if row_num >= 0 and column_num == 0:

            # if the start of the sublists are on column_num = 0,
            # it goes up until it reaches the top

            len_each_diag = len(grid) - row_num
        else:

            # Otherwise it goes to the right

            len_each_diag = len(grid[0]) - column_num
        row_num_diag = row_num
        column_num_diag = column_num

        # variables to keep track of the iterations inside the 
        # sublist without losing the start point of the sublists

        i = 0
        while i <= len_each_diag:
            each_diagonal += grid[row_num_diag][column_num_diag]
            if word in each_diagonal:

                # Checks if each_diagonal contains word 
            
                return ((column_num_diag - len(word) + 1, row_num_diag - len(word) +1), (1, 1))
            if row_num_diag < len(grid) - 1 and column_num_diag < len(grid[0]) - 1:

                # Checks if each_diag is in grid range

                row_num_diag += direction[0]
                column_num_diag += direction[1]
                i += 1
            else: 
                break
        if row_num > 0:

            # has the purpose of moving the start poiny of each_diag

            row_num -= 1
        else:
            row_num = 0
            column_num += 1
    return False

def find_right_up(grid, word):

    """
        grid: nested list of letters
        word: word (str) that needs to be found in grid

        Helper function for the find function. Makes a sublist going in the right_up direction,
        adds letter by letter until the word is found. Otherwise returns false

        Starts of the sublists: starting at the bottom right corner, then going left
        to the bottom left corner, then finally going to the left top corner.

        Almost identical to find_right_down function. Only difference is that the start points 
        of the sublists are different and goes in a different direction.

    
    """

    direction = (1, -1)
    row_num = len(grid)-1
    column_num = len(grid[0])-1
    each_diagonal = ""
    len_each_diag = 1
    while 0 <= column_num and 0 <= row_num:
        if len(each_diagonal) >= len_each_diag:
            each_diagonal = ""
        if column_num >= 0 and row_num == len(grid)-1:
            len_each_diag = len(grid[0]) - column_num
        else:
            len_each_diag = len(grid) - row_num
        row_num_diag = row_num
        column_num_diag = column_num
        i = 0
        while i <= len_each_diag:
            each_diagonal += grid[row_num_diag][column_num_diag]
            if word in each_diagonal:
                return ((column_num_diag - len(word) + 1, row_num_diag + len(word) - 1), (1, -1))
            if row_num_diag > 0 and column_num_diag < len(grid[0]) - 1:
                row_num_diag += direction[1]
                column_num_diag += direction[0]
                i += 1
            else:
                break
        if column_num > 0 :
            column_num -= 1
        else:
            column_num = 0
            row_num -= 1 
    return False


def find(grid, word):

    """
    grid: nested list of letters
    word: word that needs to be found in the grid

    Uses each helper function and checks if they have a solution

    Returns either a tuple of the positiona and direction of the word
    or False if it is not found
    
    """

    if find_right(grid, word) != False:
        return find_right(grid, word)
    elif find_down(grid, word) != False:
        return find_down(grid, word)
    elif find_right_down(grid, word) != False:
        return find_right_down(grid, word)
    elif find_right_up(grid, word) != False:
        return find_right_up(grid, word)
    else:
        return False
    
def find_all(grid, words):

    """
    grid: nested list of letters 
    words: list of words that need to be found in tthe grid

    Uses the find function and stores the solution or a boolean: False 
    into a dictionary where the keys are the words from the "words" parameter

    Returns the dictionary

    """

    solutions = {}
    for word in words:
        solutions[word] = find(grid, word)
    return solutions  

def is_valid(grid, word, solution):

    """
    grid: nested list of letters
    word: the word to check if it has a valid placement in the grid
    solution: position and direction of the word being placed in the grid

    Helper function for generate that checks if the words position and direction will let it fit inside 
    the boundaries of the grid and if it has a valid placement.

    valid placement: either " " or when the same letter of two words overlaps
    
    Returns a boolean to say whether or not it is a valid placement

    """

    column_num = solution[0][0]
    row_num = solution[0][1]
    dir = solution[1]
    i=0
    while i < len(word) and column_num < len(grid[0]) and 0 <= row_num < len(grid):  
        if(grid[row_num][column_num] != " "):
            return False
        i += 1
        column_num += dir[0]
        row_num += dir[1]
    if i < len(word):
        return False
    else:
        return True

def rand_fill(grid):

    """
    grid: nested list fo letters

    Helper function for generate that fills in " " with random lowercase alphabets.

    Returns the grid
    
    """

    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if grid[y][x] == " ":
                grid[y][x] = random.choice(ALPHABETS)
    return grid

    

def generate(width, height, words):

    """
    width: width of grid that is being generated by this function
    height: height of grid that is being generated by this function
    words: a list of words that needs to be generated in the grid

    Generates a function that contains some or all of the words in 
    the list (words).
    
    """

    grid = []
    words_in_grid=[]
    for y in range(0, height):
        grid.append([])
        for x in range(0, width):
            grid[y].append(" ")
    for word in words:
        for i in range(100):
            column_num = random.randrange(0, width)
            row_num = random.randrange(0, height)
            dir = random.choice(DIRECTIONS)
            sol = ((column_num, row_num), dir)
            copy = 0 
            if is_valid(grid, word, sol) == True:
                words_in_grid.append(word)
                for letter in word:
                    grid[row_num][column_num] = letter
                    column_num += dir[0]
                    row_num += dir[1]
                break           
    grid = rand_fill(grid)
    return (grid, words_in_grid)

def print_generated(grid, words): 

    """ Prints generated word search """

    print_grid = ""
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            print(grid[row][column], end="")
        print()


                     
        




# print_word_grid([["p", "c", "n", "d", "t", "h", "g"],
#                  ["w", "a", "x", "o", "a", "x", "f"],
#                  ["o", "t", "w", "g", "d", "r", "k"],
#                  ["l", "j", "p", "i", "b", "e", "t"],
#                  ["f", "v", "l", "t", "o", "w", "n"]])

# print(rand_fill([["h", "i", "e", " "], 
#                  ["q", " ", " ", "r"], 
#                  [" ", " ", "d", "f"], 
#                  ["h", " ", "l", "k"]]))

g, w = generate(4,5, ["cat", "bat", "hat", "bag"])
print_generated(g, w)

# print_generated(generate(4,5, ["cat", "bat", "hat", "bag"]))

# print(is_valid([[" ", " ", " ", " "], 
#                 [" ", " ", " ", " "], 
#                 [" ", " ", " ", " "], 
#                 [" ", " ", " ", " "]], "cat", ((1, 1),(1, 1))))    
            
# print_word_grid(generate(5,6, ["hi", "cat", "bat", "go"]))               








    


from turtle import *
import random


# MARGINS
MARGX = 20 # horizontal margin 
MARGY = 20 # vertical margin 

# MESSAGES
MESSAGE_HEIGHT = 40

# BOARD
BOARD_LENGTH = window_width() - 2 * MARGX 
BOARD_HEIGHT = window_height() - 4 * MARGY - 2 * MESSAGE_HEIGHT

# GRID
NUMBER_OF_ROWS = 20
NUMBER_OF_COLUMNS = 20
CELL_LENGTH = BOARD_LENGTH / NUMBER_OF_COLUMNS # length of a single cell
CELL_HEIGHT = BOARD_HEIGHT / NUMBER_OF_ROWS # height of a single cell

# START POS of the first cell (bottom-left of board)
WINDOW_WIDTH = window_width()
WINDOW_HEIGHT = window_height()
START_POSITION = (
    -WINDOW_WIDTH / 2 + MARGX, 
    -WINDOW_HEIGHT / 2 + 2 * MARGY + MESSAGE_HEIGHT
)


def hop_by(x, y): # move by (x, y) without drawing
    up()
    goto(xcor() + x, ycor() + y)
    down()


def hop_to(x, y): # move to position (x, y) without drawing
    up()
    goto(x, y)
    down()


def box(length, height, border_colour, bg_colour): # draw a rectangle
    color(border_colour, bg_colour)
    begin_fill()
    rt(90)
    for _ in range(2):
        fd(length)
        lt(90)
        fd(height)
        lt(90)
    end_fill()
    setheading(90)


def draw_message(border_colour, bg_colour, text): # draw a box with a message
    box(WINDOW_WIDTH - 2 * MARGX, MESSAGE_HEIGHT, border_colour, bg_colour) 
    color("black") 
    hop_by(BOARD_LENGTH/2, MESSAGE_HEIGHT / 5) 
    write(text, align = "center", font=('Arial', 15, 'bold')) 
    hop_to(START_POSITION[0], START_POSITION[1]) 


def draw_board(): # draw the game board with cells and messages
    hop_to(-WINDOW_WIDTH/2 + MARGX, -WINDOW_HEIGHT/2 + MARGY) 
    draw_message("red", "lightpink", "Use arrows, q ends") 
    hop_to(START_POSITION[0], START_POSITION[1]) 
    box(WINDOW_WIDTH - 2 * MARGX, WINDOW_HEIGHT - 4 * MARGY - 2 * MESSAGE_HEIGHT, "black", "lightgrey") 
    hop_to(-WINDOW_WIDTH/2 + MARGX, WINDOW_HEIGHT/2 - MARGY - MESSAGE_HEIGHT) 
    draw_message("red", "lightpink", "Your score is: 0")
    for _ in range(NUMBER_OF_ROWS):
        for _ in range(NUMBER_OF_COLUMNS):
            box(CELL_LENGTH, CELL_HEIGHT, "black", "lightgrey") 
            hop_by(CELL_LENGTH, 0) 
        hop_by(-BOARD_LENGTH, CELL_HEIGHT)
    update()


def cell(position, colour): # draw a single cell 
    hop_to(START_POSITION[0], START_POSITION[1]) 
    hop_by((position[1]) * CELL_LENGTH, (position[0]) * CELL_HEIGHT) 
    setheading(90) 
    box(CELL_LENGTH, CELL_HEIGHT, "black", colour) 


def snake_head(position, colour): # draw the head of the snake 
    cell(position, colour) 
    setheading(90) 
    hop_by(CELL_LENGTH / 2, CELL_HEIGHT / 2) 
    dot(CELL_HEIGHT / 2, "red")


def draw_multiple_cells(positions, colour):
    for position in positions: 
        hop_to(START_POSITION[0] + position[1] * CELL_LENGTH,
           START_POSITION[1] + position[0] * CELL_HEIGHT)        
        setheading(90) 
        box(CELL_LENGTH, CELL_HEIGHT, "black", colour) 
        hop_to(START_POSITION[0], START_POSITION[1])


def spawn_head(board_matrix): # spawn snake head in a random empty cell
    head_pos = None
    while head_pos is None:
        row, column = random.randint(0, NUMBER_OF_ROWS - 1), random.randint(0, NUMBER_OF_COLUMNS - 1) 
        if board_matrix[row][column] == "0": 
            board_matrix[row][column] = "H"
            head_pos = (row, column)  
            snake_head(head_pos, "yellow") 
    return head_pos


def spawn_stones(board_matrix, how_many): # spawn given number of stones on empty cells
    stones = [] 
    while len(stones) < how_many: 
        row, column = random.randint(0, NUMBER_OF_ROWS - 1), random.randint(0, NUMBER_OF_COLUMNS - 1) 
        if board_matrix[row][column] == "0": 
            board_matrix[row][column] = "S" 
            stones.append((row, column)) 
    draw_multiple_cells(stones, "blue") 


def spawn_food(board_matrix, how_much): # spawn given number of food cells on empty cells
    food = [] 
    while len(food) < how_much: 
        row, column = random.randint(0, NUMBER_OF_ROWS - 1), random.randint(0, NUMBER_OF_COLUMNS - 1) 
        if board_matrix[row][column] == "0": 
            board_matrix[row][column] = "F" 
            food.append((row, column)) 
    draw_multiple_cells(food, "green") 


# keyboard input handling
pressed_key = ""


def set_direction(key):

    def result():
        global pressed_key
        pressed_key = key
        print(f"The {key} key was pressed")
    return result


def ini_keyboard():
    for direction in ["Up", "Left", "Right", "Down", "q"]:
        onkey(set_direction(direction.lower()), direction)
    listen()


def moving(board_matrix, snake, wynik):
    global pressed_key
    row, col = snake[0]  # current head position

    # update head position based on key
    if pressed_key == "up": 
        row += 1
    elif pressed_key == "down": 
        row -= 1
    elif pressed_key == "right": 
        col += 1 
    elif pressed_key == "left": 
        col -= 1 
    elif pressed_key == "q":
        return None

    if row < 0 or row >= NUMBER_OF_ROWS or col < 0 or col >= NUMBER_OF_COLUMNS:
        return None, wynik

    new_head = (row, col)

    # collision with empty space
    if board_matrix[row][col] == "0":
        cell(snake[-1], "lightgrey")
        board_matrix[snake[-1][0]][snake[-1][1]] = "0"
        snake = [new_head] + snake[:-1]
        draw_multiple_cells(snake[1:], "yellow")
        snake_head(new_head, "yellow")
        board_matrix[new_head[0]][new_head[1]] = "H"
        for el in snake[1:]:
            board_matrix[el[0]][el[1]] = "B"

    # collision with food
    elif board_matrix[row][col] == "F":
        snake = [new_head] + snake
        wynik += 1
        hop_to(START_POSITION[0], START_POSITION[1] + BOARD_HEIGHT + MARGY)
        draw_message("red", "lightpink", f"Your score is: {wynik}")
        spawn_food(board_matrix, 1)
        draw_multiple_cells(snake[1:], "yellow")
        snake_head(new_head, "yellow")
        board_matrix[new_head[0]][new_head[1]] = "H"
        for el in snake[1:]:
            board_matrix[el[0]][el[1]] = "B"

    # collision with stones or own body
    elif board_matrix[row][col] in ["S", "B"]:
        return None, wynik

    return snake, wynik


def game_loop(board_matrix, snake, wynik, speed):
    snake, wynik = moving(board_matrix, snake, wynik)
    if snake is not None:
        ontimer(lambda: game_loop(board_matrix, snake, wynik, speed), speed)    
    else:
        hop_to(- WINDOW_WIDTH / 2 + MARGX, 0)
        color("black") 
        hop_by(BOARD_LENGTH/2, 0) 
        write("GAME OVER!", align = "center", font=('Arial', 50, 'bold')) 


def main(): 
    tracer(0, 0)
    setheading(90)
    draw_board()
    board_matrix = [["0" for _ in range(NUMBER_OF_COLUMNS)] for _ in range(NUMBER_OF_ROWS)]
    spawn_stones(board_matrix, 10)
    spawn_food(board_matrix, 10)
    snake = [spawn_head(board_matrix)]
    wynik = 0
    ini_keyboard()
    game_loop(board_matrix, snake, wynik, 200)
    update()


main()
done()
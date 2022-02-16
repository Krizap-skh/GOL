import time
import random


def run_game():
    """Запускает игру"""
    ROWS = 10
    COLS = 10
    times = 7
    first_step = create_first_table(ROWS, COLS)
    next_step = create_first_table(ROWS, COLS)
    for _ in range(1, times):
        print_table(ROWS, COLS, first_step)
        create_next_table(ROWS, COLS, first_step, next_step)
        time.sleep(0.3)
        print(f'{_ + 1} times\n *********')
        first_step, next_step = next_step, first_step
    print_table(ROWS, COLS, first_step)
    return


def create_first_table(rows, cols):
    """Создает список со случайным расположением живых клеток"""
    grid = []
    for row in range(rows):
        grid_rows = []
        for col in range(cols):
            if random.randint(0, 2) == 0:
                grid_rows += [1]
            else:
                grid_rows += [0]
        grid += [grid_rows]
    return grid


def print_table(rows, cols, table):
    """Создает игровое поле с символами "_" dead, "0" alive"""
    output_str = ""
    for row in range(rows):
        for col in range(cols):
            if table[row][col] == 0:
                output_str += "_"
            else:
                output_str += "0"
        output_str += "\n\r"
    print(output_str, end=" ")


def count_live_neighborns(row, col, rows, cols, table):
    """Считает живых соседей в соседних 8 клетках"""
    alive_count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):
                alive_count += table[((row + i) % rows)][((col + j) % cols)]
    return alive_count
    

def create_next_table(rows, cols, table, next_table):
    """Опеределяет статус ячеек на следующий ход и """
    for row in range(rows):
        for col in range(cols):
            live_neighbors = count_live_neighborns(row, col, rows, cols, table)
            if live_neighbors < 2 or live_neighbors > 3:
                next_table[row][col] = 0
            elif live_neighbors == 3 and table[row][col] == 0:
                next_table[row][col] = 1
            else:
                next_table[row][col] = table[row][col]
    return next_table


game_start = run_game()

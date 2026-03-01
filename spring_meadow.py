from turtle import *
from random import *
import math

def hop(x, y):
    up()
    rt(90)
    fd(x)
    lt(90)
    fd(y)
    down()

def parallelogram(length1, length2, acute_angle, border_colour, bg_colour):
    color(border_colour)
    fillcolor(bg_colour)
    begin_fill()
    rt(90)
    fd(length1)
    lt(acute_angle)
    fd(length2)
    lt(180 - acute_angle)
    fd(length1)
    lt(acute_angle)
    fd(length2)
    end_fill()
    lt(180)

def ladybug(size):
    parallelogram(size, 3/4 * 2 * size, 90, "red", "red")
    hop(0, 3/4 * 2 * size)
    parallelogram(size, 1/4 * 2 * size, 90, "black", "black")
    hop(0, -3/4 * 2 * size)
    spots = [(1/6 * size, 3/2 * 1/5 * size), (4/6 * size, 0), (-3/6 * size, 3/2 * 1/5 * size), (2/6 * size, 0), (-3/6 * size,  3/2 * 1/5 * size), (4/6 * size, 0), (-2/6 * size, 3/10 * size)]
    for spot in spots:
        hop(spot[0], spot[1])
        dot(1/4 * size, "black")
    hop(-1/6 * size, 8/10 * size)
    lt(45)
    pensize(size/20)
    down()
    fd(1/2 * size)
    up()
    rt(45)
    hop(4/6 * size, -math.sqrt((1/2 * size)**2 - (2/6 * size)**2))
    rt(45)
    down()
    fd(1/2 * size)
    up()
    pensize(1)

def draw_two_rectangles_with_a_gap(length, height, gap, border_colour, bg_colour):
    lt(90)
    parallelogram(height, length, 90, border_colour, bg_colour)
    rt(90)
    hop(gap, 0)
    parallelogram(length, height, 90, border_colour, bg_colour)
    hop(-gap, 0)

def butterfly(size, colour1, colour2):
    bigger_wing_length = 9/20 * size
    bigger_wing_height = 2/3 * 10/14 * size
    hop(9/20 * size, 0)
    parallelogram(1/10 * size, 12/14 * size, 90, "black", "black")
    hop(1/20 * size, 13/14 * size)
    dot(2/14 * size, "black")
    hop(-1/20 * size, -12/14 * size)
    draw_two_rectangles_with_a_gap(bigger_wing_length, bigger_wing_height, 1/10 * size, "black", colour1)
    hop(-1/4 * bigger_wing_length, 1/4 * bigger_wing_height)
    draw_two_rectangles_with_a_gap(1/2 * bigger_wing_length, 1/2 * bigger_wing_height, 1/10 * size + 1/2 * bigger_wing_length, "black", colour2)
    hop(1/4 * bigger_wing_length, 3/4 * bigger_wing_height)
    draw_two_rectangles_with_a_gap(1/2 * bigger_wing_length, 1/2 * bigger_wing_height, 1/10 * size, "black", colour2)

def draw_two_parallelograms_with_a_gap(length, height, gap, acute_angle, border_colour, bg_colour):
    lt(90)
    parallelogram(height, length, acute_angle, border_colour, bg_colour)
    rt(acute_angle)
    hop(gap, 0)
    lt(acute_angle)
    parallelogram(length, height, acute_angle, border_colour, bg_colour)
    hop(-gap, 0)

def fern(size):
    longest_branch_length = math.sqrt((1/3 * size)**2 + (5/2 * 1/8 * size)**2)
    setheading(90)
    hop(4/9 * size, 0)
    parallelogram(1/9 * size, size, 90, "green", "green")
    draw_two_parallelograms_with_a_gap(longest_branch_length, 1/9 * size, 1/9 * size, 45, "green", "green")
    hop(0, 1/3 * size)
    draw_two_parallelograms_with_a_gap(8/10 * longest_branch_length, 1/9 * size, 1/9 * size, 45, "green", "green")
    hop(0, 1/3 * size)
    draw_two_parallelograms_with_a_gap(6/10 * longest_branch_length, 1/9 * size, 1/9 * size, 45, "green", "green")


def draw_ladybugs(how_many):
    for _ in range(how_many):
        position = (randint(- window_width() // 2, window_width() // 2), randint(- window_height() // 2, - window_height() // 6))
        angle = randint(0, 359)
        size = randint(10, 40)
        up()
        goto(position[0], position[1])
        down()
        setheading(angle)
        ladybug(size)


def draw_butterflies(how_many):
    for _ in range(how_many):
        size = randint(20, 80)
        colours = ["yellow", "red", "black", "brown", "pink", "silver",
                "LightCoral", "light slate blue", "steel blue", "tan4", "teal"]
        colour1 = choice(colours)
        colours.remove(colour1)
        colour2 = choice(colours)
        position = (randint(- window_width() // 2, window_width() // 2), randint(- window_height() // 6, window_height() // 2))
        angle = randint(0, 359)
        up()
        goto(position[0], position[1])
        down()
        setheading(angle)
        butterfly(size, colour1, colour2)

def draw_ferns(how_many):
    for _ in range(how_many):
        position = (randint(- window_width() // 2, window_width() // 2), randint(- window_height() // 2, - window_height() // 6))
        size = randint(20, 100)
        up()
        goto(position[0], position[1])
        down()
        fern(size)

def main():
    tracer(0,0)
    setheading(90)
    hop(- 1/2 * window_width(), - 1/2 * window_height())
    parallelogram(window_width(), 1/3 * window_height(), 90, "lawn green", "lawn green")
    hop(0, 1/3 * window_height())
    parallelogram(window_width(), 2/3 * window_height(), 90, "sky blue", "sky blue")
    draw_ladybugs(20)
    draw_ferns(20)
    draw_butterflies(20)
    done()


main()

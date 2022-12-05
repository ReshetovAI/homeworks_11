import numpy as np
import matplotlib.pyplot as plt
root_list = []
x_change = []
func_direct = -1
color = 'r'
line = 'k'


def change_color():
    global color
    if color == 'r':
        color = 'b'
    else:
        color = 'r'
    return color


def change_line():
    global line
    if line == '-.':
        line = '-'
    else:
        line = '-.'
    return line


def func(x, a, b, c, d, e):
    function = a*(x**4)*np.sin(np.cos(x))+b*(x**3)+c*(x**2)+d*x+e
    return function

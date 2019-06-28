import math
import numpy as np
import interpolation

def debug(variable):
    print(variable, " = ", eval(variable))

def print_running(message):
    print("\n\n~ Jalankan ", message)

print_running(" Interpolasi : Metode Lagrange\n")
x = np.array([2, 11 / 4, 4])
y = np.array([1 / 2, 4 / 11, 1 / 4])
x_int = 3
debug(" x ")
debug(" y ")
debug(" x_int ")
[y_int] = interpolation.lagrange(x, y, x_int)
debug(" y_int ")

print_running(" Interpolasi : Metode Neville\n")
x = np.array([1.0, 1.3, 1.6, 1.9, 2.2])
y = np.array([0.7651977, 0.6200860, 0.4554022, 0.2818186, 0.1103623])
x_int = 1.5
debug(" x ")
debug(" y ")
debug(" x_int ")
[y_int, q] = interpolation.neville(x, y, x_int)
debug(" y_int ")
debug(" q ")

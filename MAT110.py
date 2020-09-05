from sympy import *
import sympy
from sympy.parsing.sympy_parser import *
import matplotlib.pyplot as plt
import numpy as np


class MAT110:
    ID = None
    NAME = 'MAT110'
    TAGS = []

    # TODO: make each method here identifiable so we can switch its status

    def __init__(self, expr, variable, point=None):
        transformations = (standard_transformations +
                           (implicit_multiplication_application,))
        self.exp = parse_expr(expr, transformations=transformations)
        self.exp = sympify(expr)
        self.var = symbols(variable)
        self.point = point

    def my_limit(self, sign=None):
        if sign is None:
            return sympy.limit(self.exp, self.var, self.point)
        else:
            return sympy.limit(self.exp, self.var, self.point, sign)

    def diff(self):
        return self.exp.diff(self.var).subs(self.var, self.point)

    def continuity(self):
        e1 = self.exp.subs(self.var, self.point)
        e2 = self.my_limit()
        e3 = self.my_limit('+') == self.my_limit('-')
        return e1 == e2 and e3

    def diff_able(self):
        r = sympify('h-' + str(self.point))
        e2 = sympify(self.exp.subs(self.var, r) - self.exp.subs(self.var, self.point))
        e3 = sympy.limit(e2 / r, 'h', 0, '+')
        e4 = sympy.limit(e2 / r, 'h', 0, '-')
        return self.continuity() and e3 == e4


x = np.linspace(0, 20, 100)

# Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(x, x, label='linear')
ax.set_xlabel('x')  # Add an x-label to the axes.
ax.set_ylabel('y')  # Add a y-label to the axes.
ax.set_title("Simple Plot")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()
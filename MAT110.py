from sympy import *
import sympy
from sympy.parsing.sympy_parser import *

transformations = (standard_transformations +
                   (implicit_multiplication_application,))


def my_limit(exp, var, point):
    expr = parse_expr(exp, transformations=transformations)
    expr = sympify(expr)
    variable = symbols(var)
    return sympy.limit(expr, variable, point)


def diff(exp, var, val=None):
    expr = parse_expr(exp, transformations=transformations)
    expr = sympify(expr)
    variable = symbols(var)
    return expr.diff(variable).subs(var, val)


pprint(diff('sin(x)', 'x', 0))

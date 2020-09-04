from sympy import *
import sympy
from sympy.parsing.sympy_parser import *
import matplotlib as mlt

transformations = (standard_transformations +
                   (implicit_multiplication_application,))


def my_limit(exp, var, point, sign=None):
    expr = parse_expr(exp, transformations=transformations)
    expr = sympify(expr)
    variable = symbols(var)
    if sign is None:
        return sympy.limit(expr, variable, point)
    else:
        return sympy.limit(expr, variable, point, sign)


def diff(exp, var, val=None):
    expr = parse_expr(exp, transformations=transformations)
    expr = sympify(expr)
    variable = symbols(var)
    return expr.diff(variable).subs(var, val)


def continuity(exp, var, point):
    expr = parse_expr(exp, transformations=transformations)
    expr = sympify(expr)
    variable = symbols(var)
    e1 = expr.subs(variable, point)
    e2 = my_limit(exp, var, point)
    e3 = my_limit(exp, var, point, '+') == my_limit(exp, var, point, '-')
    return e1 == e2 and e3


def diff_able(exp, var, point):
    expr = parse_expr(exp, transformations=transformations)
    e1 = sympify(expr)
    variable = symbols(var)
    # e1 = my_limit(exp, var)
    r = sympify('h-'+str(point))
    e2 = sympify(e1.subs(var, r) - e1.subs(var, point))
    e3 = sympy.limit(e2 / r, 'h', 0, '+')
    e4 = sympy.limit(e2 / r, 'h', 0, '-')
    return continuity(exp, var, point) and e3 == e4


print(diff_able('1/x', 'x', 1))

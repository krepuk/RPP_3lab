"""
Module for solving quadratic equations.
"""

def calculate_discriminant(a, b, c):
    """
    Calculate discriminant for quadratic equation.

    Args:
        a: Coefficient for x²
        b: Coefficient for x
        c: Constant term

    Returns:
        float: Discriminant value

    Raises:
        ValueError: If a is zero (not a quadratic equation)
    """
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero")
    return b ** 2 - 4 * a * c


def solve_quadratic(a, b, c):
    """
    Solve quadratic equation and return roots.

    Args:
        a: Coefficient for x²
        b: Coefficient for x
        c: Constant term

    Returns:
        tuple: Roots of the equation
    """
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero")

    discriminant = calculate_discriminant(a, b, c)

    if discriminant > 0:
        root1 = (-b + discriminant ** 0.5) / (2 * a)
        root2 = (-b - discriminant ** 0.5) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return(root,) 
    else:
        real_part = -b / (2 * a)
        imaginary_part = (-discriminant) ** 0.5 / (2 * a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2

# def bad_function():
# x=1  
# print("no indent")  

# very_long_variable_name_that_is_way_too_long_and_violates_pep8_guidelines_so_much = 1  

# def another_bad_function(  x , y  ):  
#    unused = 123  
#    return True
# ssdvfsvscxvxcvsdvfgsdDSGSD
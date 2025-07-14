import numpy as np


def add_inverse(a, b):
    """The inverse function of addition
    Args:
        a: The first number
        b: The second number
    Returns:
        The subtraction of a and b
    """
    return a - b


def subtract_inverse(a, b):
    """The inverse function of subtraction
    Args:
        a: The first number
        b: The second number
    Returns:
        The addition of a and b
    """
    return a + b


def multiply_inverse(a, b):
    """The inverse function of multiplication
    Args:
        a: The first number
        b: The second number
    Returns:
        The division of a and b
    """
    try:
        return a / b
    except (OverflowError, ValueError, ZeroDivisionError):
        return np.nan


def divide_inverse(a, b):
    """The inverse function of division
    Args:
        a: The first number
        b: The second number
    Returns:
        The multiplication of a and b
    """
    try:
        return a * b
    except (OverflowError, ValueError, ZeroDivisionError):
        return np.nan


def power_inverse(a, b):
    """The inverse function of power
    Args:
        a: The first number
        b: The second number
    Returns:
        The root of a and b
    """
    try:
        return a ** (1 / b)
    except (OverflowError, ValueError, ZeroDivisionError):
        return np.nan


def root_inverse(a, b):
    """The inverse function of root
    Args:
        a: The first number
        b: The second number
    Returns:
        The power of a and b
    """
    try:
        return a ** (b)
    except (OverflowError, ValueError):
        return np.nan


def game_solver(
    l_numbers,
    target_num,
    l_operations=[
        add_inverse,
        subtract_inverse,
        multiply_inverse,
        divide_inverse,
        power_inverse,
        root_inverse,
    ],
):
    """
    This function is used to solve the 24 game (or any other number game) recursively.
    Args:
        l_numbers [list]: The list of numbers in the formula
        target_num [int]: The target outcome
        l_operations [list]: The list of operations. The input functions should
                      be operations between two numbers, named in the format
                      operation_inverse, and should be the inverse function
                      of the operation. Refer to the example operation
                      functions for details.
    Returns [str or np.nan]:
        The equation of the game, or np.nan if no solution is found.
        The output string is a formula, such as "1 add 2 subtract 3", with operations
        strictly from left to right, ignoring operation precedence. For example, this
        expression represents (1+2)/3 rather than 1+(2/3).
    """
    if len(l_numbers) == 1:
        # In the most extreme case, we only use one number, which must equal target_num, otherwise there is no solution.
        # If it equals, return this number; otherwise, return np.nan.
        if l_numbers[0] == target_num:
            return str(l_numbers[0])
        else:
            return np.nan
    else:
        # We can simplify the problem as follows: assume we have n available numbers. For the target number, we can
        # first select a number, then choose an inverse operation to obtain a new target number. This transforms
        # the problem into using the remaining n-1 numbers to achieve the new target number.
        for i in range(len(l_numbers)):
            for operation in l_operations:
                try:
                    target_num_temp = operation(target_num, l_numbers[i])
                    # Check if the result is valid (not nan, not infinite, not too large)
                    if (
                        np.isnan(target_num_temp)
                        or np.isinf(target_num_temp)
                        or abs(target_num_temp) > 1e15
                    ):  # 设置一个合理的上限
                        continue

                    l_numbers_temp = l_numbers.copy()
                    del l_numbers_temp[i]
                    equation = game_solver(
                        l_numbers_temp, target_num_temp, l_operations
                    )  # Recursive call, if the lower layer has a solution, return str, otherwise return np.nan
                    if type(equation) == str:
                        return (
                            equation
                            + " "
                            + str(operation.__name__[:-8])
                            + " "
                            + str(l_numbers[i])
                        )
                    else:
                        continue
                except (OverflowError, ValueError, ZeroDivisionError):
                    # 当遇到数值计算错误时，跳过当前操作，继续下一个
                    continue
        return np.nan

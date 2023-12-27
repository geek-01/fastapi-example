def factorial(n):
    """
    Calculate the factorial of a given non-negative integer.

    Parameters:
    - n (int): The non-negative integer for which the factorial is calculated.

    Returns:
    - int: The factorial of n.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
def addition(a: float, b:float) -> float:
    return a + b


def subtraction(a: float, b:float) -> float:
    return a - b

def multiplication(a: float, b:float) -> float:
    return a * b

def division(a: float, b: float) -> float:
    if b == 0:  # Checks if 'b' is zero. If it is, we raise an error and stop the function.
        raise ValueError("Division by zero is not allowed.")  # This sends an error message when someone tries to divide by zero.
    return a / b  # If 'b' is not zero, we divide the first number (a) by the second number (b) and return the result.

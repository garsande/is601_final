# tests/unit/test_calculator.py

import pytest  # Import the pytest framework for writing and running tests
from typing import Union  # Import Union for type hinting multiple possible types
from app.operations import add, subtract, multiply, divide  # Import the calculator functions from the operations module
from app.operations import power, root, modulus, absoluteDifference, integerDivide, percentage, logarithm
# Define a type alias for numbers that can be either int or float
Number = Union[int, float]


# ---------------------------------------------
# Unit Tests for the 'add' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),           # Test adding two positive integers
        (-2, -3, -5),        # Test adding two negative integers
        (2.5, 3.5, 6.0),     # Test adding two positive floats
        (-2.5, 3.5, 1.0),    # Test adding a negative float and a positive float
        (0, 0, 0),            # Test adding zeros
    ],
    ids=[
        "add_two_positive_integers",
        "add_two_negative_integers",
        "add_two_positive_floats",
        "add_negative_and_positive_float",
        "add_zeros",
    ]
)
def test_add(a: Number, b: Number, expected: Number) -> None:
    """
    Test the 'add' function with various combinations of integers and floats.

    This parameterized test verifies that the 'add' function correctly adds two numbers,
    whether they are positive, negative, integers, or floats. By using parameterization,
    we can efficiently test multiple scenarios without redundant code.

    Parameters:
    - a (Number): The first number to add.
    - b (Number): The second number to add.
    - expected (Number): The expected result of the addition.

    Steps:
    1. Call the 'add' function with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    Example:
    >>> test_add(2, 3, 5)
    >>> test_add(-2, -3, -5)
    """
    # Call the 'add' function with the provided arguments
    result = add(a, b)
    
    # Assert that the result of add(a, b) matches the expected value
    assert result == expected, f"Expected add({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Unit Tests for the 'subtract' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),           # Test subtracting a smaller positive integer from a larger one
        (-5, -3, -2),        # Test subtracting a negative integer from another negative integer
        (5.5, 2.5, 3.0),     # Test subtracting two positive floats
        (-5.5, -2.5, -3.0),  # Test subtracting two negative floats
        (0, 0, 0),            # Test subtracting zeros
    ],
    ids=[
        "subtract_two_positive_integers",
        "subtract_two_negative_integers",
        "subtract_two_positive_floats",
        "subtract_two_negative_floats",
        "subtract_zeros",
    ]
)
def test_subtract(a: Number, b: Number, expected: Number) -> None:
    """
    Test the 'subtract' function with various combinations of integers and floats.

    This parameterized test verifies that the 'subtract' function correctly subtracts the
    second number from the first, handling both positive and negative values, as well as
    integers and floats. Parameterization allows for comprehensive testing of multiple cases.

    Parameters:
    - a (Number): The number from which to subtract.
    - b (Number): The number to subtract.
    - expected (Number): The expected result of the subtraction.

    Steps:
    1. Call the 'subtract' function with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    Example:
    >>> test_subtract(5, 3, 2)
    >>> test_subtract(-5, -3, -2)
    """
    # Call the 'subtract' function with the provided arguments
    result = subtract(a, b)
    
    # Assert that the result of subtract(a, b) matches the expected value
    assert result == expected, f"Expected subtract({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Unit Tests for the 'multiply' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),           # Test multiplying two positive integers
        (-2, 3, -6),         # Test multiplying a negative integer with a positive integer
        (2.5, 4.0, 10.0),    # Test multiplying two positive floats
        (-2.5, 4.0, -10.0),  # Test multiplying a negative float with a positive float
        (0, 5, 0),            # Test multiplying zero with a positive integer
    ],
    ids=[
        "multiply_two_positive_integers",
        "multiply_negative_and_positive_integer",
        "multiply_two_positive_floats",
        "multiply_negative_float_and_positive_float",
        "multiply_zero_and_positive_integer",
    ]
)
def test_multiply(a: Number, b: Number, expected: Number) -> None:
    """
    Test the 'multiply' function with various combinations of integers and floats.

    This parameterized test verifies that the 'multiply' function correctly multiplies two numbers,
    handling both positive and negative values, as well as integers and floats. Parameterization
    enables efficient testing of multiple scenarios in a concise manner.

    Parameters:
    - a (Number): The first number to multiply.
    - b (Number): The second number to multiply.
    - expected (Number): The expected result of the multiplication.

    Steps:
    1. Call the 'multiply' function with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    Example:
    >>> test_multiply(2, 3, 6)
    >>> test_multiply(-2, 3, -6)
    """
    # Call the 'multiply' function with the provided arguments
    result = multiply(a, b)
    
    # Assert that the result of multiply(a, b) matches the expected value
    assert result == expected, f"Expected multiply({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Unit Tests for the 'divide' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 3, 2.0),           # Test dividing two positive integers
        (-6, 3, -2.0),         # Test dividing a negative integer by a positive integer
        (6.0, 3.0, 2.0),       # Test dividing two positive floats
        (-6.0, 3.0, -2.0),     # Test dividing a negative float by a positive float
        (0, 5, 0.0),            # Test dividing zero by a positive integer
    ],
    ids=[
        "divide_two_positive_integers",
        "divide_negative_integer_by_positive_integer",
        "divide_two_positive_floats",
        "divide_negative_float_by_positive_float",
        "divide_zero_by_positive_integer",
    ]
)
def test_divide(a: Number, b: Number, expected: float) -> None:
    """
    Test the 'divide' function with various combinations of integers and floats.

    This parameterized test verifies that the 'divide' function correctly divides the first
    number by the second, handling both positive and negative values, as well as integers
    and floats. Parameterization allows for efficient and comprehensive testing across multiple cases.

    Parameters:
    - a (Number): The dividend.
    - b (Number): The divisor.
    - expected (float): The expected result of the division.

    Steps:
    1. Call the 'divide' function with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    Example:
    >>> test_divide(6, 3, 2.0)
    >>> test_divide(-6, 3, -2.0)
    """
    # Call the 'divide' function with the provided arguments
    result = divide(a, b)
    
    # Assert that the result of divide(a, b) matches the expected value
    assert result == expected, f"Expected divide({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Unit Tests for the 'power' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (3, 2, 9.0),           # Test dividing two positive integers
        (0, 5, 0.0),            # Test dividing zero by a positive integer
    ],
    ids=[
        "power_check_two_positive_integers",
        "power_check_zero_by_positive_integer",
    ]
)
def test_power(a: Number, b: Number, expected: float) -> None:
    """
    Test the 'power' function with various combinations of integers and floats.

    This parameterized test verifies that the 'power' function correctly finds the power of the first
    number by the second, handling both positive and negative values, as well as integers
    and floats. Parameterization allows for efficient and comprehensive testing across multiple cases.
    """
    # Call the 'divide' function with the provided arguments
    result = power(a, b)
    
    # Assert that the result of divide(a, b) matches the expected value
    assert result == expected, f"Expected divide({a}, {b}) to be {expected}, but got {result}"



# ---------------------------------------------
# Unit Tests for the 'root' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (4, 2, 2.0),           # Test dividing two positive integers
        (16.0, 2.0, 4.0),       # Test dividing two positive floats
        ],
    ids=[
        "root_two_positive_integers",
        "root_two_positive_floats",
        ]
)
def test_root(a: Number, b: Number, expected: float) -> None:
    """
    Test the 'root' function with various combinations of integers and floats.

    This parameterized test verifies that the 'root' function correctly roots the first
    number by the second, handling both positive and negative values, as well as integers
    and floats. Parameterization allows for efficient and comprehensive testing across multiple cases.

    Parameters:
    - a (Number): The dividend.
    - b (Number): The divisor.
    - expected (float): The expected result of the division.

    Steps:
    1. Call the 'root' function with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    """
    # Call the 'divide' function with the provided arguments
    result = root(a, b)
    
    # Assert that the result of divide(a, b) matches the expected value
    assert result == expected, f"Expected divide({a}, {b}) to be {expected}, but got {result}"



# ---------------------------------------------
# Unit Tests for the 'modulus' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (7, 3, 1.0),           # Test dividing two positive integers
        (-6, 4, 2.0),         # Test dividing a negative integer by a positive integer
        (6.0, 5.0, 1.0),       # Test dividing two positive floats
        (-16.0, 13.0, 10.0),     # Test dividing a negative float by a positive float
    ],
    ids=[
        "modulus_two_positive_integers",
        "modulus_negative_integer_by_positive_integer",
        "modulus_two_positive_floats",
        "modulus_negative_float_by_positive_float",
    ]
)
def test_modulus(a: Number, b: Number, expected: float) -> None:
    """
    Test the 'modulus' function with various combinations of integers and floats.

    This parameterized test verifies that the 'modulus' function correctly moduluss the first
    number by the second, handling both positive and negative values, as well as integers
    and floats. Parameterization allows for efficient and comprehensive testing across multiple cases.

    Parameters:
    - a (Number): The dividend.
    - b (Number): The divisor.
    - expected (float): The expected result of the modulus.

    """
    # Call the 'modulus' function with the provided arguments
    result = modulus(a, b)
    
    # Assert that the result of modulus(a, b) matches the expected value
    assert result == expected, f"Expected modulus({a}, {b}) to be {expected}, but got {result}"




# ---------------------------------------------
# Unit Tests for the 'integerDivide' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 3, 2.0),           # Test dividing two positive integers
        (-6, 3, -2.0),         # Test dividing a negative integer by a positive integer
        (6.0, 3.0, 2.0),       # Test dividing two positive floats
        (-6.0, 3.0, -2.0),     # Test dividing a negative float by a positive float
        (0, 5, 0.0),            # Test dividing zero by a positive integer
    ],
    ids=[
        "integerDivide_two_positive_integers",
        "integerDivide_negative_integer_by_positive_integer",
        "integerDivide_two_positive_floats",
        "integerDivide_negative_float_by_positive_float",
        "integerDivide_zero_by_positive_integer",
    ]
)
def test_integerDivide(a: Number, b: Number, expected: float) -> None:
    """
    Test the 'integerDivide' function with various combinations of integers and floats.

    This parameterized test verifies that the 'integerDivide' function correctly integerDivides the first
    number by the second, handling both positive and negative values, as well as integers
    and floats. Parameterization allows for efficient and comprehensive testing across multiple cases.

    Parameters:
    - a (Number): The dividend.
    - b (Number): The divisor.
    - expected (float): The expected result of the division.

    Steps:
    1. Call the 'integerDivide' function with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    Example:
    >>> test_integerDivide(6, 3, 2.0)
    >>> test_integerDivide(-6, 3, -2.0)
    """
    # Call the 'integerDivide' function with the provided arguments
    result = integerDivide(a, b)
    
    # Assert that the result of integerDivide(a, b) matches the expected value
    assert result == expected, f"Expected integerDivide({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Unit Tests for the 'absoluteDifference' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),           # Test absoluteDifferenceing a smaller positive integer from a larger one
        (-5, -3, 2),        # Test absoluteDifferenceing a negative integer from another negative integer
        (5.5, 2.5, 3.0),     # Test absoluteDifferenceing two positive floats
        (-5.5, -2.5, 3.0),  # Test absoluteDifferenceing two negative floats
        (0, 0, 0),            # Test absoluteDifferenceing zeros
    ],
    ids=[
        "absoluteDifference_two_positive_integers",
        "absoluteDifference_two_negative_integers",
        "absoluteDifference_two_positive_floats",
        "absoluteDifference_two_negative_floats",
        "absoluteDifference_zeros",
    ]
)
def test_absoluteDifference(a: Number, b: Number, expected: Number) -> None:
    """
    Test the 'absoluteDifference' function with various combinations of integers and floats.

    This parameterized test verifies that the 'absoluteDifference' function correctly absoluteDifferences the
    second number from the first, handling both positive and negative values, as well as
    integers and floats. Parameterization allows for comprehensive testing of multiple cases.

    Parameters:
    - a (Number): The number from which to absoluteDifference.
    - b (Number): The number to absoluteDifference.
    - expected (Number): The expected result of the absoluteDifferenceion.

    Steps:
    1. Call the 'absoluteDifference' function with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    Example:
    >>> test_absoluteDifference(5, 3, 2)
    >>> test_absoluteDifference(-5, -3, -2)
    """
    # Call the 'absoluteDifference' function with the provided arguments
    result = absoluteDifference(a, b)
    
    # Assert that the result of absoluteDifference(a, b) matches the expected value
    assert result == expected, f"Expected absoluteDifference({a}, {b}) to be {expected}, but got {result}"



# ---------------------------------------------
# Unit Tests for the 'percentage' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 100, 10.0),           # Test dividing two positive integers
        (20.0, 200.0, 40.0),       # Test dividing two positive floats
        ],
    ids=[
        "percentage_two_positive_integers",
        "percentage_two_positive_floats",
    ]
)
def test_percentage(a: Number, b: Number, expected: float) -> None:
    """
    Test the 'percentage' function with various combinations of integers and floats.

    This parameterized test verifies that the 'percentage' function correctly percentages the first
    number by the second, handling both positive and negative values, as well as integers
    and floats. Parameterization allows for efficient and comprehensive testing across multiple cases.

    Parameters:
    - a (Number): The exponent.
    - b (Number): The base.
    - expected (float): The expected result of the percentage.

    Steps:
    1. Call the 'percentage' function with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    Example:
    >>> test_percentage(6, 3, 2.0)
    >>> test_percentage(-6, 3, -2.0)
    """
    # Call the 'percentage' function with the provided arguments
    result = percentage(a, b)
    
    # Assert that the result of percentage(a, b) matches the expected value
    assert result == expected, f"Expected percentage({a}, {b}) to be {expected}, but got {result}"




# ---------------------------------------------
# Unit Tests for the 'logarithm' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (100, 10, 2.0),           # Test dividing two positive integers
        (16.0, 2.0, 4.0),       # Test dividing two positive floats
        ],
    ids=[
        "logarithm_two_positive_integers",
        "logarithm_two_positive_floats",
        ]
)
def test_logarithm(a: Number, b: Number, expected: float) -> None:
    """
    Test the 'logarithm' function with various combinations of integers and floats.

    This parameterized test verifies that the 'logarithm' function correctly logarithms the first
    number by the second, handling both positive and negative values, as well as integers
    and floats. Parameterization allows for efficient and comprehensive testing across multiple cases.

    Parameters:
    - a (Number): The number.
    - b (Number): The base.
    - expected (float): The expected result of the division.

    Steps:
    1. Call the 'logarithm' function with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    Example:
    >>> test_logarithm(6, 3, 2.0)
    >>> test_logarithm(-6, 3, -2.0)
    """
    # Call the 'logarithm' function with the provided arguments
    result = logarithm(a, b)
    
    # Assert that the result of logarithm(a, b) matches the expected value
    assert result == expected, f"Expected logarithm({a}, {b}) to be {expected}, but got {result}"



# ---------------------------------------------
# Negative Test Case: Division by Zero
# ---------------------------------------------

def test_divide_by_zero() -> None:
    """
    Test the 'divide' function with division by zero.

    This negative test case verifies that attempting to divide by zero raises a ValueError
    with the appropriate error message. It ensures that the application correctly handles
    invalid operations and provides meaningful feedback to the user.

    Steps:
    1. Attempt to call the 'divide' function with arguments 6 and 0, which should raise a ValueError.
    2. Use pytest's 'raises' context manager to catch the expected exception.
    3. Assert that the error message contains "Cannot divide by zero!".

    Example:
    >>> test_divide_by_zero()
    """
    # Use pytest's context manager to check for a ValueError when dividing by zero
    with pytest.raises(ValueError) as excinfo:
        # Attempt to divide 6 by 0, which should raise a ValueError
        divide(6, 0)
    
    # Assert that the exception message contains the expected error message
    assert "Cannot divide by zero!" in str(excinfo.value), \
        f"Expected error message 'Cannot divide by zero!', but got '{excinfo.value}'"

import pytest
import uuid

from app.models.calculation import (
    Calculation,
    Addition,
    Subtraction,
    Multiplication,
    Division,
    Power,
    Root,
    Modulus,
    IntegerDivide,
    AbsoluteDifference,
    Percentage,
    Logarithm
)

# Helper function to create a dummy user_id for testing.
def dummy_user_id():
    return uuid.uuid4()

def test_addition_get_result():
    """
    Test that Addition.get_result returns the correct sum.
    """
    inputs = [10, 5, 3.5]
    addition = Addition(user_id=dummy_user_id(), inputs=inputs)
    result = addition.get_result()
    assert result == sum(inputs), f"Expected {sum(inputs)}, got {result}"

def test_subtraction_get_result():
    """
    Test that Subtraction.get_result returns the correct difference.
    """
    inputs = [20, 5, 3]
    subtraction = Subtraction(user_id=dummy_user_id(), inputs=inputs)
    # Expected: 20 - 5 - 3 = 12
    result = subtraction.get_result()
    assert result == 12, f"Expected 12, got {result}"

def test_multiplication_get_result():
    """
    Test that Multiplication.get_result returns the correct product.
    """
    inputs = [2, 3, 4]
    multiplication = Multiplication(user_id=dummy_user_id(), inputs=inputs)
    result = multiplication.get_result()
    assert result == 24, f"Expected 24, got {result}"

def test_division_get_result():
    """
    Test that Division.get_result returns the correct quotient.
    """
    inputs = [100, 2, 5]
    division = Division(user_id=dummy_user_id(), inputs=inputs)
    # Expected: 100 / 2 / 5 = 10
    result = division.get_result()
    assert result == 10, f"Expected 10, got {result}"

def test_power_get_result():
    """
    Test that Power.get_result returns the correct value.
    """
    inputs = [3, 2, 2]
    power = Power(user_id=dummy_user_id(), inputs=inputs)
    # Expected: 100 / 2 / 5 = 10
    result = power.get_result()
    assert result == 81, f"Expected 81, got {result}"

def test_root_get_result():
    """
    Test that Root.get_result returns the correct value.
    """
    inputs = [81, 2, 2]
    root = Root(user_id=dummy_user_id(), inputs=inputs)
    
    result = root.get_result()
    assert result == 3, f"Expected 3, got {result}"

def test_modulus_get_result():
    """
    Test that Modulus.get_result returns the correct quotient.
    """
    inputs = [66, 16, 4]
    modulus = Modulus(user_id=dummy_user_id(), inputs=inputs)
    # Expected: 100 / 2 / 5 = 10
    result = modulus.get_result()
    assert result == 2, f"Expected 2, got {result}"

def test_integer_divide_get_result():
    """
    Test that IntegerDivide.get_result returns the correct quotient.
    """
    inputs = [133, 22]
    integerDivide = IntegerDivide(user_id=dummy_user_id(), inputs=inputs)
    # Expected: 100 / 2 / 5 = 10
    result = integerDivide.get_result()
    assert result == 6, f"Expected 6, got {result}"

def test_absolute_difference_get_result():
    """
    Test that AbsoluteDifference.get_result returns the correct quotient.
    """
    inputs = [10, -5, 20]
    absoluteDifference = AbsoluteDifference(user_id=dummy_user_id(), inputs=inputs)
    # Expected: 100 / 2 / 5 = 10
    result = absoluteDifference.get_result()
    assert result == 5, f"Expected 5, got {result}"

def test_percentage_get_result():
    """
    Test that Percentage.get_result returns the correct quotient.
    """
    inputs = [100, 10]
    percentage = Percentage(user_id=dummy_user_id(), inputs=inputs)
    # Expected: 100 / 2 / 5 = 10
    result = percentage.get_result()
    assert result == 10, f"Expected 10, got {result}"

def test_logarithm_get_result():
    """
    Test that Logarithm.get_result returns the correct quotient.
    """
    inputs = [64, 2]
    logarithm = Logarithm(user_id=dummy_user_id(), inputs=inputs)
    # Expected: 100 / 2 / 5 = 10
    result = logarithm.get_result()
    assert result == 6, f"Expected 6, got {result}"

def test_division_by_zero():
    """
    Test that Division.get_result raises ValueError when dividing by zero.
    """
    inputs = [50, 0, 5]
    division = Division(user_id=dummy_user_id(), inputs=inputs)
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        division.get_result()

def test_power_by_zero():
    """
    Test that Power.get_result raises ValueError when dividing by zero.
    """
    inputs = [50, -1]
    power = Power(user_id=dummy_user_id(), inputs=inputs)
    with pytest.raises(ValueError, match="Negative exponents not supported."):
        power.get_result()

def test_root_by_zero():
    """
    Test that Root.get_result raises ValueError when dividing by zero.
    """
    inputs = [50, 0, 5]
    root = Root(user_id=dummy_user_id(), inputs=inputs)
    with pytest.raises(ValueError, match="Zero root is undefined"):
        root.get_result()

def test_modulus_by_zero():
    """
    Test that Modulus.get_result raises ValueError when dividing by zero.
    """
    inputs = [50, 0, 5]
    modulus = Modulus(user_id=dummy_user_id(), inputs=inputs)
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        modulus.get_result()

def test_integer_division_by_zero():
    """
    Test that IntegerDivide.get_result raises ValueError when dividing by zero.
    """
    inputs = [50, 0, 5]
    integerDivide = IntegerDivide(user_id=dummy_user_id(), inputs=inputs)
    with pytest.raises(ValueError, match="Division by zero is not allowed"):
        integerDivide.get_result()

def test_percentage_by_zero():
    """
    Test that Percentage.get_result raises ValueError when dividing by zero.
    """
    inputs = [50, 0, 5]
    percentage = Percentage(user_id=dummy_user_id(), inputs=inputs)
    with pytest.raises(ValueError, match="Zero base is undefined"):
        percentage.get_result()

def test_logarithm_by_zero():
    """
    Test that Logarithm.get_result raises ValueError when dividing by zero.
    """
    inputs = [50, 0, 5]
    logarithm = Logarithm(user_id=dummy_user_id(), inputs=inputs)
    with pytest.raises(ValueError, match="Zero base is undefined"):
        logarithm.get_result()


        
def test_calculation_factory_addition():
    """
    Test the Calculation.create factory method for addition.
    """
    inputs = [1, 2, 3]
    calc = Calculation.create(
        calculation_type='addition',
        user_id=dummy_user_id(),
        inputs=inputs,
    )
    # Check that the returned instance is an Addition.
    assert isinstance(calc, Addition), "Factory did not return an Addition instance."
    assert calc.get_result() == sum(inputs), "Incorrect addition result."

def test_calculation_factory_subtraction():
    """
    Test the Calculation.create factory method for subtraction.
    """
    inputs = [10, 4]
    calc = Calculation.create(
        calculation_type='subtraction',
        user_id=dummy_user_id(),
        inputs=inputs,
    )
    # Expected: 10 - 4 = 6
    assert isinstance(calc, Subtraction), "Factory did not return a Subtraction instance."
    assert calc.get_result() == 6, "Incorrect subtraction result."

def test_calculation_factory_multiplication():
    """
    Test the Calculation.create factory method for multiplication.
    """
    inputs = [3, 4, 2]
    calc = Calculation.create(
        calculation_type='multiplication',
        user_id=dummy_user_id(),
        inputs=inputs,
    )
    # Expected: 3 * 4 * 2 = 24
    assert isinstance(calc, Multiplication), "Factory did not return a Multiplication instance."
    assert calc.get_result() == 24, "Incorrect multiplication result."

def test_calculation_factory_division():
    """
    Test the Calculation.create factory method for division.
    """
    inputs = [100, 2, 5]
    calc = Calculation.create(
        calculation_type='division',
        user_id=dummy_user_id(),
        inputs=inputs,
    )
    # Expected: 100 / 2 / 5 = 10
    assert isinstance(calc, Division), "Factory did not return a Division instance."
    assert calc.get_result() == 10, "Incorrect division result."

def test_calculation_factory_power():
    """
    Test the Calculation.create factory method for power.
    """
    inputs = [3,2]
    calc = Calculation.create(
        calculation_type='power',
        user_id=dummy_user_id(),
        inputs=inputs,
    )
    # Expected: 100 / 2 / 5 = 10
    assert isinstance(calc, Power), "Factory did not return a Power instance."
    assert calc.get_result() == 9, "Incorrect power result."

def test_calculation_factory_root():
    """
    Test the Calculation.create factory method for root.
    """
    inputs = [4,2]
    calc = Calculation.create(
        calculation_type='root',
        user_id=dummy_user_id(),
        inputs=inputs,
    )
    # Expected: 100 / 2 / 5 = 10
    assert isinstance(calc, Root), "Factory did not return a Root instance."
    assert calc.get_result() == 2, "Incorrect root result."

def test_calculation_factory_modulus():
    """
    Test the Calculation.create factory method for modulus.
    """
    inputs = [13,10]
    calc = Calculation.create(
        calculation_type='modulus',
        user_id=dummy_user_id(),
        inputs=inputs,
    )
    # Expected: 100 / 2 / 5 = 10
    assert isinstance(calc, Modulus), "Factory did not return a Modulus instance."
    assert calc.get_result() == 3, "Incorrect modulus result."

def test_calculation_factory_integer_divide():
    """
    Test the Calculation.create factory method for integerDivide.
    """
    inputs = [133,22]
    calc = Calculation.create(
        calculation_type='integerdivide',
        user_id=dummy_user_id(),
        inputs=inputs,
    )
    # Expected: 100 / 2 / 5 = 10
    assert isinstance(calc, IntegerDivide), "Factory did not return a IntegerDivide instance."
    assert calc.get_result() == 6, "Incorrect integerDivide result."

def test_calculation_factory_absolute_difference():
    """
    Test the Calculation.create factory method for absolute difference.
    """
    inputs = [10,-5,20]
    calc = Calculation.create(
        calculation_type='absolutedifference',
        user_id=dummy_user_id(),
        inputs=inputs,
    )
    # Expected: 100 / 2 / 5 = 10
    assert isinstance(calc, AbsoluteDifference), "Factory did not return a Absolute difference instance."
    assert calc.get_result() == 5, "Incorrect absolute difference result."

def test_calculation_factory_percentage():
    """
    Test the Calculation.create factory method for percentage.
    """
    inputs = [10,100]
    calc = Calculation.create(
        calculation_type='percentage',
        user_id=dummy_user_id(),
        inputs=inputs,
    )
    # Expected: 100 / 2 / 5 = 10
    assert isinstance(calc, Percentage), "Factory did not return a Percentage instance."
    assert calc.get_result() == 10, "Incorrect percentage result."

def test_calculation_factory_logarithm():
    """
    Test the Calculation.create factory method for logarithm.
    """
    inputs = [16,2]
    calc = Calculation.create(
        calculation_type='logarithm',
        user_id=dummy_user_id(),
        inputs=inputs,
    )
    # Expected: 100 / 2 / 5 = 10
    assert isinstance(calc, Logarithm), "Factory did not return a Logarithm instance."
    assert calc.get_result() == 4, "Incorrect logarithm result."


def test_calculation_factory_invalid_type():
    """
    Test that Calculation.create raises a ValueError for an unsupported calculation type.
    """
    with pytest.raises(ValueError, match="Unsupported calculation type"):
        Calculation.create(
            calculation_type='dummy',  # unsupported type
            user_id=dummy_user_id(),
            inputs=[10, 3],
        )

def test_invalid_inputs_for_addition():
    """
    Test that providing non-list inputs to Addition.get_result raises a ValueError.
    """
    addition = Addition(user_id=dummy_user_id(), inputs="not-a-list")
    with pytest.raises(ValueError, match="Inputs must be a list of numbers."):
        addition.get_result()

def test_invalid_inputs_for_subtraction():
    """
    Test that providing fewer than two numbers to Subtraction.get_result raises a ValueError.
    """
    subtraction = Subtraction(user_id=dummy_user_id(), inputs=[10])
    with pytest.raises(ValueError, match="Inputs must be a list with at least two numbers."):
        subtraction.get_result()

def test_invalid_inputs_for_division():
    """
    Test that providing fewer than two numbers to Division.get_result raises a ValueError.
    """
    division = Division(user_id=dummy_user_id(), inputs=[10])
    with pytest.raises(ValueError, match="Inputs must be a list with at least two numbers."):
        division.get_result()

def test_invalid_inputs_for_power():
    """
    Test that providing fewer than two numbers to Power.get_result raises a ValueError.
    """
    power = Power(user_id=dummy_user_id(), inputs=[10])
    with pytest.raises(ValueError, match="Inputs must be a list with at least two numbers."):
        power.get_result()

def test_invalid_inputs_for_root():
    """
    Test that providing fewer than two numbers to Root.get_result raises a ValueError.
    """
    root = Root(user_id=dummy_user_id(), inputs=[10])
    with pytest.raises(ValueError, match="Inputs must be a list with at least two numbers."):
        root.get_result()


def test_invalid_inputs_for_modulus():
    """
    Test that providing fewer than two numbers to Modulus.get_result raises a ValueError.
    """
    modulus = Modulus(user_id=dummy_user_id(), inputs=[10])
    with pytest.raises(ValueError, match="Inputs must be a list with at least two numbers."):
        modulus.get_result()


def test_invalid_inputs_for_integer_divide():
    """
    Test that providing fewer than two numbers to IntegerDivide.get_result raises a ValueError.
    """
    integerDivide = IntegerDivide(user_id=dummy_user_id(), inputs=[10])
    with pytest.raises(ValueError, match="Inputs must be a list with at least two numbers."):
        integerDivide.get_result()

def test_invalid_inputs_for_absolute_difference():
    """
    Test that providing fewer than two numbers to AbsoluteDifference.get_result raises a ValueError.
    """
    absoluteDifference = AbsoluteDifference(user_id=dummy_user_id(), inputs=[10])
    with pytest.raises(ValueError, match="Inputs must be a list with at least two numbers."):
        absoluteDifference.get_result()

def test_invalid_inputs_for_percentage():
    """
    Test that providing fewer than two numbers to Percentage.get_result raises a ValueError.
    """
    percentage = Percentage(user_id=dummy_user_id(), inputs=[10])
    with pytest.raises(ValueError, match="Inputs must be a list with at least two numbers."):
        percentage.get_result()

def test_invalid_inputs_for_logarithm():
    """
    Test that providing fewer than two numbers to Logarithm.get_result raises a ValueError.
    """
    logarithm = Logarithm(user_id=dummy_user_id(), inputs=[10])
    with pytest.raises(ValueError, match="Inputs must be a list with at least two numbers."):
        logarithm.get_result()


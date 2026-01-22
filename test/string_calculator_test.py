import pytest
import logging
from src.string_calculator import StringCalculator

logger = logging.getLogger(__name__)
""" Starter unit test file for the String Calculator kata.

This unit tests below support the first step of the kata and is designed to get you started practicing the 
"Three Rules". One at a time, remove the @pytest.mark.skip annotation and run pytest; the test should fail. Update the 
calculate_string implementation so the test passes. Continue in this fashion until all three tests are passing.

Once completing these, three tests, write your own tests to complete the String Calculator kata. 
"""

calc_instance = StringCalculator()

#@pytest.mark.skip
def test_an_empty_string_yields_zero():
    assert 0 == calc_instance.calculate_string('')


#@pytest.mark.skip
def test_a_single_number_yields_that_value():
    assert 5 == calc_instance.calculate_string('5')


#@pytest.mark.skip
def test_two_numbers_comma_delimited_yield_the_sum():
    assert 14 == calc_instance.calculate_string('5,9')


def test_add_function_with_integers():
    # simple case with two numbers
    assert 7 == calc_instance.add("3,4")


def test_add_function_with_longer_strings():
    # longer string of numbers
    assert 20 == calc_instance.add("10,5,5")


def test_add_function_with_any_string():
    # non-numeric values should be ignored
    assert 13 == calc_instance.add("1,a,3,4,5")


def test_add_function_with_negative_string():
    #negative numbers should raise an exception
    with pytest.raises(ValueError) as excinfo:
        calc_instance.add("1,-3,4,-5")
    logger.debug(f"Exception message: {excinfo.value}")


def test_add_function_with_newline_string():
    # delimiters here are , and \n
    assert 13 == calc_instance.add("1,\n3,4,5")


def test_add_function_with_alt_delimiter_string():
    # delimiter here is ; and \n
    assert 10 == calc_instance.add("2;3\n5")


def test_add_function_call_count_so_far():
    # get total number of times add() was called so far
    assert 6 == calc_instance.get_call_count_for_add()


def test_add_function_call_count():
    # reset call count and test again
    calc_instance.set_call_count_for_add(0)
    calc_instance.add("1,2")
    calc_instance.add("3,4")
    assert 2 == calc_instance.get_call_count_for_add()


def test_add_function_with_multiple_delimiter_string():
    # delimiters here are * \n ; %
    assert 15 == calc_instance.add("***\n2;;;3\n5%%%5")
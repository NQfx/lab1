from python_basics import *
from grader_contracts.python_basics import PositiveIntegerInput, TextInput, VectorPairInput

def test_count_vowels():
    assert count_vowels(TextInput("Hello World")) == 3
    assert count_vowels(TextInput("AEIOUaeiou")) == 10
    assert count_vowels(TextInput("bcdfghjkl")) == 0
    assert count_vowels(TextInput("")) == 0

def test_has_unique_characters():
    assert has_unique_characters(TextInput("abcde")) == True
    assert has_unique_characters(TextInput("aabbc")) == False
    assert has_unique_characters(TextInput("Aa")) == False
    assert has_unique_characters(TextInput("")) == True

def test_count_one_bits():
    assert count_one_bits(PositiveIntegerInput(7)) == 3
    assert count_one_bits(PositiveIntegerInput(8)) == 1
    assert count_one_bits(PositiveIntegerInput(1)) == 1
    assert count_one_bits(PositiveIntegerInput(1023)) == 10

def test_multiplicative_persistence():
    assert multiplicative_persistence(PositiveIntegerInput(39)) == 3
    assert multiplicative_persistence(PositiveIntegerInput(4)) == 0
    assert multiplicative_persistence(PositiveIntegerInput(999)) == 4

def test_mse():
    assert mse(VectorPairInput([1, 2, 3], [1, 2, 3])) == 0.0
    assert mse(VectorPairInput([1, 0], [0, 1])) == 1.0
    assert mse(VectorPairInput([10], [20])) == 100.0

def test_prime_factorization():
    assert prime_factorization(PositiveIntegerInput(86240)) == "(2**5)(5)(7**2)(11)"
    assert prime_factorization(PositiveIntegerInput(2)) == "(2)"
    assert prime_factorization(PositiveIntegerInput(100)) == "(2**2)(5**2)"

def test_pyramid():
    assert pyramid(PositiveIntegerInput(1)) == 1
    assert pyramid(PositiveIntegerInput(5)) == 2
    assert pyramid(PositiveIntegerInput(14)) == 3
    assert pyramid(PositiveIntegerInput(10)) == "It is impossible"

def test_is_balanced_number():
    assert is_balanced_number(PositiveIntegerInput(1234006)) == True
    assert is_balanced_number(PositiveIntegerInput(123456)) == False
    assert is_balanced_number(PositiveIntegerInput(10)) == True
    assert is_balanced_number(PositiveIntegerInput(121)) == True

test_count_vowels()
test_has_unique_characters()
test_count_one_bits()
test_multiplicative_persistence()
test_mse()
test_prime_factorization()
test_pyramid()
test_is_balanced_number()
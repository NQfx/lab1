"""Заготовки задач на базовый Python."""

from grader_contracts.python_basics import PositiveIntegerInput, TextInput, VectorPairInput


def count_vowels(data: TextInput) -> int:
    text = data.value
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

def has_unique_characters(data: TextInput) -> bool:
    text = data.value
    low_text = text.lower()
    for char in low_text:
        if low_text.count(char) > 1:
            return False
    return True


def count_one_bits(data: PositiveIntegerInput) -> int:
    number = data.value
    return bin(number).count("1")


def multiplicative_persistence(data: PositiveIntegerInput) -> int:
    number = data.value
    count = 0
    while number >= 10:
        digits = str(number)
        product = 1
        for digit in digits:
            product *= int(digit)
        number = product
        count += 1
    return count

def mse(data: VectorPairInput) -> float:
    predicted, expected = data.predicted, data.expected
    squared_sum = 0.0
    count = len(expected)
    for i in range(count):
        squared_sum += (predicted[i] - expected[i])**2
    return squared_sum/count


def prime_factorization(data: PositiveIntegerInput) -> str:
    number = data.value
    res, d = [], 2
    temp = number
    while d * d <= temp:
        if temp % d == 0:
            count = 0
            while temp % d == 0:
                count += 1
                temp //= d
            res.append(f"({d}**{count})" if count > 1 else f"({d})")
        d += 1
    if temp > 1:
        res.append(f"({temp})")
    return "".join(res)


def pyramid(data: PositiveIntegerInput) -> int | str:
    cube_count = data.value
    limit = int(cube_count**0.5)
    summ = 0
    for i in range(1, limit + 1):
        summ += i**2
        if summ == cube_count:
            return i
    return "It is impossible"


def is_balanced_number(data: PositiveIntegerInput) -> bool:
    number = data.value
    str_number = str(number)
    length = len(str_number)
    if length % 2 == 0:
        count = (length - 2) // 2
    else:
        count = (length - 1) // 2
    left_sum = 0
    right_sum = 0
    for i in range(count):
        left_sum += int(str_number[i])
        right_sum += int(str_number[length - 1 - i])
    return left_sum == right_sum

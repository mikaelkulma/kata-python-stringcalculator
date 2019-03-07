import re


def add(addends):
    numeric_chars = re.findall(r"-?\d+", addends)

    numbers_lt_1k = [int(n) for n in numeric_chars if int(n) < 1000]
    for n in numbers_lt_1k:
        if n < 0: raise ValueError("negatives not allowed")
    return sum(numbers_lt_1k)

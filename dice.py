"""A module that rolls different-faced dice."""


__author__ = "A. Anand"


import random


def d4(n: int = 1) -> list:
    """Return a random number between 1 and 4 'n' number of times."""

    rolls = []

    for i in range(n):
        rolls.append(random.randint(1, 4))

    return rolls


def d6(n: int = 1) -> list:
    """Return a random number between 1 and 6 'n' number of times."""

    rolls = []

    for i in range(n):
        rolls.append(random.randint(1, 6))

    return rolls


def d8(n: int = 1) -> list:
    """Return a random number between 1 and 8 'n' number of times."""

    rolls = []

    for i in range(n):
        rolls.append(random.randint(1, 8))

    return rolls


def d10(n: int = 1) -> list:
    """Return a random number between 1 and 10 'n' number of times."""

    rolls = []

    for i in range(n):
        rolls.append(random.randint(1, 10))

    return rolls


def d12(n: int = 1) -> list:
    """Return a random number between 1 and 12 'n' number of times."""

    rolls = []

    for i in range(n):
        rolls.append(random.randint(1, 12))

    return rolls


def d20(n: int = 1) -> list:
    """Return a random number between 1 and 20 'n' number of times."""

    rolls = []

    for i in range(n):
        rolls.append(random.randint(1, 20))

    return rolls


def roll_stats():
    results = d6(4)

    results.sort()
    results.pop(0)
    return sum(results)

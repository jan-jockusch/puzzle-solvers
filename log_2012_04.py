# coding=utf-8

# WIP

# Plan: determine all possible digit combinations, then all possible line
# guesses (horizontal and vertical), then reduce guesses down to those matching
# up vertically and horizontally.

import itertools as it
import operator
import functools

grid_size = 11
horizontal_products = [
    [224, 90, 18],
    [6, 63, 40],
    [12, 4, 1, 8],
    [189, 4, 2],
    [192, 54, 7],
    [1, 120, 9, 3],
    [126, 240, 4],
    [10, 6, 7, 8],
    [6, 9, 168, 5],
    [27, 7, 20, 12],
    [4, 24, 63],
]
vertical_products = [
    [96, 28, 27],
    [7, 432, 120],
    [28, 540],
    [12, 12, 63],
    [45, 28, 6, 8],
    [2, 3, 28],
    [9, 8, 8, 90],
    [4, 9, 35],
    [15, 2, 54, 28],
    [2, 7, 8, 54],
    [6, 8, 120],
]


def powerset(iterable):
    '''List all possible combinations of any number of elements contained
    in the input.

    >>> list(powerset([1,2,3]))
    [(1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
    '''
    s = list(iterable)
    return it.chain.from_iterable(
        it.combinations(s, r + 1) for r in range(len(s))
    )


def generate_products():
    '''Generate all possible products from subsets of unique numbers 1..9'''
    products = {}
    for factors in powerset(list(range(1, 10))):
        product = functools.reduce(operator.mul, factors)
        if product not in products:
            products[product] = []
        products[product].append(factors)
    return products


all_products = generate_products()


def generate_line_guesses(line_description, line_length):
    '''Given a line description, like [12, 4, 1, 8], build all possible guesses
    where i) no digit appears twice, and ii) the line length is fulfilled. The
    guess must contain at least one separator (None) between the groups, and
    may have any number of consecutive separators, also at the beginning and at
    the end.

    This needs to walk through all possible factorizations and throw out those
    where digits appear twice. Each of the remaining guesses needs to be run
    through all its permutations, and the "None"s needed to fill up the line
    must be generated in every possible combination.

    >>> generate_line_guesses([12, 4, 1, 8], 11)
    [
        ...
    ]
    '''
    for item in line_description:
        print(all_products[item])
    pass

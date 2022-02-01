# coding=utf-8

import itertools as it

# "Wenn A größer als B ist, dann ist C größer als D"
# translates into "not A > B or C > D"

truths = '''
not Ivan > Emil or Max > Conrad
not Gustav > Ole or Ulf > Kevin
not Conrad > Gustav or Ralf > Ole
not Ivan > Ole or Ivan > Emil
not Emil > Ivan or Ivan > Ole
not Max > Kevin or Emil > Ivan
not Ivan > Ralf or Conrad > Ole
not Anton > Conrad or Emil > Kevin
not Ivan > Emil or Ulf > Ralf
not Ivan > Kevin or Conrad > Ulf
not Emil > Conrad or Anton > Ivan
not Kevin > Max or Anton > Conrad
'''

# Extract the names of the boys into a set
operators = ['or', 'not', '>', ]
boys = set([token for token in truths.split() if token not in operators])

# Merge all single expressions into one expression
true_expression = ' and '.join([
    f'({truth})'
    for truth in truths.split('\n')
    if truth.strip()
])

# Check all permutations against the set of truths
for solution in it.permutations(boys):
    heights = {name: index for index, name in enumerate(solution)}
    if eval(true_expression, heights):
        print("The height order, from smallest to tallest, of the boys is:")
        print(', '.join(solution))
        break

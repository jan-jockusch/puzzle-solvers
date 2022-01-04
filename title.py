import string
import re
import itertools as it

problem = "HUHN * GACK == FLUGBAHN"

symbols = set([letter for letter in problem
               if letter in string.ascii_uppercase])

for perm in it.permutations(string.digits):
    solution = dict(zip(symbols, perm))
    translated = problem.translate(str.maketrans(solution))
    # Remove leading zeros, because they will ruin eval()
    equation = re.sub(r'(^|\D)0+', r'\1', translated)
    if eval(equation) is True:
        print(f'''
Solution found: {translated}
{solution}
''')

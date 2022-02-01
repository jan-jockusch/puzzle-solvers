from pprint import pprint
from collections import namedtuple

# WIP

field_str = '''\
A B C D E F|
G  /H      /
I J  /K_  L|
M   N|O    |
P      |Q  |
R_ /S_ _ _ /'''

conditions_str = '''
Ah = Oh²
Hh = x²
Ih = x²
Kh = x²
Ph = Qh²
Rh = x²
Sh = Qv²
Av = Mh²
Bv = p

'''

squares = [x*x for x in range(999)]  # first 1000 squares.


def is_square(x):
    return x in squares


def is_palindrome(x):
    return x == int(''.join(reversed(str(x))))


Field = namedtuple('Field', ['letter', 'last_horiz', 'last_vert', 'value'])

elements = {}

rows = field_str.split('\n')
for row_index, row in enumerate(rows):
    cols = [row[i:i+2] for i in range(0, len(row), 2)]
    for col_index, col in enumerate(cols):
        last_horiz = col[-1] in '/|'
        last_vert = col[-1] in '/_'
        letter = col[0]
        elements[(row_index, col_index)] = Field(
            letter, last_horiz, last_vert, None
        )

words = []

pprint(elements)

import itertools as it
from collections import namedtuple

Party = namedtuple('Party', ['lastname', 'time', 'quantity', 'activity'])

lastnames = ['Müller', 'Hausmann', 'Becker', 'Keller']
times = [18, 19, 20, 21, ]
quantities = [8, 10, 12, 14, ]
activities = ['spielen', 'debattieren', 'überraschen', 'tanzen']


def check_conditions(ps):
    return ((
        # Müllers spielen Spiele
        any(p.lastname == 'Müller' for p in ps if p.activity == 'spielen')
        ^
        # Müllers beginnen um 19 Uhr
        any(p.lastname == 'Müller' for p in ps if p.time == 19)
    ) and (
        any(p.quantity == 10 for p in ps if p.time == 18)
        ^
        any(p.lastname == 'Müller' for p in ps if p.quantity == 10)
    ) and (
        any(p.quantity == 10 for p in ps if p.time == 19)
        ^
        any(p.quantity == 14 for p in ps if p.time == 21)
    ) and (
        any(p.quantity == 8 for p in ps if p.activity == 'debattieren')
        ^
        any(p.quantity == 8 for p in ps if p.time == 20)
    ) and (
        any(p.activity == 'spielen' for p in ps if p.time == 18)
        ^
        any(p.quantity == 14 for p in ps if p.activity == 'debattieren')
    ) and (
        any(p.lastname == 'Hausmann' for p in ps if p.quantity == 8)
        ^
        any(p.lastname == 'Keller' for p in ps if p.time == 18)
    ) and (
        any(p.lastname == 'Becker' for p in ps if p.time == 20)
        ^
        any(p.quantity == 10 for p in ps if p.activity == 'überraschen')
    ) and (
        any(p.time == 21 for p in ps if p.activity == 'spielen')
        ^
        any(p.quantity == 14 for p in ps if p.time == 21)
    ) and (
        any(p.lastname == 'Keller' for p in ps if p.quantity == 8)
        ^
        any(p.quantity == 12 for p in ps if p.activity == 'spielen')
    ) and (
        any(p.lastname == 'Müller' for p in ps if p.time == 19)
        ^
        any(p.quantity == 10 for p in ps if p.activity == 'tanzen')
    ))


for times_perm in it.permutations(times):
    for quantities_perm in it.permutations(quantities):
        for activities_perm in it.permutations(activities):
            comb = zip(lastnames, times_perm, quantities_perm, activities_perm)
            parties = [Party(*c) for c in comb]
            if check_conditions(parties):
                print(f'Solution found: {parties}')

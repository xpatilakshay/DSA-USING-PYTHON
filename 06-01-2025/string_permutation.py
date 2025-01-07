# 2) Print all possible permutations of a string.

import itertools

def permutations_of_strings(str):
    return list(itertools.permutations(str))

permutations = permutations_of_strings("ak")
for w in permutations:
    print("".join(w))
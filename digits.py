"""
This isn't actually right because the rules don't require that all numbers be used.
"""
import itertools as it

OPS = "+-*/"

def solve_perm(p, target):
    solutions = []
    for ops in it.product(OPS, repeat=len(p) - 1):
        A = p[0]
        fail = False
        for (B, op) in zip(p[1:], ops):
            if '/' == op and eval(f"{A}%{B}"):
                fail = True
                break
            A = eval(f"{A}{op}{B}")
            if A < 0:
                fail = True
                break
        if not fail and A == target:
            solutions.append(ops)

    return solutions


def solve(digits, target):
    for p in it.permutations(digits):
        solutions = solve_perm(p, target)
        if len(solutions) > 0:
            print(p, solutions)
            return

if __name__ == "__main__":
    #solve([1,2,3,4,5,10], 62)
    #solve([2,3,7,11,15,25],156)
    #solve([4,5,6,7,9,25],264)
    #solve([3,6,7,8,15,20], 312)
    solve([5,7,11,19,23,25], 438)
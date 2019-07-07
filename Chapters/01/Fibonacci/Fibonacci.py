from typing import Dict
from functools import lru_cache

memo: Dict[int, int] = {0: 0, 1: 1} # base cases

def fib1(n: int) -> int:
    # will run forever -> no base case! 
    return fib1(n-1) + fib1(n-2)

def fib2(n: int) -> int:
    # base case
    if n < 2:
        return n
    # naive recursive way 
    return fib2(n-1) + fib2(n-2)

#memoization 
def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n-1) + fib3(n-2)
    return memo[n]

#using memoization decorator caches return value n
@lru_cache(maxsize=None)
def fib4(n: int) -> int: # same def as fib2()
    if n < 2: 
        return n
    return fib4(n-2) + fib4(n-1) #recursive

def fib5(n: int) -> int:
    if n == 0: return n # special case
    last: int = 0 # fib(0)
    next: int = 1 # fib(1)

    for _ in range (1, n):
        last, next = next, last + next #tuple unpacking to prevent creation of temp variable (see below). last = next, next = last + next 
        # temp = next
        # last = next
        # next = last + temp 
    return next

#test
if __name__ == "__main__":
    print(fib2(0))
    print(fib2(1))
    print(fib2(2))
    print(fib2(3))
    print(fib2(4))
    print(fib2(5)) 
    print(fib3(50))
    print(fib4(50))
    print(fib5(5))
    print(fib5(50))
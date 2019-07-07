from typing import Dict

memo: Dict[int, int] = {0: 0, 1: 1} # base cases

def fib1(n: int) -> int:
    # will run forever -> no base case! 
    return fib1(n-1) + fib1(n-2)

def fib2(n: int) -> int:
    # base case
    if n < 2:
        return n
    # recursive way 
    return fib2(n-1) + fib2(n-2)
def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n-1) + fib3(n-2)
    return memo[n]
    
#test
if __name__ == "__main__":
    print(fib2(0))
    print(fib2(1))
    print(fib2(2))
    print(fib2(3))
    print(fib2(4))
    print(fib2(5)) 
    print(fib2(5))
    print(fib3(50))
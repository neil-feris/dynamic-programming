from time import perf_counter
from functools import cache, wraps


def timer(func, *args, **kwargs):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        diff = perf_counter() - start
        print(f"It took {diff:<2.10f} seconds to run")
        return result

    return wrapper


@timer
def run_fib(func, *args, **kwargs):
    print(func(*args, **kwargs))


@cache
def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)


def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n < 2:
        return 1
    else:
        memo[n] = fib_memo(n - 2, memo) + fib_memo(n - 1, memo)
        return memo[n]


if __name__ == "__main__":
    run_fib(fib_memo, 500)
    run_fib(fib, 500)

# from functools import cache


# @cache
def gridtraveller(m, n, memo={}):
    params = str(min(m, n)) + "," + str(max(m, n))
    if params in memo:
        return memo[params]
    if m <= 0 or n <= 0:
        return 0
    if m == 1 and n == 1:
        return 1
    memo[params] = gridtraveller(m - 1, n, memo) + gridtraveller(m, n - 1, memo)
    return memo[params]


print(gridtraveller(1, 1))
print(gridtraveller(3, 2))
print(gridtraveller(2, 3))
print(gridtraveller(18, 18))

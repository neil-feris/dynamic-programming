def cansum(targetSum, numbers, memo={}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum < min(numbers):
        return False

    for num in numbers:
        remainder = targetSum - num
        if cansum(remainder, numbers, memo):
            memo[targetSum] = True
            return True
    memo[targetSum] = False
    return False


print(cansum(7, [2, 4]))
print(cansum(7, [3, 5, 4, 7]))
print(cansum(15, [2, 4, 8, 10]))
print(cansum(15, [3, 5, 4, 7]))
# print(cansum(200, [7, 14]))
# print(cansum(300, [7, 14]))

const canSum = (targetSum, numbers, memo = {}) => {
  if (targetSum in memo) return memo[targetSum];
  if (targetSum === 0) return true;
  if (targetSum < Math.min(...numbers)) return false;

  for (let num of numbers) {
    remainder = targetSum - num;
    if (canSum(remainder, numbers, memo)) {
      memo[targetSum] = true;
      return true;
    }
  }
  memo[targetSum] = false;
  return false;
};

console.log(canSum(7, [2, 4])); // false
console.log(canSum(7, [3, 5, 4, 7])); // true
console.log(canSum(15, [2, 4, 8, 10])); // false
console.log(canSum(15, [3, 5, 4, 7])); // true
console.log(canSum(210, [7, 14])); // true
console.log(canSum(300, [7, 14])); // false

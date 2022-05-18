const canSum = (targetSum, numbers) => {
  if (targetSum === 0) return true;
  if (targetSum < Math.min(...numbers)) return false;

  for (let num of numbers) {
    remainder = targetSum - num;
    if (canSum(remainder, numbers)) return true;
  }
  return false;
};

console.log(canSum(7, [2, 4]));
console.log(canSum(7, [3, 5, 4, 7]));
// console.log(canSum(7, [2, 4]));
// console.log(canSum(7, [2, 4]));

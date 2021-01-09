# o(n^2) time | O(1) space
# def twonumberSum(array,targetSum):
#   for i in range(len(array)-1):
#     firstNum = array[i]
#     for j in range(i+1, len(array)):
#       secondNum = array[j]
#       if firstNum + secondNum == targetSum:
#         return [firstNum,secondNum]
#   return []

# o(n) time | O() space
# def twonumberSum(array, targetSum):
#     nums = {}
#     for num in array:
#         potentialMatch = targetSum - num
#         if potentialMatch in nums:
#             return [potentialMatch, num]
#         else:
#             nums[num] = True
#     return []

# o(nLog(n))| o(1) space
def twonumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) -1

    while left < right:
        currentSum = array[left] + array[right]

        if currentSum == targetSum:
            return [array[left],array[right]]

        elif currentSum < targetSum:
          left +=1
        elif currentSum > targetSum:
          right -= 1
    return []







 
print(twonumberSum([1, 2, 4, 8], 12))
print(twonumberSum([1, 2, 4, 3], 12))
print(twonumberSum([1, 2, 7, 5], 12))
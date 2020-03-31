# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

def twoSum(nums, target):
    solution = []
    i = 0 
    while i < len(nums):
        num2 = target - nums[i]
        if num2 in nums[i+1:]:
            solution.append(i)
            solution.append(nums.index(num2,i+1))
            return solution
        i +=1

## Tests: 

print(twoSum([3,2,4],6))
print(twoSum([3,3,0],6))
print(twoSum([4,2,2],4))
print(twoSum([1,4],5))

## Runtime: 1164 ms, faster than 34.92% of Python online submissions for Two Sum.

def twoSum2(nums, target):
    h = {}
    for i, num in enumerate(nums):
        n = target - num
        if n not in h:
            h[num] = i
        else:
            print(h)
            return [h[n], i]

## Runtime: 36 ms, faster than 77.28% of Python online submissions for Two Sum.
                
print(twoSum2([3,2,4],6))
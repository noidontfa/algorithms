from typing import DefaultDict


nums = [2,2,1]
# nums = [4,1,2,1,2]
# nums = [1]

def singleNumber(nums):
    length = len(nums)
    if length == 1:
        return nums[0]
    b = dict()
    for i in nums:
        b[i] = b.get(i,0) + 1

    for i in b:
        if b[i] == 1:
            return i



print(singleNumber(nums))
nums = [1,2,3,4,5,6,7] 
k = 3
# nums = [-1,-100,3,99]
# k = 2


def retate(nums, k):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[0:-k]


retate(nums,k)
print(nums)
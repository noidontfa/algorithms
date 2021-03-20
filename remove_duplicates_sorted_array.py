nums = [1,1,2]
nums2 = [0,0,1,1,1,2,2,3,3,4]
def removeDuplicates(nums):
    length = len(nums)
    i = 0
    try:
        while i < length:
            if nums[i] ==nums[i + 1]:
                nums.pop(i)
                length = length - 1
            else:
                i = i + 1
    except:
        return len(nums)

removeDuplicates(nums)
print(nums)
removeDuplicates(nums2)
print(nums2)
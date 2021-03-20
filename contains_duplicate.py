nums = [1,2,3,1,-1]
# nums = [1,2,3,4]


def containsDuplicate(nums):
    b = set() 
    for num in nums:
        if num in b:
            return True
        else:
            b.add(num)
    return False

print(containsDuplicate(nums))


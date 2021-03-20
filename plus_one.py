digits = [1,2,3]
# digits = [4,3,2,1]
# digits = [0]

def plusOne(digits):
    length = len(digits)
    num_int = sum(digits[i]*10**(length - 1 - i) for i in range(length))
    num_int = num_int + 1
    num_int = [int(i) for i in str(num_int)]
    return num_int
plusOne(digits)
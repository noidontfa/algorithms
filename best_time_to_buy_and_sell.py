
# prices = [1,2,3,4,5]
# prices = [7,6,4,3,1]
# prices = [2,4,1]
# prices = [7,1,5,3,6,4]
prices = [6,1,3,2,4,7]
def maxProfit(prices):
    length = len(prices)
    b = [0] * length
    profit = 0
    index_max = 0
    for i in range(1,length):
        
        if prices[i] > prices[i - 1]:
            b[i] = i - 1
        else:
            b[i] = i
    

    max = prices[length - 1]
    for i in range(length -1,-1,-1):
        min = prices[b[i]]
        # print(min)
        if min == prices[i]:
            profit = profit + max - min
            max = prices[i-1]  
    print(prices)
    print(b)
    print(profit)
    return profit

maxProfit(prices)

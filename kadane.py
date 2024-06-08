"""
Maximum subarray problem

"""


#Brute force O(n^2)
def brute(A):
    max_sum  = float("-inf")
    for i in range(len(A)-1):
        for j in range(i,len(A)):
            max_sum = max(max_sum, sum(A[i:j]))

    return max_sum

#Kadane's Algo O(n)

def kadane(A):
    max_curr = max_global = A[0]
    for i in range(1,len(A)):
        max_curr = max(A[i], max_curr+A[i])
        if max_curr > max_global:
            max_global = max_curr
    return max_global

def buySellStock(A):
    maxGlobal = maxCurr = 0

    for i in range(1,len(A)):
        maxCurr+= A[i] - A[i-1]
        if maxCurr > 0:
            pass
        else:
            maxCurr = 0
        maxGlobal = max(maxGlobal, maxCurr)

    return maxGlobal
def buySellStock1(A):
    minVal = float("inf")
    profit = 0
    for i in range(len(A)):
        minVal = min(minVal, A[i])
        profit = max(profit, A[i] - minVal)
    return profit
    

if __name__ == "__main__":
    A = [-2,3,2,-1]
    A1 = [7,1,5,3,6,4]
    print(kadane(A))
    print(brute(A))
    print(buySellStock(A1))
    print(buySellStock1(A1))
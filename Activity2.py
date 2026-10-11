def total_profit(n):
    prices = [1,n,1,n,1]
    profit = 0
    for i in range(1, len(prices)):
        if prices[i]>prices[i-1]:
            profit+= prices[i]-prices[i-1]
    return profit
print("Total profit of 4 = ",total_profit(4))
print("Total profit of 5 = ",total_profit(5))
n= int(input("Enter a number = "))
print(total_profit(n))
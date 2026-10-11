def max_profit(n):
    prices = list(range(n,0 ,-1))+list(range( 1,n+1))
    min_price ,profit = prices[0],0
    for p in prices[1:]:
        min_price = min(min_price, p )
        profit = max(profit,p - min_price)
    return profit
print("The profit of 4 is = ",max_profit(4))
print("The profit of 5 is = ",max_profit(5))
n = int(input("Enter a number = "))
print(max_profit(n))
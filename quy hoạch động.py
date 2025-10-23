def fib_dp(n):  #dinamic programming
    if n <= 1: return n    
    dp = [0] * (n+1)
    dp[0], dp[1] = 0, 1 #gán giá trị ban đầu
    for i in range (2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
print(fib_dp(50))

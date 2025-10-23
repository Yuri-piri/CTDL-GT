def knapsack(W, weights, values, n):
    dp = [[0] * (W + 1) for _ in range(n+1)]
    for i in range (1, n+1):
        for W in range (1, W+1):
            if weights[i-1] <= W:
                dp[i][w] = max(values[i-1] + dp[i-1][weights[i-1]],dp[i-1][W])
            else:
                dp[i][W] = dp[i-1][W]
    
    return dp[n][W]

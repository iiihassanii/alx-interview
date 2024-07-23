#!/usr/bin/python3
"""Making change !"""


def makeChange(coins, total):
    """making change def
    !"""
    if total <= 0:
        return 0

    # Initialize the dp array with "infinity" values
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: no coins needed to make 0 amount

    # Fill the dp array
    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

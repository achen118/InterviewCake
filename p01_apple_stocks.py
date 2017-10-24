# Suppose we could access yesterday's stock prices as a list, where:

# The indices are the time in minutes past trade opening time, which was 9: 30am local time.
# The values are the price in dollars of Apple stock at that time.
# So if the stock cost $500 at 10: 30am, stock_prices_yesterday[60] = 500.

# Write an efficient function that takes stock_prices_yesterday and returns the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.

# For example:

#   stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

#   get_max_profit(stock_prices_yesterday)
    # returns 6 (buying for $5 and selling for $11)

# No "shorting"--you must buy before you sell. You may not buy and sell in the same time step(at least 1 minute must pass).

# First attempt:
# O(n^2) time
# O(1) space

# def get_max_profit(prices):
#     max_profit = None
#     for i in range(0, len(prices) - 1):
#         buy_at = prices[i]
#         for j in range(1, len(prices)):
#             sell_at = prices[j]
#             profit = sell_at - buy_at
#             if max_profit is None:
#                 max_profit = profit
#             elif profit > max_profit:
#                 max_profit = profit
#     print(max_profit)

# Optimized:
# O(n) time
# O(1) space

def get_max_profit(prices):
    min_price = prices[0]
    max_profit = prices[1] - prices[0]
    for i in range(2, len(prices)):
        curr_profit = prices[i] - min_price
        if curr_profit > max_profit:
            max_profit = curr_profit
        if prices[i] < min_price:
            min_price = prices[i]
    print(max_profit)


# Tests:
# get_max_profit([10, 7, 5, 8, 11, 9]) => 6
# get_max_profit([10, 7, 5, 3, 1, 0]) => -1
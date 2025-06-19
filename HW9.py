import time
import matplotlib.pyplot as plt

COINS = [50, 25, 10, 5, 2, 1]

# greedy algorithm
def find_coins_greedy(amount, coins=COINS):
    result = {}
    for coin in sorted(coins, reverse=True):
        count = amount // coin
        if count:
            result[coin] = count
            amount -= coin * count
    return result

# Dynamic programming 
def find_min_coins(amount, coins=COINS):
    min_coins = [0] + [float('inf')] * amount
    coin_used = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_used[i] = coin

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        result[coin] = result.get(coin, 0) + 1
        amount -= coin
    return result

# time comparison
def compare_algorithms(max_amount=500):
    amounts = list(range(1, max_amount + 1))
    greedy_times = []
    dp_times = []

    for amount in amounts:
        start = time.time()
        find_coins_greedy(amount)
        greedy_times.append(time.time() - start)

        start = time.time()
        find_min_coins(amount)
        dp_times.append(time.time() - start)

    return amounts, greedy_times, dp_times

# Visualization
def plot_times():
    amounts, greedy_times, dp_times = compare_algorithms(500)

    plt.figure(figsize=(10, 6))
    plt.plot(amounts, greedy_times, label='Greedy Algorithm', color='green')
    plt.plot(amounts, dp_times, label='Dynamic Programming', color='red')
    plt.xlabel('Amount')
    plt.ylabel('Time (seconds)')
    plt.title('Greedy vs Dynamic Programming Coin Change Performance')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    amount = 113
    print("Greedy:", find_coins_greedy(amount))
    print("Dynamic Programming:", find_min_coins(amount))

    plot_times()

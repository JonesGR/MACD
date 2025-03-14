import csv
import matplotlib.pyplot as plt


def calculate_EMA(sample, vector=[]):
    result = [0] * sample
    alpha = 2 / (sample + 1)
    for x, price in enumerate(vector[sample:]):
        nom = 0
        denom = 0
        for i in range(sample):
            nom += ((1 - alpha) ** i) * vector[sample + x - i]
            denom += (1 - alpha) ** i
        result.append(nom / denom)

    return result


def draw_plot_1(close_prices=[], MACD=[], SIGNAL=[], buy_sell=False, start_i=-5, stop_i=1010, buys=[], sells=[]):
    plot1 = plt.subplot(2, 1, 1)
    plt.plot(list(range(0, 1000)), close_prices, color='royalblue', label='Close price')
    if buy_sell:
        for i in range(1, len(MACD)):
            if (MACD[i] > SIGNAL[i - 1] and MACD[i - 1] <= SIGNAL[i]):
                plt.plot(i + 26, close_prices[i + 26], 'o', markerfacecolor='green', markeredgecolor='green')
                buys.append(i + 26)
            elif MACD[i] < SIGNAL[i - 1] and MACD[i - 1] >= SIGNAL[i]:
                plt.plot(i + 26, close_prices[i + 26], 'o', markerfacecolor='firebrick', markeredgecolor='firebrick')
                sells.append(i + 26)
    plt.grid(True)
    plt.legend(loc="upper right")
    plt.xlim(start_i, stop_i)


def draw_plot_2(close_prices=[], MACD=[], SIGNAL=[], start_i=-5, stop_i=1010):
    plot2 = plt.subplot(2, 1, 2)
    plt.plot(list(range(26, 1000)), MACD, color='royalblue', label='MACD')
    plt.plot(list(range(26, 1000)), SIGNAL, color='red', label='SIGNAL')
    for i in range(0, len(MACD)):
        if (MACD[i] > SIGNAL[i - 1] and MACD[i - 1] <= SIGNAL[i]):
            plt.plot(i + 26, SIGNAL[i], 'o', markerfacecolor='green', markeredgecolor='green')
        elif MACD[i] < SIGNAL[i - 1] and MACD[i - 1] >= SIGNAL[i]:
            plt.plot(i + 26, SIGNAL[i], 'o', markerfacecolor='firebrick', markeredgecolor='firebrick')
    plt.xlim(start_i, stop_i)


def simulate(capital, start_i, end_i, close_prices=[], buys=[], sells=[]):
    bought_actions = 0
    for index, value in enumerate(buys):
        if value >= start_i:
            closest_buy = index
            break
    for index, value in enumerate(sells):
        if value >= start_i:
            closest_sell = index
            break

    for i in range(start_i, end_i):
        if i == buys[closest_buy] and capital != 0:
            bought_actions = capital / close_prices[i]
            capital = 0
            closest_buy += 1
        if i == sells[closest_sell]:
            if capital == 0:
                capital = close_prices[i] * bought_actions
                bought_actions = 0
            closest_sell += 1

    if bought_actions != 0:
        capital = close_prices[buys[closest_buy-1]] * bought_actions

    return capital


csv_file = 'wig20_d.csv'

close_prices = []

# Wczytanie danych z pliku CSV
with open(csv_file, 'r') as file:
    csv_reader = csv.DictReader(file, delimiter=';')
    for row in csv_reader:
        close_prices.append(float(row['Close']))

EMA26 = calculate_EMA(26, close_prices)
EMA12 = calculate_EMA(12, close_prices)

MACD = []
for i, element in enumerate(EMA12):
    MACD.append(element - EMA26[i])

MACD = MACD[26:]
SIGNAL = calculate_EMA(9, MACD)

# Okno 1
plt.figure(figsize=(12, 8))
draw_plot_1(close_prices, MACD, SIGNAL)
draw_plot_2(close_prices, MACD, SIGNAL)

plt.legend(loc="upper right")
plt.grid(True)
plt.tight_layout()
plt.show()

# Okno 2

plt.figure(figsize=(12, 8))
start_i = 950
stop_i = 998
buys = []
sells = []
draw_plot_1(close_prices, MACD, SIGNAL, True, start_i, stop_i, buys, sells)
draw_plot_2(close_prices, MACD, SIGNAL, start_i, stop_i)

capital = simulate(1000, start_i, stop_i, close_prices, buys, sells)
print("Kapitał: "+str(capital))

plt.legend(loc="upper right")
plt.grid(True)

plt.tight_layout()
plt.show()

# Okno 3

plt.figure(figsize=(12, 8))
start_i = 800
stop_i = 920
buys = []
sells = []
draw_plot_1(close_prices, MACD, SIGNAL, True, start_i, stop_i, buys, sells)
draw_plot_2(close_prices, MACD, SIGNAL, start_i, stop_i)

capital = simulate(1000, start_i, stop_i, close_prices, buys, sells)
print("Kapitał: "+str(capital))

plt.legend(loc="upper right")
plt.grid(True)

plt.tight_layout()
plt.show()

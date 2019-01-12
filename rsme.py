# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt


def rmse(a, b):
    sum = np.true_divide(np.sum((a - b) ** 2), len(a) - 1)
    return np.sqrt(sum)


def millions(x):
    return '$%1.1fM' % (x * 1e-6)


if __name__ == '__main__':
    producao_anual_co2 = np.array([0.08, 0.23, 0.03, 0.05, 0.16, 0.33, 0.18, 0.09, 0.19, 0.05, 0.14])
    fertilidade_anual = np.array([0.51, 0.29, 0.34, 0.41, 0.54, 0.82, 0.43, 0.63, 0.68, 0.86, 0.55])

    print("rmse: %f" % rmse(fertilidade_anual, producao_anual_co2))

    np.random.seed(19680801)

    x = producao_anual_co2
    y = fertilidade_anual

    fig, ax = plt.subplots()
    ax.fmt_ydata = millions

    plt.xlim(0, 1)
    plt.ylim(0, 1)

    plt.ylabel('Fertilidade Anual')
    plt.xlabel('Produacoo Anual de C02')
    plt.plot([0, 1], [0, 1], '-g')
    plt.plot(x, y, 'o')

    plt.show()

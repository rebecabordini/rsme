# coding=utf-8
import itertools

import numpy as np
import matplotlib.pyplot as plt


def millions(x):
    return '$%1.1fM' % (x * 1e-6)


def plot(x, y, x_label, y_label, rmse, plot_id):
    plt.xlim(0, 1)
    plt.ylim(0, 1)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.subplot(plot_id)
    plt.plot([0, 1], [0, 1], '-g')
    plt.plot(x, y, 'o')
    plt.annotate('Tf={0:.3f}'.format(rmse), xy=(0, 1), xytext=(0.6, 0.1))


def combinations(data):
    return list(itertools.combinations(data, 2))


if __name__ == '__main__':
    fig, ax = plt.subplots()
    ax.fmt_ydata = millions

    data = [
        {
            'values': np.array([0.08, 0.23, 0.03, 0.05, 0.16, 0.33, 0.18, 0.09, 0.19, 0.05]),
            'label': 'CO2'
        },
        {
            'values': np.array([0.51, 0.29, 0.34, 0.41, 0.54, 0.82, 0.43, 0.63, 0.68, 0.86]),
            'label': 'Fertilidade'
        },
        {
            'values': np.array([0.5, 1, 1, 1, 1, 0.5, 1, 1, 1, 1]),
            'label': 'Erosao'
        }
    ]

    plot_id = 220

    for combination in combinations(data) or []:
        axis1 = combination[0]
        axis2 = combination[1]
        plot_id += 1

        import ipdb; ipdb.set_trace()
        sum = np.true_divide(np.sum((axis2['values'] - axis1['values']) ** 2), axis2['values'].size - 1)
        rmse = np.sqrt(sum)

        plot(x=axis1.get('values'),
             y=axis2.get('values'),
             x_label=axis1.get('label'),
             y_label=axis2.get('label'),
             rmse=rmse, plot_id=plot_id)

    plt.show()

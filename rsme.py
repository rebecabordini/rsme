# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt


def plot(x, y, x_label, y_label, rmse, plot_id):
    plt.xlim(0, 1)
    plt.ylim(0, 1)

    plt.subplot(plot_id)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.plot([0, 1], [0, 1], '-g')
    plt.plot(x, y, 'o')
    plt.annotate('Tf={0:.3f}'.format(rmse), xy=(0, 1), xytext=(0.6, 0.1))


def pasto():
    return [
        {
            'values': np.array([0.19, 1.0, 0.43, 0.46, 0.61, 0.03, 0.00, 0.19, 1.0, 0.43, 0.46, 0.61, 0.03, 0]),
            'label': 'Producao'
        },
        {
            'values': np.array([0.25, 0.30, 0.19, 0.73, 0.01, 0.57, 0.27, 0.31, 0.23, 0.29, 0.57, 0.00, 0.57, 0.22]),
            'label': 'CO2'
        },
        {
            'values': np.array([0.63, 0.25, 0.41, 0.00, 0.39, 0.05, 0.41, 0.64, 0.42, 0.45, 0.22, 0.68, 0.05, 0.53]),
            'label': 'Fertilidade'
        },
        {
            'values': np.array([1.00, 1.00, 0.50, 0.50, 1.00, 0.50, 1.00, 1.00, 1.00, 0.50, 0.50, 0.50, 0.50, 1.00]),
            'label': 'Erosao'
        },
        {
            'values': np.array([0.68, 0.35, 0.03, 0.80, 0.27, 0.46, 0.28, 0.67, 0.36, 0.00, 0.85, 0.27, 0.46, 0.2]),
            'label': 'Infiltracao'
        },
    ]


def perene():
    return [
        {
            'values': np.array([0.05, 0.40, 0.00, 0.03, 1.00, 0.33]),
            'label': 'Producaoo'
        },
        {
            'values': np.array([0.32, 0.07, 0.03, 0.00, 0.07, 0.15]),
            'label': 'CO2'
        },
        {
            'values': np.array([0.63, 0.51, 0.36, 0.51, 0.78, 0.47]),
            'label': 'Fertilidade'
        },
        {
            'values': np.array([1.00, 1.00, 0.50, 1.00, 1.00, 0.50]),
            'label': 'Erosao'
        },
        {
            'values': np.array([0.84, 0.38, 0.62, 0.92, 0.38, 0.60]),
            'label': 'Infiltracao'
        },
    ]


def anual():
    return [
        {
            'values': np.array([0.22, 0.99, 0.98, 1.00, 0.03, 0.17, 0.86, 0.85, 0.87, 0.00]),
            'label': 'Producao'
        },
        {
            'values': np.array([0.08, 0.23, 0.03, 0.05, 0.16, 0.33, 0.18, 0.09, 0.19, 0.05]),
            'label': 'CO2'
        },
        {
            'values': np.array([0.51, 0.29, 0.34, 0.41, 0.54, 0.82, 0.43, 0.63, 0.68, 0.86]),
            'label': 'Fertilidade'
        },
        {
            'values': np.array([0.50, 1.00, 1.00, 1.00, 1.00, 0.50, 1.00, 1.00, 1.00, 1.00]),
            'label': 'Erosao'
        },
        {
            'values': np.array([0.41, 0.56, 0.65, 0.62, 0.56, 0.35, 0.57, 0.64, 0.59, 0.59]),
            'label': 'Infiltracao'
        },
    ]


def plot_combination(x_axis, y_axis, plot_id):
    sum = np.true_divide(np.sum((y_axis['values'] - x_axis['values']) ** 2), y_axis['values'].size - 1)
    rmse = np.sqrt(sum)

    plot(x=x_axis.get('values'),
         y=y_axis.get('values'),
         x_label=x_axis.get('label'),
         y_label=y_axis.get('label'),
         rmse=rmse, plot_id=plot_id)


if __name__ == '__main__':
    fig, ax = plt.subplots()

    data = anual()
    plot_combination(x_axis=data[0], y_axis=data[1], plot_id=221)
    plot_combination(x_axis=data[0], y_axis=data[2], plot_id=222)
    plot_combination(x_axis=data[0], y_axis=data[3], plot_id=223)
    plot_combination(x_axis=data[0], y_axis=data[4], plot_id=224)

    plt.show()

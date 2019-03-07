import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal
import six
from matplotlib import colors
color_lst = ["b", "r", "k", 'g', 'y', 'c', 'grey', 'purple',
             'teal','tan','gold','plum','navy','palegreen','orange','indigo']

complete_color_lst = list(six.iteritems(colors.cnames))

def plot_scatter(figure_name, data, label):
    plt.figure(figure_name)
    for i in range(0, len(label)):
        label_index = list(label).index(label[i])
        if label_index == i:
            plt.scatter(data[i, 0], data[i, 1], label=label[label_index], c=color_lst[label_index])
        else:
            plt.scatter(data[i, 0], data[i, 1], c=color_lst[label_index])
    plt.legend()
    plt.draw()


def plot_two_signal(figure_name, s1, s2, y_shit=5,linestyle='-'):
    plt.figure(figure_name)
    [m, n] = np.shape(s1)
    for i in range(0, n):
        plt.plot(s1[:, i] + i * y_shit, c=color_lst[i],linestyle=linestyle)
        plt.plot(s2[:, i] + i * y_shit, c=color_lst[i],linestyle=linestyle)
    plt.draw()


def plot_multiple_time_series(figure_name, data, motion_time=[]):
    plt.figure(figure_name)
    n = len(data)
    for i in range(0, n):
        plt.plot(data[i][:, 0], data[i][:, 1] + i * 10, c=color_lst[i])
    for i in range(0, len(motion_time)):
        plt.axvline(motion_time[i])
    plt.draw()





def plot_power_spectrum(data, name, fs=100):
    f, Pxx_spec = signal.periodogram(data, fs, 'flattop', scaling='spectrum')
    plt.figure(name)
    plt.plot(f, np.sqrt(Pxx_spec))
    # plt.ylim([0, 0.6])

    plt.xlabel('frequency [Hz]')
    plt.ylabel('Linear spectrum [V RMS]')
    plt.draw()


def plot_multi_subplot(x,data,names,figure_title="figure"):
	f, axarr = plt.subplots(len(data), sharex=True)
	for i in range(0,len(data)):
		for j in range(0,np.shape(data[i])[-1]):
			axarr[i].plot(x,data[i][:,j])
		axarr[i].set_title(names[i])
	f.suptitle(figure_title)
	plt.draw()





def plot_two_warped_signal(figure_name, s1, s2, path):
    plt.figure(figure_name)
    plt.plot(s1[path[0], 0], c="b")
    plt.plot(s1[path[0], 1] + 5, c="r")
    plt.plot(s1[path[0], 2] + 10, c="k")
    plt.plot(s2[path[1], 0], c="b")
    plt.plot(s2[path[1], 1] + 5, c="r")
    plt.plot(s2[path[1], 2] + 10, c="k")
    plt.draw()

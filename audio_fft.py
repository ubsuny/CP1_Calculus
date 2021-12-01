import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy import fft 
def audio_fft(X,Y):
    fig, ax = plt.subplots(figsize=(10,7))
    ax.plot(X,Y, lw=3)
    ax.set_xlabel('time(ms)',fontsize=14)
    ax.set_ylabel('Amplitude ',fontsize=14)
    ax.set_title('Audio data with phyphox',fontsize=14)
    plt.show()
    y = np.fft.fft(Y)
    y_abs = abs(y)
    print(len(y_abs),len(X))
    fig, ax = plt.subplots(figsize=(10,7))
    plt.rcParams["figure.dpi"] = 100  # just to have a better view 
    ax.plot(X, y_abs)
    ax.set_xlabel('frequency',fontsize=14)
    ax.set_ylabel('Fourier component',fontsize=14)
    ax.set_title('FFT of Audio data ',fontsize=14)
    plt.show()
    freqs = np.fft.fftfreq(len(y_abs))
    fig, ax = plt.subplots(figsize=(10,7))
    ax.plot(freqs,y_abs)
    ax.set_xlabel('frequency',fontsize=14)
    ax.set_ylabel('Fourier component',fontsize=14)
    ax.set_title('FFt of Acceleration data',fontsize=14)
    plt.show()
    from scipy.signal import find_peaks
    peaks, _ = find_peaks(y_abs, height=0)

    return freqs[peaks]
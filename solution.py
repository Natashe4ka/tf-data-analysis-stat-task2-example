import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 965404933 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    t = 41
    alpha = 1 - p
    c = t ** 2 / 2
    tau = norm.ppf(1 - alpha / 2)
    tau_2 = norm.ppf(alpha / 2)
    left = 2*((tau_2+0.5) / np.sqrt(x.shape[0]) + x.mean()/2) / c
    right = 2*((tau+0.5) / np.sqrt(x.shape[0]) + x.mean()/2) / c
    return left, right

import pandas as pd
import numpy as np

from scipy.stats import norm

from scipy.stats import erlang

chat_id = 965404933 # Ваш chat ID, не меняйте название переменной


def solution(p: float, x: np.array) -> tuple:
    t = 41
    alpha = 1 - p
    c = t ** 2 / 2
    tau = norm.ppf(1 - alpha / 2)
    tau_2 = norm.ppf(alpha / 2)
    t_0 = erlang.ppf(1 - alpha / 2, x.shape[0],loc=-0.5, scale=1 / x.shape[0])
    t_1 = erlang.ppf(alpha / 2, x.shape[0],loc=-0.5, scale=1 / x.shape[0])
    left = (t_1 + x.mean()) / c
    right = (t_0 + x.mean()) / c
    return left, right

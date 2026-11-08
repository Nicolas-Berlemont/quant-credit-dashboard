import pandas as pd
from src.analytics import drawdown, log_returns


def test_drawdown_peak_is_zero():
    p = pd.Series([100, 110, 99, 120.0])
    assert drawdown(p).round(4).tolist() == [0.0, 0.0, -0.1, 0.0]


def test_log_returns_length():
    p = pd.Series([100, 101, 102.0])
    assert len(log_returns(p)) == 2
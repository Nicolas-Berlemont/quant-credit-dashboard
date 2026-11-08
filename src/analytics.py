import numpy as np
import pandas as pd


def log_returns(prices):
    return np.log(prices / prices.shift(1)).dropna()


def realized_vol(returns, window=21, ann=252):
    """Volatilité réalisée annualisée sur fenêtre glissante (21 jours ≈ 1 mois de bourse)."""
    return returns.rolling(window).std() * np.sqrt(ann)


def drawdown(prices):
    """Perte depuis le plus haut historique (0 = au sommet, -0.1 = -10 %)."""
    return prices / prices.cummax() - 1


if __name__ == "__main__":
    p = pd.Series([100, 110, 99, 120.0])
    print("drawdown:", drawdown(p).round(4).tolist())   # attendu [0, 0, -0.1, 0]
    print("returns :", log_returns(p).round(4).tolist())
    assert drawdown(p).round(4).tolist() == [0.0, 0.0, -0.1, 0.0]
    print("OK analytics")
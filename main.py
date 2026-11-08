from src.data import get_prices
from src.analytics import log_returns, realized_vol, drawdown

prices = get_prices(["LQD", "HYG", "IEF"])
rets = log_returns(prices)

print("Prix (5 dernières lignes) :")
print(prices.tail())

print("\nVol réalisée 1 mois, dernière valeur :")
print(realized_vol(rets).iloc[-1].round(3))

print("\nDrawdown max historique :")
print(drawdown(prices).min().round(3))

assert len(rets) == len(prices) - 1, "problème de taille sur les rendements"
print("\nOK main")
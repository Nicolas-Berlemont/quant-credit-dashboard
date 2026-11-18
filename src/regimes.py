import pandas as pd
from hmmlearn.hmm import GaussianHMM


def fit_regimes(features, n_states=2, seed=42):
    """Retourne une série de régimes. 0 = le plus calme (vol moyenne la plus basse)."""
    X = (features - features.mean()) / features.std()
    model = GaussianHMM(n_components=n_states, covariance_type="full",
                        n_iter=200, random_state=seed)
    model.fit(X.values)
    states = pd.Series(model.predict(X.values), index=features.index, name="regime")
    order = features["vol"].groupby(states).mean().sort_values().index
    return states.map({old: new for new, old in enumerate(order)})


if __name__ == "__main__":
    from src.data import get_prices
    from src.analytics import log_returns, realized_vol

    prices = get_prices(["HYG"])["HYG"]
    ret = log_returns(prices)
    vol = realized_vol(ret)
    feats = pd.DataFrame({"ret": ret, "vol": vol}).dropna()

    reg = fit_regimes(feats)
    print("Part des jours par régime :")
    print(reg.value_counts(normalize=True).round(3))
    print("\nVol moyenne par régime :")
    print(feats["vol"].groupby(reg).mean().round(3))
    print("\nCovid (9-31 mars 2020), jours par régime :")
    print(reg.loc["2020-03-09":"2020-03-31"].value_counts())

    m = feats["vol"].groupby(reg).mean()
    assert m.loc[0] < m.loc[1], "le régime 0 doit être le plus calme"
    print("\nOK regimes")
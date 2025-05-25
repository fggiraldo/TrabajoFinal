import pytest
import pandas as pd
from src.preprocessing.recopilacion import obtener_crypto_yfinance
from datetime import datetime, timedelta

def test_obtener_crypto_yfinance():
    tickers = ["BTC-USD", "ETH-USD"]
    fecha_fin = datetime.today().strftime('%Y-%m-%d')
    fecha_inicio = (datetime.today() - timedelta(days=10)).strftime('%Y-%m-%d')
    df = obtener_crypto_yfinance(tickers, fecha_inicio, fecha_fin)
    # Verifica que el resultado sea un DataFrame
    assert isinstance(df, pd.DataFrame)
    # Verifica que las columnas incluyan los tickers
    for ticker in tickers:
        assert ticker in df.columns
    # Verifica que el DataFrame no esté vacío
    assert not df.empty

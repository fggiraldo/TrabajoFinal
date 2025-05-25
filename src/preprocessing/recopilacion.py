import yfinance as yf
import pandas as pd
from pipeline.config import TICKERS

def obtener_crypto_yfinance(
    ticker: list[str], fecha_inicio: str, fecha_fin: str
) -> pd.DataFrame:
    """Obtiene los datos de los tickers de yfinance.

    Parameters
    ----------
    ticker : list[str]
        Lista de tickers de yfinance.
    fecha_inicio : str
        Fecha de inicio en formato 'YYYY-MM-DD'.
    fecha_fin : str
        Fecha de fin en formato 'YYYY-MM-DD'.

    Returns
    -------
    pd.DataFrame
        DataFrame con los precios de cierre de los tickers de yfinance.
    """
    df = yf.download(ticker, start=fecha_inicio, end=fecha_fin)

    # Seleccionar solamente los precios al cierre del día
    df = df.Close

    return df
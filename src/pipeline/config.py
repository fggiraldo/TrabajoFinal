"""Config file para el preprocesamiento."""
from pathlib import Path

# Obtener la ruta absoluta del directorio del proyecto
ROOT_DIR = Path(__file__).parent.parent.parent
DATA_DIR = ROOT_DIR / "src" / "data" / "raw"

TICKERS = ["BTC-USD","ETH-USD","USDT-USD","XRP-USD","BNB-USD","SOL-USD","DOGE-USD","ADA-USD","TRX-USD","LTC-USD"]

RUTA_MODELOS = str(ROOT_DIR / "src/models")

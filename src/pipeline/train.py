"""Script de entrenamiento para el modelo Prophet."""
import argparse
import json
import logging
import os
import sys
from datetime import datetime
from typing import Dict, Tuple

import joblib
import numpy as np
import pandas as pd
from prophet import Prophet
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def guardar_modelo(modelo, tick, metricas, directorio=None):
    """
    Guarda el modelo Prophet y las métricas en el directorio especificado.

    Args
    ----
        modelo: Modelo Prophet entrenado.
        tick: Ticker de la acción (str).
        metricas: Diccionario de métricas.
        directorio: Carpeta donde guardar los archivos. Si es None, usa RUTA_MODELOS.
    """
    from src.pipeline.config import RUTA_MODELOS

    if directorio is None:
        directorio = RUTA_MODELOS
    os.makedirs(directorio, exist_ok=True)
    modelo_path = os.path.join(directorio, f"prophet_{tick}.joblib")
    metricas_path = os.path.join(directorio, f"metricas_{tick}.json")
    joblib.dump(modelo, modelo_path)
    with open(metricas_path, "w") as f:
        json.dump(metricas, f)
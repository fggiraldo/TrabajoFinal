"""Pruebas para el módulo de inferencia."""
import os
import shutil

import numpy as np
import pandas as pd
import pytest
from prophet import Prophet

from src.pipeline.config import RUTA_MODELOS

from src.pipeline.inference import (
    cargar_modelo,
    guardar_prediccion,
    realizar_prediccion,
    visualizar_prediccion,
)
from src.pipeline.train import guardar_modelo




@pytest.fixture(scope="module", autouse=True)
def setup_and_teardown():
    """Fixture para crear y eliminar carpeta temporal."""
    # Crear carpeta temporal antes de los tests
    os.makedirs(RUTA_MODELOS, exist_ok=True)
    yield
    # Eliminar carpeta temporal después de los tests
    shutil.rmtree(RUTA_MODELOS, ignore_errors=True)


@pytest.fixture
def modelo_prueba():
    """Fixture para crear un modelo de prueba."""
    fechas = pd.date_range(start="2020-01-01", end="2020-12-31", freq="D")
    np.random.seed(42)
    valores = np.random.normal(100, 10, len(fechas)).cumsum()
    df = pd.DataFrame({"ds": fechas, "y": valores})
    modelo = Prophet()
    modelo.fit(df)
    return modelo


def test_cargar_modelo(modelo_prueba):
    """Prueba para cargar un modelo."""
    metricas = {"mse": 0.0, "rmse": 0.0, "mae": 0.0, "r2": 1.0}
    guardar_modelo(modelo_prueba, "ETH-USD", metricas, RUTA_MODELOS)
    modelo = cargar_modelo("ETH-USD")
    assert isinstance(modelo, Prophet)


def test_cargar_modelo_no_existe():
    """Prueba para cargar un modelo que no existe."""
    with pytest.raises(FileNotFoundError):
        cargar_modelo("MODELO_INEXISTENTE")


def test_realizar_prediccion(modelo_prueba):
    """Prueba para realizar una predicción."""
    predicciones = realizar_prediccion(modelo_prueba, "2021-01-01", "2021-01-31")
    assert isinstance(predicciones, pd.DataFrame)
    assert "ds" in predicciones.columns
    assert "yhat" in predicciones.columns
    assert "yhat_lower" in predicciones.columns
    assert "yhat_upper" in predicciones.columns
    assert len(predicciones) > 0


def test_visualizar_prediccion(modelo_prueba):
    """Prueba para visualizar una predicción."""
    predicciones = realizar_prediccion(modelo_prueba, "2021-01-01", "2021-01-31")
    visualizar_prediccion(
        predicciones, "ETH-USD", "2021-01-01", "2021-01-31", directorio=RUTA_MODELOS
    )
    archivos = os.listdir(RUTA_MODELOS)
    assert any(
        f.startswith("prediccion_ETH-USD_") and f.endswith(".png") for f in archivos
    )


def test_guardar_prediccion(modelo_prueba):
    """Prueba para guardar una predicción."""
    predicciones = realizar_prediccion(modelo_prueba, "2021-01-01", "2021-01-31")
    guardar_prediccion(
        predicciones, "ETH-USD", "2021-01-01", "2021-01-31", directorio=RUTA_MODELOS
    )
    archivos = os.listdir(RUTA_MODELOS)
    assert any(
        f.startswith("prediccion_ETH-USD_") and f.endswith(".parquet") for f in archivos
    )

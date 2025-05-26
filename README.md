# Trabajo final: Metodología para Data Science

La inversión en `criptomonedas` es una estrategia atractiva debido a su alta rentabilidad potencial, pero conlleva riesgos significativos como volatilidad extrema, regulación incierta y riesgos de seguridad. Este trabajo busca evaluar cómo distribuir un capital de S/1,000,000 en un portafolio diversificado de criptomonedas para maximizar el rendimiento y minimizar el riesgo.

## Dataset

El dataset utilizado es el [Criptomonedas - yfinance], la data de yfinance sobre criptomonedas incluye varios campos clave que permiten analizar el comportamiento del mercado.

1️⃣ Precio de cierre (Close) – Último precio registrado en el período seleccionado.
2️⃣ Precio de apertura (Open) – Precio al inicio del período.
3️⃣ Precio más alto (High) – Máximo alcanzado en el período.
4️⃣ Precio más bajo (Low) – Mínimo registrado en el período.
5️⃣ Volumen (Volume) – Cantidad de criptomonedas negociadas.
6️⃣ Capitalización de mercado (Market Cap) – Valor total de la criptomoneda en circulación.
7️⃣ Variación porcentual (Change %) – Cambio en el precio respecto al período anterior.

## Estructura del Proyecto
```
├── data/                 # Datos originales y procesados
│   ├── raw/              # Datos originales
│   └── processed/        # Datos procesados
├── notebooks/            # Jupyter notebooks con el análisis
├── src/                  # Código fuente
│   ├── preprocessing/    # Scripts de limpieza y procesamiento
│   ├── features/         # Feature engineering
│   └── test/             # Test
├── reports/              # Reportes y visualizaciones
├── .github/              # Configuración de GitHub
│   └── workflows/        # GitHub Actions workflows
├── .pre-commit-config.yaml # Configuración de pre-commit hooks
├── tests/                # Tests unitarios y de integración
└── README.md             # Este archivo
```

## Entregables

### 1. Descripción del Problema

### 2. Metodología Científica

### 3. Código Fuente

### 4. Experimentación

### 5. Validación y Pruebas


## Entregables

Cada estudiante deberá:
1. Crear ramas descriptivas para cada tarea
2. Realizar commits con mensajes significativos
3. Documentar el proceso en el README.md
4. Crear un pull request final que incluya:
   - Descripción de cambios realizados
   - Justificación de decisiones
   - Resultados obtenidos
   - Visualizaciones relevantes
   - Evidencia de que los tests pasan correctamente



## Recursos Adicionales

- [Documentación de Git](https://git-scm.com/doc)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)
- [Pytest Documentation](https://docs.pytest.org/)
- [Pre-commit Documentation](https://pre-commit.com/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

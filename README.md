# Trabajo Final: Metodología para Data Science

## Descripción del Proyecto

Este proyecto consiste en el análisis de un dataset de bonos del tesoro, donde el objetivo es predecir el riesgo que existe en la inversion. El objetivo principal es practicar el flujo completo de un proyecto de data science, desde la limpieza y manipulación de datos hasta la preparación para modelado, tal como vimos en clase, utilizando Git como herramienta principal de control de versiones.

## Objetivos del Proyecto
1. Analizar el comportamiento histórico de la inversion en el bono del tesoro opciones de inversión
2. Desarrollar modelos predictivos para estimar rendimientos futuros en el horizonte de 8 años
3. Implementar algoritmos de optimización de portafolio considerando el presupuesto disponible
4. Evaluar y comparar las diferentes estrategias de inversión
5. Generar recomendaciones basadas en el perfil de riesgo del inversionista y el horizonte temporal definido

## Dataset

El dataset utilizado es el [Bcrp](https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PD04719XD/json), que contiene información sobre los bonos del tesoro pubico.

## Estructura del Proyecto
```
├── data/                  # Datos originales y procesados
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

## Tareas a Realizar



## Recursos Adicionales

- [Documentación de Git](https://git-scm.com/doc)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)
- [Pytest Documentation](https://docs.pytest.org/)
- [Pre-commit Documentation](https://pre-commit.com/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

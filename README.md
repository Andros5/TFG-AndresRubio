# TFG - Andrés Rubio

Este repositorio contiene el código, datos y resultados desarrollados para el Trabajo Fin de Grado (TFG) titulado **"Análisis Formal de Conceptos como Herramienta para la Explicabilidad en Modelos de Aprendizaje Automático"**.

El objetivo del TFG es aplicar técnicas del **Análisis Formal de Conceptos (AFC)** para la **extracción y uso de implicaciones lógicas** en conjuntos de datos, con énfasis en la explicabilidad de decisiones automáticas. Se analiza el comportamiento de dichas implicaciones en distintos contextos, centrándose especialmente en cómo varían los resultados al ajustar parámetros como el soporte y la confianza.

Se utilizan dos conjuntos de datos reales: el conocido dataset **Titanic** y el dataset de **Churn Modelling** (fuga de clientes). Ambos han sido discretizados y tratados para permitir la generación de implicaciones a través de herramientas como **ConExp** y el análisis de su impacto en predicciones.

---

## 🔧 Estructura del repositorio

Este repositorio se divide en dos carpetas principales:

- [`titanic/`](#-titanic)
- [`churn_modelling/`](#-churn-modelling)

---

## 📁 Titanic

Contiene todos los notebooks, datos y resultados relacionados con el análisis basado en el dataset Titanic.

### Archivos principales:

- **`ajusteHiperparametrosModeloXAI.ipynb`**  
  Notebook encargado del ajuste de hiperparámetros como soporte, confianza, número de rangos de edad y de tarifa. Relacionado con el **capítulo 5, sección 4** de la memoria.

- **`entregaKaggleModeloXAI.ipynb`**  
  Notebook que genera el CSV de predicción para Kaggle. Contiene dos versiones del modelo:
  - Versión clásica utilizada en el **capítulo 5, sección 3**, con un **accuracy de 0.75598**.
  - Segunda versión alternativa (no incluida en la memoria) basada en comparar la **confianza de las implicaciones de `Survives` vs. `NotSurvived`**, alcanzando un **accuracy de 0.77511**.

- **`modeloXAI.ipynb`**  
  Modelo base empleado para los cálculos y predicciones. Utilizado en el **capítulo 4**, en las primeras secciones del **capítulo 5** y durante todo el **capítulo 6**. Es el modelo de referencia para hacer pruebas y generar nuevos resultados.

- **`resultados.txt`**  
  Registro de pruebas intermedias y anotaciones realizadas durante la fase de desarrollo del modelo antes de consolidar los resultados en la memoria final.

### Carpetas:

- **`conjuntos_entrenamiento/`**  
  Contiene variaciones y discretizaciones del conjunto de entrenamiento original en formato CSV. Se usaron para probar distintos cortes de edad y tarifa.

- **`conjuntos_prueba/`**  
  Contiene conjuntos de prueba discretizados, compatibles con los entrenamientos generados.

- **`resultados/`**  
  Archivos con resultados de implicaciones, predicciones y análisis diversos generados durante los experimentos descritos en la memoria.

- **`titanic.zip`**  
  ZIP descargado desde Kaggle con los datasets `train.csv` y `test.csv` originales.

---

## 📁 Churn Modelling

Conjunto de experimentos realizados sobre el dataset de fuga de clientes, aplicando también el enfoque AFC.

### Archivos principales:

- **`churnModellingNotebook.ipynb`**  
  Notebook que utiliza las implicaciones generadas por **ConExp** y las adapta a una estructura de análisis definida en la clase `Context` (descrita en la memoria). Se realizan cálculos sobre:
  - Frecuencia de implicaciones.
  - Falsos positivos y falsos negativos.
  - Variaciones según umbrales de **confianza y soporte**.

- **`pasarAConExp.py`**  
  Script en Python para transformar datasets discretizados en formato `.cxt`, el cual es requerido por ConExp para generar las implicaciones.

### Carpetas:

- **`ConExpDatos/`**  
  - `.cxt`: contexto en formato formal para ConExp generado desde el conjunto de entrenamiento.  
  - `.txt`: archivo con todas las implicaciones generadas por ConExp desde el `.cxt`.

- **`conjuntos_entrenamiento/`**  
  Variaciones discretizadas del conjunto de entrenamiento de 8000 instancias.

- **`conjuntos_prueba/`**  
  Variaciones discretizadas del conjunto de prueba.

- **`resultados/`**  
  Resultados de análisis similares a los realizados con el dataset Titanic.

- **`churn_modelling_dataset.zip`**  
  Contiene el CSV original con 1000 registros descargados desde Kaggle.

---

## 📚 Tecnologías y herramientas utilizadas

- Python 3.10+
- Jupyter Notebooks
- ConExp (software para cálculo de implicaciones en AFC)
- Pandas, Numpy, Scikit-learn (preprocesamiento)
- Kaggle (datasets y evaluación)
- Matplotlib, Seaborn (visualización de datos)

---

## 🧾 Licencia

Este proyecto está licenciado bajo la **Licencia MIT**. Puedes consultarla en el archivo [`LICENSE`](./LICENSE) para más detalles. Esto permite el uso, modificación y distribución del código con fines académicos o personales, siempre que se reconozca la autoría original.

---

## ✉️ Contacto

Si tienes dudas sobre el contenido de este repositorio o el trabajo presentado, puedes contactarme a través de GitHub o mediante los datos de contacto proporcionados en la memoria del TFG.

---

## 🔗 Referencias

- [Análisis Formal de Conceptos - Wikipedia](https://es.wikipedia.org/wiki/An%C3%A1lisis_formal_de_conceptos)
- [ConExp - FCA Software Tool](https://github.com/xflr6/concepts)
- [Dataset Titanic - Kaggle](https://www.kaggle.com/c/titanic)
- [Dataset Churn Modelling - Kaggle](https://www.kaggle.com/datasets/shubhendra7/churn-modelling)


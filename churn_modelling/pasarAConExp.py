import pandas as pd


def csv_to_cxt(csv_path, cxt_path, id_col=None):
    # Cargar el CSV
    df = pd.read_csv(csv_path)

    # Si hay una columna de ID, separamos los nombres de objeto
    if id_col and id_col in df.columns:
        object_names = df[id_col].astype(str).tolist()
        df = df.drop(columns=[id_col])
    else:
        object_names = [f"Obj{i+1}" for i in range(len(df))]

    attribute_names = df.columns.tolist()

    # Convertimos los valores binarios a "X" (presencia) o " " (ausencia)
    incidence_matrix = df.map(lambda x: 'X' if x == 'X' else '.').values.tolist()

    # Crear contenido del archivo .cxt
    lines = []
    lines.append("B")
    lines.append("")  # Línea vacía requerida por el formato
    lines.append(str(len(object_names)))
    lines.append(str(len(attribute_names)))
    lines.extend(object_names)
    lines.extend(attribute_names)
    for row in incidence_matrix:
        lines.append(''.join(row))

    # Guardar el archivo
    with open(cxt_path, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')

csv_to_cxt("C:/Users/andre/OneDrive/Documentos/Universidad/TFG/codigo/churn_modelling/train_data_cm.csv", "conexp_train_data_cm.cxt", id_col="RowNumber")

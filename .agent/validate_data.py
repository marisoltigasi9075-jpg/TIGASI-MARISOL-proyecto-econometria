from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_FOLDER = PROJECT_ROOT / "data"

def find_csv():
    """
    Busca automáticamente el primer archivo CSV dentro de la carpeta data.
    """
    csv_files = list(DATA_FOLDER.rglob("*.csv"))

    if len(csv_files) == 0:
        return None

    return csv_files[0]


def validate_data():

    report = []

    csv_file = find_csv()

    if csv_file is None:
        report.append("❌ No se encontró ningún archivo CSV.")
        return report

    report.append(f"✅ Archivo encontrado: {csv_file.name}")

    try:
        df = pd.read_csv(csv_file)
    except Exception as e:
        report.append(f"❌ Error al leer el archivo: {e}")
        return report

    report.append(f"✅ Filas: {len(df)}")
    report.append(f"✅ Columnas: {len(df.columns)}")

    if df.isnull().sum().sum() == 0:
        report.append("✅ No existen valores nulos.")
    else:
        report.append(f"⚠ Existen {df.isnull().sum().sum()} valores nulos.")

    duplicados = df.duplicated().sum()

    if duplicados == 0:
        report.append("✅ No existen registros duplicados.")
    else:
        report.append(f"⚠ Existen {duplicados} registros duplicados.")

    return report
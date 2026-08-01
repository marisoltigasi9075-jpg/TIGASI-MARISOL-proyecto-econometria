from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

SCRIPTS = [
    "src/obtener_datos.py",
    "src/limpiar_datos.py",
    "src/estimar_modelo.py",
    "src/generar_resultados.py"
]


def validate_code():

    report = []

    for script in SCRIPTS:

        file = PROJECT_ROOT / script

        if file.exists():

            report.append(f"✅ {script}")

        else:

            report.append(f"❌ Falta {script}")

    return report
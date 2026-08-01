"""
====================================================
AGENTE GUARDIÁN DEL PROYECTO
Proyecto: Econometría VAR - Ecuador
Autor: Marisol Veronica Tigasi Ugsha
====================================================
"""

from validate_project import validate_structure
from validate_data import validate_data
from validate_code import validate_code
from report import save_report

print("=" * 55)
print("        AGENTE GUARDIÁN DEL PROYECTO")
print("=" * 55)

report = []

print("\n1. Verificando estructura del proyecto...\n")

for folder, status in validate_structure():

    if status:
        text = f"✅ Carpeta encontrada: {folder}"
    else:
        text = f"❌ Carpeta faltante: {folder}"

    print(text)
    report.append(text)

print("\n2. Verificando base de datos...\n")

for line in validate_data():

    print(line)
    report.append(line)

print("\n3. Verificando scripts del proyecto...\n")

for line in validate_code():

    print(line)
    report.append(line)

print("\n4. Generando reporte...\n")

save_report(report)

print("\n✔ VALIDACIÓN FINALIZADA CORRECTAMENTE")
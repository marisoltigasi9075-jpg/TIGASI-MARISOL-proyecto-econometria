from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

OUTPUT = PROJECT_ROOT / "outputs" / "agent_report.txt"


def save_report(lines):

    OUTPUT.parent.mkdir(exist_ok=True)

    with open(OUTPUT, "w", encoding="utf-8") as f:

        f.write("REPORTE DEL AGENTE\n")
        f.write("=" * 50 + "\n\n")

        for line in lines:

            f.write(line + "\n")

    print("\nReporte generado correctamente.")
    print(OUTPUT)
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

FOLDERS = [
    "data",
    "outputs",
    "notebooks",
    "dashboard",
    "paper",
    "src",
    "prompts"
]

def validate_structure():
    """
    Verifica que existan las carpetas principales del proyecto.
    """

    results = []

    for folder in FOLDERS:

        path = PROJECT_ROOT / folder

        if path.exists():
            results.append((folder, True))
        else:
            results.append((folder, False))

    return results
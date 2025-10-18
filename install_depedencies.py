import subprocess
import sys

# Lista wszystkich wymaganych bibliotek z dokładnymi wersjami
packages = [
    "PyQt6==6.9.1",
    "PyQt6-Qt6==6.9.2",
    "PyQt6_sip==13.10.2",
    "qt-material==2.17",
    "reportlab==4.4.4",
    "num2words==0.5.14",
    "SQLAlchemy==2.0.44",
    "pandas==2.2.3",
    "openpyxl==3.1.5",
    "pillow==11.3.0",
    "striprtf==0.0.29",
    "Jinja2==3.1.6",
    "cx_Freeze==8.4.1",
    "greenlet==3.2.4",
    "filelock==3.20.0",
    "typing_extensions==4.15.0",
    "babel==2.16.0",          # formatowanie dat / walut
    "xlsxwriter==3.2.0",      # eksport do XLSX
    "matplotlib==3.9.3",      # wykresy i statystyki
    "python-docx==1.1.2"      # eksport do DOCX
]

print("📦 Instalowanie wymaganych bibliotek...")

for package in packages:
    print(f"➡️  Instaluję: {package}")
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

print("\n✅ Wszystkie biblioteki zostały pomyślnie zainstalowane dla Python", sys.version.split()[0])

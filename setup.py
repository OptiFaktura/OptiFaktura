import sys
import os
from cx_Freeze import setup, Executable

# --- Ścieżka do ikony ---
ICON_PATH = r"C:\Users\Rostyslav Oleshchuk\Downloads\logo.ico"

# --- Ustawienia build ---
build_exe_options = {
    "packages": ["os", "sys", "sqlite3", "PyQt6"],
    "include_files": [
        ("ui", "ui"),
        ("models", "models"),
        (ICON_PATH, "logo.ico"),  # kopiujemy ikonę do katalogu aplikacji
    ],
    "excludes": ["tkinter"],
}

# --- Skróty (Menu Start + Pulpit) ---
shortcut_table = [
    # Skrót w Menu Start
    ("OptiFakturaStartShortcut",
     "ProgramMenuFolder",
     "OptiFaktura",
     "TARGETDIR",
     "[#OptiFaktura.exe]",
     None,
     "Program do wystawiania faktur VAT",
     None,
     "logo.ico",  # nazwa po skopiowaniu do folderu aplikacji
     0,
     "TARGETDIR",
     None),

    # Skrót na pulpicie
    ("OptiFakturaDesktopShortcut",
     "DesktopFolder",
     "OptiFaktura",
     "TARGETDIR",
     "[#OptiFaktura.exe]",
     None,
     "Program do wystawiania faktur VAT",
     None,
     "logo.ico",
     0,
     "TARGETDIR",
     None)
]

# --- Dane MSI ---
msi_data = {"Shortcut": shortcut_table}

# --- Opcje MSI ---
bdist_msi_options = {
    "upgrade_code": "{12345678-ABCD-1234-ABCD-1234567890AB}",
    "add_to_path": False,
    "data": msi_data,
    "install_icon": ICON_PATH,  # ta sama ikona co aplikacja
    "all_users": True,          # instaluje w Program Files
    "initial_target_dir": r"[ProgramFilesFolder]\OptiFaktura",
}

# --- Aplikacja ---
executables = [
    Executable(
        script="main.py",
        base="Win32GUI",
        target_name="OptiFaktura.exe",
        icon=ICON_PATH  # ikona aplikacji
    )
]

# --- Setup ---
setup(
    name="OptiFaktura",
    version="1.0.0",
    description="Program do wystawiania faktur VAT",
    author="OptiFaktura",
    options={
        "build_exe": build_exe_options,
        "bdist_msi": bdist_msi_options
    },
    executables=executables
)

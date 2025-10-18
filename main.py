import sys
import os
import shutil
from pathlib import Path
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow
from models.database import Database


def get_user_data_path():
    """Zwraca ścieżkę do folderu AppData dla danych programu."""
    appdata = Path(os.getenv("APPDATA"))
    app_dir = appdata / "OptiFaktura"
    app_dir.mkdir(exist_ok=True)
    return app_dir


def main():
    app = QApplication(sys.argv)

    # --- Ścieżka bazy danych ---
    user_db_path = get_user_data_path() / "opti_faktura.db"

    # Jeśli nie istnieje, skopiuj bazę z folderu programu
    exe_dir = Path(os.path.dirname(os.path.abspath(sys.argv[0])))
    source_db = exe_dir / "opti_faktura.db"

    if not user_db_path.exists() and source_db.exists():
        try:
            shutil.copy(source_db, user_db_path)
        except Exception as e:
            print(f"Błąd kopiowania bazy danych: {e}")

    db = Database(str(user_db_path))
    window = MainWindow(db)
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()

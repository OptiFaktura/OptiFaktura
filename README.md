# OptiFaktura: Desktopowy Dziennik i System Faktur 📊

**OptiFaktura** to nowoczesna, hybrydowa aplikacja desktopowa, zaprojektowana w celu usprawnienia pracy nauczycieli i małych firm. Łączy w sobie moduł rozbudowanego **dziennika szkolnego** (zarządzanie uczniami, ocenami, frekwencją, planem lekcji) z możliwością wystawiania **faktur**.

Aplikacja jest zbudowana na solidnym połączeniu **Electrona** (dla interfejsu graficznego) oraz **Pythona 3.11+ (z PySide6)** dla całej logiki biznesowej i zarządzania bazą danych (SQLite).

---

## Główne Funkcje (Python Backend)

* **Zarządzanie Użytkownikami:** Bezpieczne haszowanie haseł (PBKDF2-HMAC-SHA256) dla kont nauczycieli/użytkowników.
* **Dziennik Szkolny:** Pełne zarządzanie listami uczniów, dodawanie wpisów, statusów obecności (np. obecny, spóźniony, ucieczka) i ocen.
* **Generator Planu Lekcji:** Tworzenie i druk/eksport planów lekcji.
* **Trwała Pamięć:** Użycie **SQLite3** do lokalnego przechowywania wszystkich danych.
* **Obsługa Zasobów:** Dynamiczne ładowanie zasobów (np. czcionek **`FreeSans.ttf`**) i bezpieczne przechowywanie danych w folderze **`%APPDATA%`** po instalacji.

---

## 🛠️ Architektura i Użyte Technologie

OptiFaktura działa jako aplikacja hybrydowa, gdzie dwa procesy komunikują się ze sobą:

| Warstwa | Technologia | Funkcja |
| :--- | :--- | :--- |
| **Frontend (GUI)** | **Electron (Node.js/JS/HTML/CSS)** | Tworzy główne okno, renderuje interfejs. |
| **Backend (Logika)** | **Python (PySide6 / SQLite3)** | Obsługuje bazę danych, hasła, logikę biznesową, generowanie PDF. |
| **Komunikacja** | **`child_process.spawn`** (Node.js) | Uruchamia plik `optifaktura_python.exe` i wymienia dane. |
| **Pakowanie** | **PyInstaller** (dla Pythona) | Pakuje plik `main.py` do przenośnego `optifaktura_python.exe` (z flagą `--noconsole`). |
| **Instalator** | **Electron-Builder (Node.js)** | Generuje finalny instalator Windows (NSIS/MSI) z pakietem Electrona i binarką Pythona w folderze `resources/bin`. |

---
## 🖥️Ważne komendy bez których nie zadziała budowanie do .msi

- py -3.12 -m pip install --upgrade pip
- py -3.12 -m pip install cx_Freeze PyQt6 PyQt6-Qt6 PyQt6-sip sqlalchemy reportlab qt-material
- py -3.12 setup.py bdist_msi
---
## 👋 Kontakt i Współpraca

Poniżej znajdziesz status projektu i listę zadań. Zapraszamy do wkładu!

- 🔭 I’m currently working on: **Finalizowaniu instalatorów MSI/EXE** i rozwiązywaniu problemów ze ścieżkami zasobów w środowisku spakowanym.
- 🌱 I’m currently learning: **Zaawansowane techniki pakowania** aplikacji hybrydowych Electron+Python oraz **optymalizację zapytań SQLite**.
- 👯 I’m looking to collaborate on: **Frontend (JS/CSS)** dla widoków w Electronie oraz **projektowanie interfejsu** użytkownika (UI/UX).
- 🤔 I’m looking for help with: **Integracją WiX Toolset** w Electron-Builderze do stabilnego tworzenia pakietów **MSI**.
- 💬 Ask me about: **Łączenie procesów Node.js i Pythona** oraz prawidłowe zarządzanie ścieżkami w aplikacjach desktopowych.
- 📫 How to reach me: Otwórz **Issue** w tym repozytorium.
- 😄 Pronouns: On/Jego
- ⚡ Fun fact: Nasz backend Pythonowy potrafi dynamicznie generować **czytelne PDF-y z fakturami**!

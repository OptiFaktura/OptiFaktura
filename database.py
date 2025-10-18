import sqlite3
import os

class Database:
    def __init__(self, db_path="opti_faktura.db"):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        self._init_schema()

    def _init_schema(self):
        cur = self.conn.cursor()

        # przykładowe tabele (możesz rozszerzyć według swoich modeli)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS firma (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nazwa TEXT,
                nip TEXT,
                adres TEXT,
                konto TEXT,
                email TEXT,
                telefon TEXT,
                logo_path TEXT,
                motyw TEXT
            )
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS kontrahenci (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nazwa TEXT,
                nip TEXT,
                adres TEXT,
                email TEXT
            )
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS towary (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nazwa TEXT,
                jednostka TEXT,
                cena_netto REAL,
                vat REAL
            )
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS faktury (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                numer TEXT,
                data_wystawienia TEXT,
                data_sprzedazy TEXT,
                kontrahent_id INTEGER,
                suma_brutto REAL,
                FOREIGN KEY(kontrahent_id) REFERENCES kontrahenci(id)
            )
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS faktura_pozycje (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                faktura_id INTEGER,
                opis TEXT,
                ilosc REAL,
                cena_netto REAL,
                vat REAL,
                rabat REAL,
                FOREIGN KEY(faktura_id) REFERENCES faktury(id)
            )
        """)

        self.conn.commit()

    def execute(self, query, params=()):
        cur = self.conn.cursor()
        cur.execute(query, params)
        self.conn.commit()
        return cur

    def query(self, query, params=()):
        cur = self.conn.cursor()
        cur.execute(query, params)
        return cur.fetchall()

    def close(self):
        self.conn.close()


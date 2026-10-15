import sqlite3

forbindelse = sqlite3.connect("traening.db")

forbindelse.execute("""
CREATE TABLE IF NOT EXISTS ovelser (
    id INTEGER PRIMARY KEY,
    navn TEXT NOT NULL,
    dag TEXT NOT NULL,
    muskelgruppe TEXT NOT NULL,
    saet INTEGER NOT NULL,
    rep_min INTEGER,
    rep_max INTEGER,
    type TEXT NOT NULL
)
""")

forbindelse.execute("""
CREATE TABLE IF NOT EXISTS log (
    id INTEGER PRIMARY KEY,
    ovelse_id INTEGER NOT NULL REFERENCES ovelser(id),
    dato TEXT NOT NULL,
    kg REAL,
    reps INTEGER,
    minutter INTEGER
)
""")

forbindelse.commit()
forbindelse.close()
print("Databasen er klar")
import sqlite3

forbindelse = sqlite3.connect("traening.db")




forbindelse.execute("""
INSERT INTO ovelser (navn, dag, muskelgruppe, saet, rep_min, rep_max, type)
VALUES ('Bænkpres', 'mandag', 'bryst', 2, 8, 12, 'styrke'),
       ('Lat pulldown', 'onsdag', 'ryg', 2, 8, 12, 'styrke'),
       ('Løbebånd', 'fredag', 'cardio', 1, NULL, NULL, 'cardio')
""")

forbindelse.execute("""
INSERT INTO log (ovelse_id, dato, kg, reps, minutter)
VALUES (1, '2026-10-12', 80, 8, NULL),
       (2, '2026-10-14', 69, 8, NULL),
       (3, '2026-10-16', NULL, NULL, 30)
""")

forbindelse.commit()
forbindelse.close()
print("Program indsat")
import sqlite3

conn = sqlite3.connect("database/inventory.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sku (
    sku_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sku_name TEXT UNIQUE,
    inventory_type TEXT,
    category TEXT,
    unit TEXT,
    min_required_qty INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS location (
    location_id INTEGER PRIMARY KEY AUTOINCREMENT,
    location_name TEXT,
    location_type TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS inventory_ledger (
    ledger_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sku_id INTEGER,
    location_id INTEGER,
    movement_type TEXT,
    quantity_change INTEGER,
    movement_date TEXT,
    reference TEXT
)
""")

conn.commit()
conn.close()

print("Database initialized")

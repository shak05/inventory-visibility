import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DB_PATH = os.path.join(BASE_DIR, "database", "inventory.db")

from datetime import datetime
import sqlite3

DB = "database/inventory.db"

def inbound(sku_id, location_id, qty, ref):
    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO inventory_ledger
        VALUES (NULL, ?, ?, 'INBOUND', ?, ?, ?)
    """, (sku_id, location_id, qty, datetime.now().isoformat(), ref))

    conn.commit()
    conn.close()

def consume(sku_id, location_id, qty, ref):
    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO inventory_ledger
        VALUES (NULL, ?, ?, 'CONSUMPTION', ?, ?, ?)
    """, (sku_id, location_id, -qty, datetime.now().isoformat(), ref))

    conn.commit()
    conn.close()

def transfer(sku_id, from_loc, to_loc, qty, ref):
    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()
    now = datetime.now().isoformat()

    cursor.execute("""
        INSERT INTO inventory_ledger VALUES
        (NULL, ?, ?, 'TRANSFER_OUT', ?, ?, ?)
    """, (sku_id, from_loc, -qty, now, ref))

    cursor.execute("""
        INSERT INTO inventory_ledger VALUES
        (NULL, ?, ?, 'TRANSFER_IN', ?, ?, ?)
    """, (sku_id, to_loc, qty, now, ref))

    conn.commit()
    conn.close()

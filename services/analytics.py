import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DB_PATH = os.path.join(BASE_DIR, "database", "inventory.db")

import pandas as pd
import sqlite3

def inventory_snapshot():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("""
        SELECT s.sku_name, s.inventory_type, l.location_name,
               SUM(il.quantity_change) AS quantity
        FROM inventory_ledger il
        JOIN sku s ON il.sku_id = s.sku_id
        JOIN location l ON il.location_id = l.location_id
        GROUP BY s.sku_name, l.location_name
    """, conn)
    conn.close()
    return df

def inventory_aging():
    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql("""
        SELECT s.sku_name, s.inventory_type,
               MAX(il.movement_date) AS last_move
        FROM inventory_ledger il
        JOIN sku s ON il.sku_id = s.sku_id
        GROUP BY s.sku_name
    """, conn)

    df["last_move"] = pd.to_datetime(df["last_move"])
    df["age_days"] = (pd.Timestamp.now() - df["last_move"]).dt.days

    df = df[df["inventory_type"].isin(["Consumable", "Spare"])]
    conn.close()
    return df

def safety_compliance():
    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql("""
        SELECT s.sku_name, SUM(il.quantity_change) AS qty, s.min_required_qty
        FROM inventory_ledger il
        JOIN sku s ON il.sku_id = s.sku_id
        WHERE s.inventory_type = 'Safety'
        GROUP BY s.sku_name
    """, conn)

    df["status"] = df.apply(
        lambda x: "RISK" if x.qty < x.min_required_qty else "OK", axis=1
    )

    conn.close()
    return df

print("USING DB:", DB_PATH)

import sqlite3
from datetime import datetime, timedelta

conn = sqlite3.connect("database/inventory.db")
cursor = conn.cursor()

now = datetime.now()

# Inbound Consumable (O_RING → sku_id = 1)
cursor.execute("""
INSERT INTO inventory_ledger
(sku_id, location_id, movement_type, quantity_change, movement_date, reference)
VALUES (1, 1, 'INBOUND', 100, ?, 'PO-001')
""", ((now - timedelta(days=40)).isoformat(),))

# Consumption
cursor.execute("""
INSERT INTO inventory_ledger
(sku_id, location_id, movement_type, quantity_change, movement_date, reference)
VALUES (1, 1, 'CONSUMPTION', -30, ?, 'JOB-101')
""", ((now - timedelta(days=10)).isoformat(),))

# Safety inventory (FIRE_EXT → sku_id = 3)
cursor.execute("""
INSERT INTO inventory_ledger
(sku_id, location_id, movement_type, quantity_change, movement_date, reference)
VALUES (3, 1, 'INBOUND', 3, ?, 'SAFETY-PO')
""", ((now - timedelta(days=5)).isoformat(),))

conn.commit()
conn.close()

print("Inventory movements inserted")

import sqlite3

conn = sqlite3.connect("database/inventory.db")
cursor = conn.cursor()

# SKUs with inventory types
cursor.execute("""
INSERT OR IGNORE INTO sku (sku_name, inventory_type, category, unit, min_required_qty)
VALUES ('O_RING', 'Consumable', 'Seals', 'nos', NULL)
""")

cursor.execute("""
INSERT OR IGNORE INTO sku VALUES (NULL, 'PUMP_MOTOR', 'Spare', 'Motors', 'nos', NULL)
""")

cursor.execute("""
INSERT OR IGNORE INTO sku VALUES (NULL, 'FIRE_EXT', 'Safety', 'Safety', 'nos', 5)
""")

# Locations
cursor.execute("""
INSERT OR IGNORE INTO location VALUES (NULL, 'Warehouse Kochi', 'Warehouse')
""")

cursor.execute("""
INSERT OR IGNORE INTO location VALUES (NULL, 'Field Rig 12', 'Field')
""")

conn.commit()
conn.close()

print("Seed data inserted")

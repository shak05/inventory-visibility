OFS Multi-Location Inventory Visibility Engine

📦 Project Overview

This project is a ledger-based inventory visibility system designed for Oil Field Services (OFS) operations.
It provides a unified view of inventory across multiple locations such as warehouses and field sites by tracking transaction-level inventory movements instead of storing static stock quantities.
The system is implemented as a Proof of Concept (PoC) focusing on inventory visibility, aging, dead stock identification, and safety compliance.

🎯 Objectives

Track inventory movements across multiple locations
Maintain a transaction-level inventory ledger
Derive real-time inventory snapshots
Calculate inventory aging and identify slow/dead stock
Monitor safety inventory compliance
Visualize key inventory insights through a dashboard

🧠 Key Concepts Used
SKU (Stock Keeping Unit)
A unique identifier representing a type of inventory item (for example: O_RING, PUMP_MOTOR).

Ledger-Based Inventory
Inventory quantities are not stored directly.
Every inventory change is recorded as a ledger entry, and the current stock is derived by aggregating these transactions.

Inventory Movements
Inbound – Stock received into a location
Consumption – Stock used or consumed
Transfer – Stock moved between locations (recorded as OUT + IN)

🏗️ System Architecture

User Action
↓
Inventory Movement (Inbound / Consume / Transfer)
↓
Inventory Ledger (Database)
↓
Analytics Layer (Snapshot, Aging, KPIs)
↓
Streamlit Dashboard

🗄️ Database Design
Tables
sku
Stores item master data.

sku_id
sku_name
inventory_type (Consumable, Spare, Safety, etc.)
category
unit
min_required_qty (used for safety inventory)

location
Stores location master data.
location_id
location_name
location_type (Warehouse, Field)

inventory_ledger
Stores all inventory transactions.
ledger_id
sku_id
location_id
movement_type
quantity_change
movement_date

reference

📊 Analytics & KPIs
Inventory Snapshot
Shows the current stock per SKU and location, derived from the inventory ledger.

Inventory Aging
Measures how long inventory has been inactive based on the last movement date.
0–30 days → Fresh
31–90 days → Slow-moving
90+ days → Dead stock

Safety Compliance
Flags safety inventory when the available quantity falls below the minimum required level.

📈 Dashboard Features

Built using Streamlit:
Inventory Snapshot table
Inventory Aging table
Safety Compliance table
Bar chart showing Inventory Quantity by SKU

🛠️ Tech Stack

Python
SQLite (used for PoC simplicity)
Pandas
Streamlit
Git & GitHub

▶️ How to Run the Project
1. Clone the repository
git clone https://github.com/
<your-username>/inventory-visibility-engine.git
cd inventory_visibility

2. Install dependencies
pip install -r requirements.txt

3. Initialize the database
python database/init_db.py
python database/seed_data.py

4. Insert inventory movements (example)
from services.movements import inbound, consume
inbound(1, 1, 100, "PO-001")
consume(1, 1, 30, "JOB-101")

5. Run the dashboard
streamlit run dashboard/app.py

🚀 Future Enhancements

API layer using FastAPI
PostgreSQL backend for production deployment
Demand forecasting for consumables
Predictive maintenance for spare parts
Role-based access control

📌 Key Takeaway

This project demonstrates how ledger-based design enables accurate, auditable, and scalable inventory visibility, similar to real-world ERP systems used in industrial supply chains.

👤 Author

Shakthi Sathish Krishnan
B.Tech Data Science
Mar Athanasius College of Engineering, Kothamangalam

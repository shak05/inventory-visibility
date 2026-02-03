import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from services.analytics import (
    inventory_snapshot,
    inventory_aging,
    safety_compliance
)


st.title("OFS Inventory Visibility System")

st.header("Inventory Snapshot")
st.dataframe(inventory_snapshot())

st.header("Aging (Consumables & Spares)")
st.dataframe(inventory_aging())

st.header("Safety Compliance")
st.dataframe(safety_compliance())

import matplotlib.pyplot as plt
from services.analytics import inventory_snapshot

st.subheader("Inventory Quantity by SKU")

# Get snapshot data
df = inventory_snapshot()

# Aggregate quantity by SKU
sku_qty = df.groupby("sku_name")["quantity"].sum()

# Plot
fig, ax = plt.subplots()
sku_qty.plot(kind="bar", ax=ax)

ax.set_xlabel("SKU")
ax.set_ylabel("Quantity")
ax.set_title("Current Inventory by SKU")

st.pyplot(fig)


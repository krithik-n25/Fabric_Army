import pandas as pd
import numpy as np
import random

# ------------------------------
# Base Configurations
# ------------------------------

FABRICS = ["Cotton", "Polyester", "Nylon", "Wool", "Kevlar", "Bamboo Fibre"]
REGIONS = ["Cold Desert", "Hot Desert", "Jungle", "Coastal", "High Altitude", "General Use"]

# Logical cost ranges by fabric
FABRIC_COST = {
    "Cotton": (200, 600),
    "Polyester": (150, 450),
    "Nylon": (300, 900),
    "Wool": (400, 1200),
    "Kevlar": (1200, 3500),
    "Bamboo Fibre": (250, 700)
}

# Transport difficulty factor by region
REGION_LOGISTICS = {
    "Cold Desert": (12, 30),
    "Hot Desert": (10, 25),
    "Jungle": (15, 40),
    "Coastal": (5, 15),
    "High Altitude": (20, 45),
    "General Use": (3, 10)
}

# Base demand pattern depending on climate & need
BASE_DEMAND = {
    "Cold Desert": (5000, 15000),
    "Hot Desert": (4000, 13000),
    "Jungle": (6000, 20000),
    "Coastal": (4500, 14000),
    "High Altitude": (5500, 18000),
    "General Use": (3000, 10000)
}

# ------------------------------
# Cluster Classification Rules
# ------------------------------
def classify_priority(cost, transport_time, demand, stock):
    """
    Determines supply priority:
    HIGH → High demand, low supply, long transport
    MEDIUM → Balanced
    LOW → Surplus supply or easy transport
    """
    if demand > stock * 1.2 and transport_time > 18:
        return "HIGH"
    elif stock > demand and transport_time < 10:
        return "LOW"
    else:
        return "MEDIUM"

# ------------------------------
# Dataset Generator
# ------------------------------
def generate_dataset(n=5000):
    data = []

    for _ in range(n):
        fabric = random.choice(FABRICS)
        region = random.choice(REGIONS)

        # realistic value generation
        cost = np.random.uniform(*FABRIC_COST[fabric])
        transport_time = np.random.uniform(*REGION_LOGISTICS[region])
        distance = round(transport_time * random.uniform(30, 80), 1) # km scale logic

        demand = np.random.uniform(*BASE_DEMAND[region])
        stock_available = np.random.uniform(demand * 0.4, demand * 1.6)
        supplier_rating = round(np.random.uniform(1, 5), 1)
        risk_factor = round(np.random.uniform(1, 10), 1)

        # Label
        supply_priority = classify_priority(cost, transport_time, demand, stock_available)

        entry = {
            "Fabric_Type": fabric,
            "Region": region,
            "Cost_per_Unit(INR)": round(cost, 2),
            "Transport_Time(days)": round(transport_time, 2),
            "Distance_to_Base(km)": distance,
            "Demand_Units": round(demand),
            "Available_Stock": round(stock_available),
            "Supplier_Rating(1-5)": supplier_rating,
            "Risk_Factor(1-10)": risk_factor,
            "Supply_Priority": supply_priority
        }

        data.append(entry)

    df = pd.DataFrame(data)
    df.to_csv("supply_chain_dataset_5000.csv", index=False)
    print("✅ Dataset generated successfully as: supply_chain_dataset_5000.csv")
    return df

# Run generator
df = generate_dataset()
df.head()
 
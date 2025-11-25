# Cell: build_and_save_encoders.py
import os, joblib, pandas as pd
from sklearn.preprocessing import LabelEncoder

# Paths — edit if different
DATA_DIR = "model/datasets"
PKL_DIR  = "pkl_file"
os.makedirs(PKL_DIR, exist_ok=True)

# Load datasets (use the files you have)
df_fabric = pd.read_csv(os.path.join(DATA_DIR, "fabric_full_smart_dataset_5000.csv"))
df_sust   = pd.read_csv(os.path.join(DATA_DIR, "fabric_full_sustainability_dataset_5000.csv"))
df_supply = pd.read_csv(os.path.join(DATA_DIR, "supply_chain_dataset_5000.csv"))

# 1) Fabric encoder (use union of all Fabric_Type values across files)
fabric_values = pd.concat([
    df_fabric["Fabric_Type"].astype(str),
    df_sust["Fabric_Type"].astype(str),
    df_supply["Fabric_Type"].astype(str)
], ignore_index=True).dropna().unique()

fabric_le = LabelEncoder()
fabric_le.fit(fabric_values)
joblib.dump(fabric_le, os.path.join(PKL_DIR, "fabric_label_encoder.pkl"))
print("Saved:", os.path.join(PKL_DIR, "fabric_label_encoder.pkl"))

# 2) Terrain encoder (from fabric file)
if "Terrain" in df_fabric.columns:
    terrain_vals = df_fabric["Terrain"].astype(str).dropna().unique()
    terrain_le = LabelEncoder(); terrain_le.fit(terrain_vals)
    joblib.dump(terrain_le, os.path.join(PKL_DIR, "terrain_label_encoder.pkl"))
    print("Saved:", os.path.join(PKL_DIR, "terrain_label_encoder.pkl"))
else:
    print("Warning: 'Terrain' column not in fabric dataset")

# 3) Region encoder (from supply or sustainability dataset)
region_values = []
if "Region" in df_supply.columns:
    region_values = df_supply["Region"].astype(str).dropna().unique()
elif "Region_Suitability" in df_sust.columns:
    region_values = df_sust["Region_Suitability"].astype(str).dropna().unique()

if len(region_values)>0:
    region_le = LabelEncoder(); region_le.fit(region_values)
    joblib.dump(region_le, os.path.join(PKL_DIR, "region_label_encoder.pkl"))
    print("Saved:", os.path.join(PKL_DIR, "region_label_encoder.pkl"))
else:
    print("Warning: no Region values found to encode.")

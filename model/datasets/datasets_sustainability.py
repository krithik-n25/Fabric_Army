import pandas as pd
import numpy as np
import random

# -------------------------------------
# FABRIC DATA PROFILE RULES (REALISTIC)
# -------------------------------------
FABRIC_PROFILES = {
    "Cotton": {
        "recyclability": (7, 10),
        "biodegradability": (8, 10),
        "water_usage": (9000, 20000),
        "carbon_emissions": (5, 10),
        "toxicity": (2, 6),
        "microplastic_shedding": (0, 0),
        "durability": (4, 7),
        "suitable_regions": ["Hot Desert", "Coastal", "Jungle"]
    },
    "Polyester": {
        "recyclability": (4, 7),
        "biodegradability": (0, 2),
        "water_usage": (500, 3000),
        "carbon_emissions": (12, 25),
        "toxicity": (6, 10),
        "microplastic_shedding": (6, 10),
        "durability": (7, 10),
        "suitable_regions": ["Cold Desert", "Hot Desert", "High Altitude"]
    },
    "Nylon": {
        "recyclability": (5, 8),
        "biodegradability": (0, 3),
        "water_usage": (800, 5000),
        "carbon_emissions": (10, 20),
        "toxicity": (5, 9),
        "microplastic_shedding": (5, 9),
        "durability": (8, 10),
        "suitable_regions": ["High Altitude", "Desert"]
    },
    "Wool": {
        "recyclability": (6, 9),
        "biodegradability": (6, 10),
        "water_usage": (5000, 12000),
        "carbon_emissions": (6, 12),
        "toxicity": (1, 4),
        "microplastic_shedding": (0, 1),
        "durability": (6, 9),
        "suitable_regions": ["Cold Desert", "High Altitude"]
    },
    "Kevlar": {
        "recyclability": (3, 5),
        "biodegradability": (0, 0),
        "water_usage": (2000, 6000),
        "carbon_emissions": (15, 25),
        "toxicity": (7, 10),
        "microplastic_shedding": (2, 5),
        "durability": (10, 10),
        "suitable_regions": ["War Zones", "High Altitude", "Extreme Terrain"]
    },
    "Bamboo Fiber": {
        "recyclability": (7, 10),
        "biodegradability": (7, 10),
        "water_usage": (1000, 5000),
        "carbon_emissions": (2, 6),
        "toxicity": (1, 4),
        "microplastic_shedding": (0, 0),
        "durability": (5, 8),
        "suitable_regions": ["Coastal", "Jungle", "Tropical"]
    }
}

REGIONS = ["Cold Desert", "Hot Desert", "Jungle", "Coastal", "High Altitude", "General Use"]

# -------------------------------------
# SMART DATA GENERATION
# -------------------------------------

def generate_dataset(rows=5000):
    data = []

    for _ in range(rows):
        fabric = random.choice(list(FABRIC_PROFILES.keys()))
        profile = FABRIC_PROFILES[fabric]

        entry = {
            "Fabric_Type": fabric,
            "Recyclability": np.random.uniform(*profile["recyclability"]),
            "Biodegradability": np.random.uniform(*profile["biodegradability"]),
            "Water_Usage": np.random.uniform(*profile["water_usage"]),
            "Carbon_Emissions": np.random.uniform(*profile["carbon_emissions"]),
            "Toxicity": np.random.uniform(*profile["toxicity"]),
            "Microplastic_Shedding": np.random.uniform(*profile["microplastic_shedding"]),
            "Durability": np.random.uniform(*profile["durability"]),
            "Region_Suitability": random.choice(profile["suitable_regions"])
        }

        data.append(entry)

    df = pd.DataFrame(data)
    df.to_csv("fabric_full_sustainability_dataset_5000.csv", index=False)
    print("✅ Dataset created: fabric_full_sustainability_dataset_5000.csv")


if __name__ == "__main__":
    generate_dataset()

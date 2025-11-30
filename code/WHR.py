# WHR Project Data Sci
# Jack Donahue

# Questions
# 1) What impact does GDP have on the general happiness level?
# 2) Does the country's main industries meaningfully impact happiness?
# 3) What is the impact of government style on Happiness?
# 4) What (if any) is the impact of air quality on happiness?

import numpy as np
import matplotlib.pyplot as plt
import csv

# checking function
def try_float(val):
    if val is None:
        return np.nan
    val = val.strip()
    if val in ("", "NaN", "NULL", "None"):
        return np.nan
    try:
        return float(val)
    except ValueError:
        return np.nan

filename = "/home/jack/Documents/COMP3125-WHR_Project/data/WHR.csv"
rows = []


# Load CSV file into program
with open(filename, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        rows.append({
            "country": row["Country name"],
            "happiness": try_float(row["Life evaluation (3-year average)"]),
            "gdp": try_float(row["Explained by: Log GDP per capita"]),
            "life_expectancy": try_float(row["Explained by: Healthy life expectancy"]),
            "freedom": try_float(row["Explained by: Freedom to make life choices"]),
            "corruption": try_float(row["Explained by: Perceptions of corruption"])
        })


# More cleaning
cleaned = [
    r for r in rows
    if not (np.isnan(r["happiness"]) or np.isnan(r["gdp"]))
]

print(f"[INFO] Loaded {len(rows)} rows, kept {len(cleaned)} valid rows.")

# Convert to arrays
happiness = np.array([r["happiness"] for r in cleaned])
gdp = np.array([r["gdp"] for r in cleaned])
life_expectancy = np.array([r["life_expectancy"] for r in cleaned])
freedom = np.array([r["freedom"] for r in cleaned])
corruption = np.array([r["corruption"] for r in cleaned])
countries = [r["country"] for r in cleaned]

# A) GDP vs Happiness
plt.figure(figsize=(8,6))
plt.scatter(gdp, happiness, c="blue")
plt.xlabel("GDP contribution to happiness (Log GDP per capita)")
plt.ylabel("Life Evaluation Score")
plt.title("Impact of GDP on Happiness")
plt.grid(True)
plt.tight_layout()
plt.show()

# B) Life Expectancy vs Happiness
plt.figure(figsize=(8,6))
plt.scatter(life_expectancy, happiness, c="purple")
plt.xlabel("Healthy Life Expectancy Contribution")
plt.ylabel("Life Evaluation Score")
plt.title("Impact of Life Expectancy on Happiness")
plt.grid(True)
plt.tight_layout()
plt.show()

# C) Freedom to Make Life Choices vs Happiness
plt.figure(figsize=(8,6))
plt.scatter(freedom, happiness, c="green")
plt.xlabel("Freedom to Make Life Choices (Contribution)")
plt.ylabel("Life Evaluation Score")
plt.title("Impact of Freedom to Make Life Choices on Happiness")
plt.grid(True)
plt.tight_layout()
plt.show()

# D) Perceived Corruption vs Happiness
plt.figure(figsize=(8,6))
plt.scatter(corruption, happiness, color="red")
plt.xlabel("Perception of Corruption (higher = more corruption)")
plt.ylabel("Life Evaluation Score")
plt.title("Impact of Perceived Corruption on Happiness")
plt.grid(True)
plt.tight_layout()
plt.show()



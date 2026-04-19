# ======================================
# Task 1: Explore the Dataset
# ======================================

import pandas as pd   
import glob           
import os

# --------------------------------------------------
# 1. LOAD THE DATASET
# --------------------------------------------------

all_files = glob.glob("data/*.csv")

print(f"All file found: {len(all_files)}")
for f in all_files:
    print(" -", os.path.basename(f))

df_list = []
for file in all_files:
    temp_df = pd.read_csv(file)
   
    station_name = os.path.basename(file).replace("PRSA_Data_", "").replace("_20130301-20170228.csv", "")
    temp_df["station"] = station_name
    df_list.append(temp_df)

df = pd.concat(df_list, ignore_index=True)

print("\n✅ Completely Downloading!")

# --------------------------------------------------
# 2. DISPLAY THE FIRST 5 ROWS
# --------------------------------------------------

print("\n" + "="*60)
print("📋 5 Row of data:")
print("="*60)
print(df.head())   
# --------------------------------------------------
# 3. IDENTIFY COLUMN NAMES AND DATA TYPES
# --------------------------------------------------

print("\n" + "="*60)
print(" Column name and type of data:")
print("="*60)
print(df.dtypes)  

print("\n Summary (info):")
print("-"*60)
df.info()          

# --------------------------------------------------
# 4. COUNT TOTAL ROWS AND COLUMNS
# --------------------------------------------------

print("\n" + "="*60)
print(" Count Total Rows and Columns:")
print("="*60)

rows, columns = df.shape   

print(f"Total Rows    : {rows:,} Rows")
print(f"Total Columns : {columns} Columns")
print(f"\n Name of Column ({columns} Columns):")
for i, col in enumerate(df.columns, 1):
    print(f"  {i:2}. {col}")
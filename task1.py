# ======================================
# Task 1: Explore the Dataset
# ======================================

import pandas as pd   
import glob           

# --------------------------------------------------
# 1. LOAD THE DATASET
# --------------------------------------------------

all_files = glob.glob("data/*.csv")  # หาไฟล์ CSV ทั้งหมดในโฟลเดอร์ data/
print(f"All files: {len(all_files)} ")
df_list = []  
for file in all_files:
    temp = pd.read_csv(file)  
    df_list.append(temp)      
df = pd.concat(df_list, ignore_index=True)
print("\n✅ Completely Downloading!")

# --------------------------------------------------
# 2. DISPLAY THE FIRST 5 ROWS
# --------------------------------------------------
  
print("\n--- 5 Row of data ---")
print(df.head())

# --------------------------------------------------
# 3. IDENTIFY COLUMN NAMES AND DATA TYPES
# --------------------------------------------------

print("\n--- Column name and type of data ---")
print(df.dtypes)
      
# --------------------------------------------------
# 4. COUNT TOTAL ROWS AND COLUMNS
# --------------------------------------------------

rows, cols = df.shape
print(f"\n Total Rows: {rows}")
print(f"Total Columns: {cols}")

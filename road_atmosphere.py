import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

atmospheric_condition = pd.read_csv("ATMOSPHERIC_COND.csv")
road_surface_condition = pd.read_csv("ROAD_SURFACE_COND.csv")

merged_df = pd.merge(atmospheric_condition, road_surface_condition, on='ACCIDENT_NO')
pivot_table = pd.crosstab(merged_df["Atmosph Cond Desc"], merged_df["Surface Cond Desc"])

plt.figure(figsize=(12, 8))
sns.heatmap(pivot_table, annot=True, fmt='d', cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap by Count of accident_id')
plt.xlabel('Road Surface Condition')
plt.ylabel('Atmospheric Condition')
plt.show()
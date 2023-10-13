import pandas as pd

accident = pd.read_csv("ACCIDENT.csv")
print(accident["Light Condition Desc"].unique())
print(accident["Road Geometry Desc"].unique())
print(accident["SPEED_ZONE"].unique())


# Group by "Light Condition Desc" and "Road Geometry Desc" and count the accidents
grouped_data = accident.groupby(['Light Condition Desc', 'Road Geometry Desc'])['ACCIDENT_NO'].count().reset_index()

# Rename the count column to something more descriptive (e.g., "Accident Count")
grouped_data = grouped_data.rename(columns={'Accident_ID': 'Accident Count'})

# Display the result
print(grouped_data)
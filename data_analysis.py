import pandas as pd

node = pd.read_csv("ACCIDENT.csv")
print(node["Accident Type Desc"].unique())

# Group by "Light Condition Desc" and "Road Geometry Desc" and count the accidents
# grouped_data = node.groupby(['Region Name']).agg({'Lat': 'mean', 'Long': 'mean'}).reset_index()

# # Display the result
# print(grouped_data)

 
 



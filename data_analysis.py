import pandas as pd

node = pd.read_csv("PERSON.csv")
print(node["Age Group"].unique())
print(node["SEX"].unique())
print(node["Inj Level Desc"].unique())
print(node["Road User Type Desc"].unique())
print(node["SEATING_POSITION"].unique())



# Group by "Light Condition Desc" and "Road Geometry Desc" and count the accidents
# grouped_data = node.groupby(['Road User Type Desc', "Inj Level Desc"]).agg({'Lat': 'mean', 'Long': 'mean'}).reset_index()
grouped_data = node.groupby(['Age Group', "Inj Level Desc"])["ACCIDENT_NO"].count().reset_index()

# # Display the result
print(grouped_data)
# print(grouped_data[(grouped_data["Road User Type Desc"] == "Drivers") | (grouped_data["Road User Type Desc"] == "Passengers")])

 
 



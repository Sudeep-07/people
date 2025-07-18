import csv

youngest = {"Name": None, "Age": float("inf"), "City": None, "Country": None}
oldest = {"Name": None, "Age": float("-inf"), "City": None, "Country": None}

with open("people.csv", mode="r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        name = row["Name"]
        age = int(row["Age"])
        city = row["City"]
        country = row["Country"]

        if age < youngest["Age"]:
            youngest = {"Name": name, "Age": age, "City": city, "Country": country}
        if age > oldest["Age"]:
            oldest = {"Name": name, "Age": age, "City": city, "Country": country}

print("👶 Youngest Person:")
print(f"Name: {youngest['Name']}, Age: {youngest['Age']}, City: {youngest['City']}, Country: {youngest['Country']}")

print("\n🧓 Oldest Person:")
print(f"Name: {oldest['Name']}, Age: {oldest['Age']}, City: {oldest['City']}, Country: {oldest['Country']}")

# or 

# ✅ Optimized Code:

# import csv

# with open("people.csv", mode="r") as file:
#     reader = csv.DictReader(file)
#     data = list(reader)

# # Convert age to integer once and sort only once
# for person in data:
#     person["Age"] = int(person["Age"])

# # Sort the data by age
# sorted_data = sorted(data, key=lambda x: x["Age"])

# # Youngest is first, oldest is last
# youngest = sorted_data[0]
# oldest = sorted_data[-1]

# print("👶 Youngest Person:")
# print(f"Name: {youngest['Name']}, Age: {youngest['Age']}, City: {youngest['City']}, Country: {youngest['Country']}")

# print("\n🧓 Oldest Person:")
# print(f"Name: {oldest['Name']}, Age: {oldest['Age']}, City: {oldest['City']}, Country: {oldest['Country']}")


# or 

#  Optional Alternative (One-pass & Efficient):

# If performance matters for large datasets, and you want to avoid sorting:



# import csv

# youngest = oldest = None

# with open("people.csv", mode="r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         row["Age"] = int(row["Age"])
#         if youngest is None or row["Age"] < youngest["Age"]:
#             youngest = row
#         if oldest is None or row["Age"] > oldest["Age"]:
#             oldest = row

# print("👶 Youngest Person:")
# print(f"Name: {youngest['Name']}, Age: {youngest['Age']}, City: {youngest['City']}, Country: {youngest['Country']}")

# print("\n🧓 Oldest Person:")
# print(f"Name: {oldest['Name']}, Age: {oldest['Age']}, City: {oldest['City']}, Country: {oldest['Country']}")

import csv

youngest = {"Name": None, "Age": float("inf"), "City": None}
oldest = {"Name": None, "Age": float("-inf"), "City": None}

with open("people.csv", mode="r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        name = row["Name"]
        age = int(row["Age"])
        city = row["City"]

        if age < youngest["Age"]:
            youngest = {"Name": name, "Age": age, "City": city}
        if age > oldest["Age"]:
            oldest = {"Name": name, "Age": age, "City": city}

print("👶 Youngest Person:")
print(f"Name: {youngest['Name']}, Age: {youngest['Age']}, City: {youngest['City']}")

print("\n🧓 Oldest Person:")
print(f"Name: {oldest['Name']}, Age: {oldest['Age']}, City: {oldest['City']}")

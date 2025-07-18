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

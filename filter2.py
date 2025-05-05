import json

with open("./school-data2.json", "r") as file:
    data = json.load(file)

cutoff_timestamp = 1736645174000

filtered_data = [obj for obj in data if obj["lastVisitTime"] > cutoff_timestamp]


with open("filtered_data.json", "w") as file:
    json.dump(filtered_data, file, indent=4)

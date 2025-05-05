import json
from datetime import datetime

with open("./watch-history.json") as f:
    data = json.load(f)

cutoff_date = datetime.strptime("2025-01-01T00:00:00.000Z", "%Y-%m-%dT%H:%M:%S.%fZ")


def parse_timestamp(timestamp):
    try:
        return datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%fZ")
    except ValueError:
        return datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")


filtered_data = []
for obj in data:
    timestamp = parse_timestamp(obj["time"])
    if timestamp > cutoff_date:
        unix_timestamp = int(timestamp.timestamp())
        obj["unix_timestamp"] = unix_timestamp
        filtered_data.append(obj)

with open("filtered-watch-history.json", "w") as file:
    json.dump(filtered_data, file, indent=4)

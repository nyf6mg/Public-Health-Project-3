import json
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timezone


def count_timestamps_per_week(file_path, file_path2, save_file):
    with open(file_path, "r") as file:
        data = json.load(file)
    with open(file_path2, "r") as file2:
        data2 = json.load(file2)

    timestamps = []
    for obj in data:
        ts = obj["lastVisitTime"]
        if ts > 10000000000:
            ts /= 1000
        try:
            timestamps.append(datetime.fromtimestamp(ts, timezone.utc))
        except ValueError as e:
            print(e)

    for obj in data2:
        ts = obj["lastVisitTime"]
        if ts > 10000000000:
            ts /= 1000
        try:
            timestamps.append(datetime.fromtimestamp(ts, timezone.utc))
        except ValueError as e:
            print(e)

    df = pd.DataFrame(timestamps, columns=["datetime"])
    df.set_index("datetime", inplace=True)

    weekly_counts = df.resample("W").size()
    weekly_counts.to_csv(save_file, header=["Count"])

    plt.figure(figsize=(10, 5))
    plt.plot(weekly_counts.index, weekly_counts.values, marker="o")
    plt.title("Weekly Count of Timestamps")
    plt.xlabel("Week")
    plt.ylabel("Count of Timestamps")
    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.show()


file_path = "./data.json"
file_path2 = "./personal-data2.json"
count_timestamps_per_week(file_path, file_path2, "./personal-wc.csv")
file_path3 = "./filtered_data.json"
file_path4 = "./data-school.json"
count_timestamps_per_week(file_path3, file_path4, "./school-wc.csv")

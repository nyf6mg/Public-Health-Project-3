import json
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timezone


def count_timestamps_per_week(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)

    timestamps = []
    for obj in data:
        ts = obj["unix_timestamp"]
        if ts > 1_000_000_0000:
            ts /= 1000

        print(f"Original timestamp: {obj['unix_timestamp']}, Converted timestamp: {ts}")
        try:
            timestamps.append(datetime.fromtimestamp(ts, timezone.utc))
        except ValueError as e:
            print(e)

    df = pd.DataFrame(timestamps, columns=["datetime"])
    df.set_index("datetime", inplace=True)

    weekly_counts = df.resample("W").size()
    weekly_counts.to_csv("./youtube-wc.csv", header=["Count"])

    plt.figure(figsize=(10, 5))
    plt.plot(weekly_counts.index, weekly_counts.values, marker="o")
    plt.title("Weekly Count of Timestamps")
    plt.xlabel("Week")
    plt.ylabel("Count of Timestamps")
    plt.xticks(rotation=45)
    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.show()


file_path = "./filtered-watch-history.json"
count_timestamps_per_week(file_path)

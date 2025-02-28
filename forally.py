import json
import csv

with open("data.json", "r") as json_file:
    data = json.load(json_file)


csv_file = "greenhouse_output.csv"

keys = data[0].keys()

with open(csv_file, "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=keys)
    writer.writeheader()
    writer.writerows(data)

print(f"csv file '{csv_file}' has been created successfully!")

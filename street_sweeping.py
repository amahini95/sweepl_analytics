import json
import re

# Read the data from the CSV file
with open('Street_Sweeping_Schedule.csv', 'r') as file:
    data = file.readlines()

# Remove the header
data = data[1:]

result = []

# Process each line
for line in data:
    line = line.strip().split(',')
    weeks = sum(map(int, line[9:14])) + int(line[14])

    # Extract coordinates from the LINESTRING
    coordinates = re.findall(r"[-]?\d+\.\d+", line[-1])
    points = [coordinates[i:i + 2] for i in range(0, len(coordinates), 2)]

    # Duplicate the points based on the number of weeks
    for _ in range(weeks):
        for point in points:
            result.append([float(point[1]), float(point[0])])

# Write the resulting JSON data to a file
with open('output.json', 'w') as outfile:
    json.dump(result, outfile, indent=4)

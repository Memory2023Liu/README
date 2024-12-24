import os

# Function to calculate development time (Replace with actual logic)
def calculate_dev_time():
    # Example logic to calculate development time
    dev_time = "10 hours"  # Replace with actual calculation
    return dev_time

# Read README file
with open('README.md', 'r') as file:
    lines = file.readlines()

# Update development time in README (adjust as necessary)
for i, line in enumerate(lines):
    if 'Weekly Development Time:' in line:
        lines[i] = f"Weekly Development Time: {calculate_dev_time()}\n"

# Write updated README file
with open('README.md', 'w') as file:
    file.writelines(lines)

import matplotlib.pyplot as plt
import re
# Define file names and corresponding labels
experiments = ["1-2-3-4", "3-4-5-6", "5-6-7-8"]
labels = ["2", "4", "8"]
ipc_values = []

# Specify the baseline IPC values manually (same order as experiments)
baseline_ipc = [0.104721, 0.428719, 0.442091 ]  # <-- Change these values as needed

# Regular expression pattern to extract IPC value
ipc_pattern = re.compile(r"CPU 0 cumulative IPC:\s+([\d.]+)")

# Read IPC values from files
for exp in experiments:
    file_path = f"results/{exp}.txt"
    try:
        with open(file_path, "r") as file:
            matches = list(ipc_pattern.finditer(file.read()))  # Find all occurrences
            
            if len(matches) >= 2:  # Ensure there are at least two matches
                ipc = float(matches[1].group(1))  # Extract the second match
                ipc_values.append(ipc)
                print(ipc)
            else:
                print(f"Warning: Less than two IPC values found in {file_path}")
                ipc_values.append(0)  # Default value if second match is missing
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        ipc_values.append(0)  # Default value in case of error

# Normalize IPC values using the baseline
normalized_ipc = [ipc / base if base != 0 else 0 for ipc, base in zip(ipc_values, baseline_ipc)]

# Plot bar chart
plt.figure(figsize=(6, 4))
plt.bar(labels, normalized_ipc, color="steelblue")
plt.ylabel("Normalized IPC")
plt.ylim(0, max(normalized_ipc) * 1.2)  # Adjust y-axis for better visualization
plt.title("Normalized IPC for Different Workloads")
plt.savefig("results/ipc_chart_0.png")
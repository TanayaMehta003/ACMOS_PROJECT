import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# Load the CSV file
file_path = 'n_ft.csv'  # Replace this with the actual file path
data = pd.read_csv(file_path)

# Extract columns for plotting
x_columns = [col for col in data.columns if "X" in col]
y_columns = [col for col in data.columns if "Y" in col]

# Define l_nmos values in nanometers
l_nmos_values_nm = [180, 360, 540, 720, 900, 1080, 1260]

# Sort the l_nmos values and their corresponding data columns
sorted_data = sorted(zip(l_nmos_values_nm, x_columns, y_columns), key=lambda x: x[0])
sorted_l_nmos_values, sorted_x_columns, sorted_y_columns = zip(*sorted_data)

# Plot the graph
plt.figure(figsize=(10, 6))
for l_nmos_nm, x_col, y_col in zip(sorted_l_nmos_values, sorted_x_columns, sorted_y_columns):
    plt.plot(data[x_col], data[y_col], label=f"L_nmos = {l_nmos_nm} nm")  # Smooth lines

# Format Y-axis to show values divided by 10^9
plt.gca().yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
plt.ticklabel_format(style='scientific', axis='y', scilimits=(9, 9))
plt.gca().yaxis.offsetText.set_visible(False)  # Hide the default offset text
plt.ylabel("nft (x10⁹)")  # Add x10⁹ notation to the Y-axis label

# Add labels, title, and legend
plt.xlim(left=4)
plt.xlabel("ngm/id")
plt.title("nft vs ngm_id")
plt.legend(title="L_nmos values (nm)")
plt.grid(True)
plt.tight_layout()

# Display the plot
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, ScalarFormatter

# Load the CSV file
file_path = 'n_ids_w_v_gm_id.csv'  # Replace this with the path to your CSV file
data = pd.read_csv(file_path)

# Extract columns for plotting
x_columns = [col for col in data.columns if "X" in col]
y_columns = [col for col in data.columns if "Y" in col]

# Define l_pmos values in nanometers
l_nmos_values_nm = [180, 360, 540, 720, 900, 1080, 1260]  # Corresponding l_pmos values in nanometers

# Plot the graph
plt.figure(figsize=(10, 6))
for (x_col, y_col), l_nmos_nm in zip(zip(x_columns, y_columns), l_nmos_values_nm):
    plt.plot(data[x_col], data[y_col], label=f"L_pmos = {l_nmos_nm} nm")  # No marker for smooth lines

# plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, _: f'{y / 1e9:.1f}'))  # Format Y-axis in terms of 10^9

# Format Y-axis to show values divided by 10^9
# plt.gca().yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
# plt.ticklabel_format(style='scientific', axis='y', scilimits=(9, 9))
# plt.gca().yaxis.offsetText.set_visible(False)  # Hide the default offset text
# plt.ylabel("Pft x10⁹)")  # Add x10⁹ notation to the Y-axis label


# Add labels, title, and legend
plt.xlim(left=4)
plt.xlabel("ngm/id")
plt.ylabel("nid/w")
plt.title("nid_w vs ngm_id")
plt.legend(title="L_nmos values (nm)")
plt.grid(True)
plt.tight_layout()

# Display the plot
plt.show()

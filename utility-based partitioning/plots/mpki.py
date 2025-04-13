import matplotlib.pyplot as plt
import numpy as np

# Replace these with your actual data
baseline_mpki = [33, 39, 26]
static_partitioning_mpki = [31, 14, 32]

# X-axis labels
combinations = ['combination1', 'combination2', 'combination3']
x = np.arange(len(combinations))
width = 0.35

fig, ax = plt.subplots()
bars1 = ax.bar(x - width/2, baseline_mpki, width, label='Non Secure System', color='royalblue')
bars2 = ax.bar(x + width/2, static_partitioning_mpki, width, label='Secure System', color='indianred')

# Labels and title
ax.set_ylabel('MPKI')
ax.set_ylabel('Combination of traces')
ax.set_xticks(x)
ax.set_xticklabels(combinations)
ax.legend()

# Optional: Add value labels on top of bars
for bar in bars1 + bars2:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom')

plt.tight_layout()
plt.savefig('mpki_comparison.png', dpi=300)
plt.close()

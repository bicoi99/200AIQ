import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("presentation_plots/shares.csv")
data["diff"] = data["share"].diff()
bottom_50 = data["share"][50]
from50to70 = data["share"][70] - data["share"][51]
from70to85 = data["share"][85] - data["share"][71]
from85to95 = data["share"][95] - data["share"][86]
top_5 = data["share"][100] - data["share"][96]

objects = ["Bottom 50%", "50% - 70%", "70% - 85%", "85% - 95%", "Top 5%"]
y_pos = np.arange(len(objects))
performance = [bottom_50, from50to70, from70to85, from85to95, top_5]

fig, ax = plt.subplots(figsize=(10, 7))
ax.bar(y_pos, performance, align='center', color="forestgreen")
for i, v in enumerate(performance):
    print(f" {i} {v}")
    ax.text(i-.18, v+.008, f"{v*100:.1f} %", fontsize=14)
plt.xticks(y_pos, objects, fontsize=12)
plt.yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7], fontsize=12)
plt.ylabel("Fraction of Shares Held", fontsize=16)
plt.ylim([0, 0.7])
plt.suptitle("Distribution of Facebook Shares", fontsize=20)

plt.show()

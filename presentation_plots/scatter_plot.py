import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Shares after 48 hrs vs. shares after 1 hr (proportional axes)
data = pd.read_csv("presentation_plots/48vs1hr.csv")
data = data[data["Facebook"] >= data["TS2"]]
z = np.polyfit(data["TS2"], data["Facebook"], 1)
p = np.poly1d(z)
plt.scatter(data["TS2"], data["Facebook"], 1, 'k')
plt.plot(data["TS2"], p(data["TS2"]), "r--")
plt.ylabel("Shares after 48h", fontsize=16)
plt.xlabel("Shares after 1h", fontsize=16)
plt.xlim([0, 30000])
plt.ylim([0, 30000])
plt.tight_layout()
plt.savefig("presentation_plots/48hvs.1h_plot.png", transparent=True)

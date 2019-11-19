import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("results_plot/classification_results.csv")

confusion_matrix = np.array([[80000, 10], [30, 10000]])

sn.set(font_scale=1.4)
sn.heatmap(confusion_matrix, annot=True, fmt="d")

plt.show()

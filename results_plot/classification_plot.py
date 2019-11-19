import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("results_plot/classification_results.csv")

prediction = np.zeros(50)
real = data["viral"]
for i in range(len(prediction)):
    if data["prob_False"][i] > data["prob_True"][i]:
        prediction[i] = 0
    else:
        prediction[i] = 1

print("Done loop!")

plt.subplot(2, 1, 1)
plt.plot(np.arange(50), prediction[:50], "bo-")
plt.yticks([0, 1])
plt.xticks([])
plt.ylabel("Prediction", fontsize=18)
plt.subplot(2, 1, 2)
plt.plot(np.arange(50), data["viral"][:50], "ro-")
plt.yticks([0, 1])
plt.ylabel("Actual", fontsize=18)
plt.suptitle("Model predictions and actual values", fontsize=20)
plt.show()

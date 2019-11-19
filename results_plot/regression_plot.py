import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

prediction = pd.read_csv("results_plot/regression_results.csv")
actual = pd.read_csv("results_plot/merged2.csv")

prediction_plot = prediction["Facebook"][:50]
actual_plot = actual["Facebook"][:50]

actual, = plt.plot(np.arange(50), actual_plot, "ro-", label="Actual")
prediction, = plt.plot(np.arange(50), prediction_plot,
                       "bo-", label="Prediction")
plt.legend(handles=[actual, prediction], fontsize=16)
plt.ylabel("Number of shares on Facebook", fontsize=18)
plt.suptitle("Model predictions and actual values", fontsize=20)
plt.show()

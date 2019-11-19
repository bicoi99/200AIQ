import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import dates
import datetime

data = pd.read_csv("all_topics_plot/multiTimeline-2.csv")
converted_dates = list(map(datetime.datetime.strptime,
                           data["Month"], len(data["Month"])*['%Y-%m']))
x_axis = converted_dates
formatter = dates.DateFormatter('%Y')
print(formatter)
fig, ax = plt.subplots(figsize=(10, 7))
obama, = ax.plot(x_axis, data["Obama"], label="Obama")
palestine, = ax.plot(x_axis, data["Palestine"], label="Palestine")
economy, = ax.plot(x_axis, data["Economy"], label="Economy")
microsoft, = ax.plot(x_axis, data["Microsoft"], label="Microsoft")
ax.xaxis.set_major_locator(dates.YearLocator())
ax.xaxis.set_major_formatter(formatter)
plt.xlabel("Years", fontsize=18)
plt.ylabel("Weightings", fontsize=18)
plt.suptitle("Popularity over time", fontsize=20)
plt.legend(handles=[obama, palestine, economy, microsoft],
           fontsize=16, framealpha=0)
plt.gcf().autofmt_xdate(rotation=25)
# plt.xticks(np.arange(2014, 2020))
plt.savefig("all_topics_plot/google_trends_plot.png", transparent=True)
plt.show()

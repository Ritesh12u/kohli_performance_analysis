import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")
opponent  = df["Opposition"].unique()
print(opponent)

df["Pos"] = df["Pos"].map({
    'v Sri Lanka' : "Playing vs Sri Lanka",
    'v Australia' : "Playing vs Ausrtalia",
    'v Bangladesh' : "Playing vs Bangladesh",
    'v South Africa' : "Playing vs South Africa",
    'v Zimbabwe' : "Playing vs Zimbabwe",
   'v New Zealand' : "Playing vs New Zealand",
    'v Ireland' : "Playing vs Ireland",
    'v Netherlands' : "Playing vs Netherlands",
    'v West Indies' : "Playing vs West Indies",
    'v Pakistan' : "Playing vsPakistan",
    'v England' :"Playing vs England",
})
opponent_count = df["Opposition"].value_counts()
print(opponent_count)

opponent_value = opponent_count.values
opponent_labels = opponent_count.index
print(opponent_value)

fig = plt.figure(figsize=(10,7))
plt.pie(opponent_value, labels = opponent_labels)
plt.show()
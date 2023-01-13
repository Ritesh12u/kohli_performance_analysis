import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# read the CSV file

df = pd.read_csv("dataset.csv")
print(df.head(10))
# FInd total number of runs kohli has scored

total_run = df["Runs"].sum()
no_of_matches = len(df["Runs"])
print(f"\nTotal run of the kohli is scored in {no_of_matches} matches:",total_run)
# Average number of run he has scored

avg_run = df["Runs"].mean()
print(f"\nThe average score of kohli in {no_of_matches} is::",int(avg_run))
# Number of matches in differtent position

position  = df["Pos"].unique()  #return the unique position from the dataset
# print(position)

df["Pos"] = df["Pos"].map({
    3.0 : "Batting at 3",
    4.0 : "Batting at 4",
    2.0 : "Batting at 2",
    1.0 : "Batting at 1",
    7.0 : "Batting at 7",
    5.0 : "Batting at 5",
    6.0 : "Batting at 6",
})
# print(df[["Runs","Pos","Opposition"]].head())
# pos_count = df["Pos"].value_counts()
# print(pos_count)
# print(type(pos_count))
# pos_values = pos_count.values
# pos_labels = pos_count.index
# print(pos_values)

# fig = plt.figure(figsize=(10,7))
# plt.pie(pos_values, labels = pos_labels)
# plt.show()

#........display n number of pie chart using function

def show_pie_plot(df,key):
    counts = df[key].value_counts()
    count_values = counts.values
    count_label = counts.index

    fig = plt.figure(figsize=(10,7)) 
    plt.pie(count_values, labels=count_label)
    # plt.show()

show_pie_plot(df,"Pos")
show_pie_plot(df,"Opposition")
show_pie_plot(df,"Ground")



# Total run scored in differnt position

runs_at_pos  = df.groupby("Pos")["Runs"].sum()
runs_at_pos_values = runs_at_pos.values
runs_at_pos_labels = runs_at_pos.index

fig = plt.figure(figsize=(10,7))
plt.pie(runs_at_pos_values, labels=runs_at_pos_labels)
# plt.show()
print(runs_at_pos)

# Total number of 6s of different opposition
sixes  = df.groupby("Opposition")["6s"].sum()
sixes_values = sixes.values
sixes_labels = sixes.index

fig = plt.figure(figsize=(10,7))
plt.pie(sixes_values, labels=sixes_labels)
# plt.show()
print(sixes)

# NUmber of centuries scored by kohli in first ans second innings

centuries = df.query("Runs>=100")
print(centuries)

innings = centuries["Inns"]
tons = centuries["Runs"]

fig = plt.figure(figsize=(10,7))
plt.bar(innings, tons, color = 'blue', width=0.2)
# plt.show()

# CAlculate the dismisses of kohli

dismissals = df["Dismissal"].value_counts()
print(dismissals)

dismissals_counts = dismissals.values
dismissals_labels = dismissals.index
show_pie_plot(df,"Dismissal")
# plt.show()
# Aggainst which team he has scord the most run

fig = plt.figure(figsize=(10,7))
plt.bar(
    df["Opposition"], df["Runs"], color = 'red', width =0.2
)
# plt.show()
# Aggainst which team he scored most centuries
fig = plt.figure(figsize=(10,7))
plt.bar(
    centuries["Opposition"], centuries["Runs"], color = 'green', width =0.2
)
plt.show()
# Analyze the strike rate

# kohli's striked rate in first and sechonf=d innings

# Runs scored by kohli by 4s played

# Runs scored by kohli by 6s played
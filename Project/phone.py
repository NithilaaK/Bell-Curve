import pandas as pd
import csv
import plotly.figure_factory as ff

df = pd.read_csv("Project/phone.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()], ["Average Rating"])
fig.show()
import pandas as pd
import plotly.express as px

file = 'covid_data.csv'
df = pd.read_csv(file)

fig = px.scatter(df, x="date", y="cases", color="country", size_max=60)
fig.show()
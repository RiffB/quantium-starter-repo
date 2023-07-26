from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import csv

app = Dash(__name__)

filepath = 'pink_morsels_output.csv'
data = pd.read_csv(filepath)
sales = data['sales'].tolist()
dates = data['date'].tolist()

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Date": dates,
    "Sales": sales,
})

fig = px.line(df, x="Date", y="Sales", title="Pink Morsel Sales")

app.layout = html.Div(children=[
    html.H1(children='Dash App'),

    html.Div(children='''
        Line Plot exercise
    '''),

    dcc.Graph(
        id='pink-morsels-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
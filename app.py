from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# 1. Initialize the Dash app
app = Dash(__name__)

# 2. Load and prepare the data
# We must sort by date to ensure the line chart flows correctly
df = pd.read_csv('formatted_data.csv')
df = df.sort_values(by="date")

# 3. Create the Line Chart using Plotly Express
fig = px.line(
    df, 
    x="date", 
    y="sales", 
    title="Pink Morsel Sales Trend",
    labels={"date": "Date of Sale", "sales": "Total Sales (USD)"}
)

# 4. Define the App Layout
app.layout = html.Div(style={'fontFamily': 'Arial, sans-serif', 'padding': '20px'}, children=[
    # Header element
    html.H1(
        children='Pink Morsel Sales Visualizer',
        style={'textAlign': 'center', 'color': '#2c3e50'}
    ),

    # Line Chart element
    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

# 5. Run the server
if __name__ == '__main__':
    app.run(debug=True)
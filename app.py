from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

# 1. Initialize Dash
app = Dash(__name__)

# 2. Data Preparation
df = pd.read_csv('formatted_data.csv')
df = df.sort_values(by="date")

# 3. App Layout (with Neon Styling)
app.layout = html.Div(style={
    'backgroundColor': '#0a0b10', 
    'color': '#00ffcc', 
    'fontFamily': 'Courier New, monospace',
    'padding': '40px',
    'minHeight': '100vh'
}, children=[
    
    # Neon Header
    html.H1(
        children='PINK MORSEL: SALES ARENA',
        style={
            'textAlign': 'center', 
            'textShadow': '0 0 10px #00ffcc, 0 0 20px #00ffcc',
            'marginBottom': '30px'
        }
    ),

    # Radio Button Container
    html.Div(style={'textAlign': 'center', 'marginBottom': '20px'}, children=[
        html.Label("FILTER BY SECTOR:", style={'fontWeight': 'bold', 'marginRight': '15px'}),
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All', 'value': 'all'}
            ],
            value='all',
            inline=True,
            style={'display': 'inline-block'},
            inputStyle={"margin-left": "20px", "margin-right": "5px"}
        ),
    ]),

    # The Dynamic Graph
    dcc.Graph(id='sales-line-chart')
])

# 4. Callback Logic (The "Brain" of the App)
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_graph(selected_region):
    # Filter data based on radio selection
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    # Create figure with a dark theme
    fig = px.line(
        filtered_df, 
        x="date", 
        y="sales", 
        template="plotly_dark",
        labels={"date": "Timeline", "sales": "Credits (USD)"}
    )

    # Neon line color and plot styling
    fig.update_traces(line_color='#00ffcc', line_width=3)
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='#00ffcc'
    )
    
    return fig

if __name__ == '__main__':
    app.run(debug=True)
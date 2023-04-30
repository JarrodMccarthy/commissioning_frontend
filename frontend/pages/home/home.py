import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from pages.home import home_callbacks

#sensor_display = 

layout = dbc.Container([
    dbc.Row(
        [
            html.H6("Overview"),
            html.Hr(),
            dbc.Col(
                [
                    html.H4("Current"),
                    html.Div(id='sensor-1-current', children=[], style={'padding': 50}), #24E124713C241806, metric: distance                   
                    
                ],
                width=3,
            ),
            dbc.Col(
                [
                    html.H4("Device History"),
                    #html.Div(id='sensor-1-history', children=[]),                    
                    html.Div(dcc.Graph(id="sensor-1-history-graph", style={'width': 400}))
                ],
                width=9,
            ),
        ],
        justify="evenly"
    ),
    dcc.Interval(id='sensor-update-interval',interval=120*1000, n_intervals=0),
    html.Hr(),
    dcc.Interval(id='overview-interval-component', interval=120*1000, n_intervals=0),
    #html.Button('Submit', id='home-submit-button', n_clicks=0),
    dbc.Row(
        [
            dbc.Col(html.Div(id='overview-div', children=[]), width=12)
        ],
        justify="between",
    ),
    html.Div(id='dummy-display', children = [])
])

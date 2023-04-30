from classes.api import API
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.express as px
import dash_daq as daq
from app import app
from dash.exceptions import PreventUpdate

@app.callback(
    Output('overview-div', 'children'),
    Input('home-submit-button', 'n_clicks'))
def callback(n):
    api = API()
    return f"{n}"


@app.callback(
    Output('sensor-1-current', 'children'),
    Input('sensor-update-interval', 'n_intervals'),
    PreventUpdate=True,
)
def update_sensors(n):
    api = API()
    device_id = "24E124713C241806"
    metric = "distance"
    measurements = api.get_sensor_measurement(device_id, metric)
    latest_measurement_value = measurements["measurements"][0]["value"]
    return daq.Tank(
    value=int(latest_measurement_value),
    showCurrentValue=True,
    height=700,
    width=150,
    units='mm',
    min=0,
    max=2500,
    
    #style={'margin-left': '50px'}
)

@app.callback(
    Output("sensor-1-history-graph", 'figure'),
    Input('sensor-update-interval', 'n_intervals'),
    PreventUpdate=True,
)
def update_sensors(n):
    #try:
    api = API()
    device_id = "24E124713C241806"
    metric = "distance"
    measurements = api.get_sensor_measurement(device_id, metric)
    df = pd.DataFrame.from_records(measurements["measurements"])
    df[['metric', 'label', 'timestamp']] = df['measurement_id'].str.split('#',expand=True)
    #print(df.head())
    fig = px.line(df, x="timestamp", y="value", width=1000, height=800)
    fig.update_yaxes(nticks=25)
    #fig.update_layout(yaxis_range=(0, 2500))
    return fig
    # except Exception as e:
    #     return "Failed bro"
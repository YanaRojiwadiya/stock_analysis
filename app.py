import dash
from dash import html, dcc, Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Label("Enter company name:"),
    dcc.Input(id='my-input', type='text', value=''),
    html.Label("Select a time range:", style={'margin-right': '10px', 'margin-left': '30px'}),
    dcc.Dropdown(
        id='time-range-dropdown',
        options=[
            {'label': '1D', 'value': '1d'},
            {'label': '5D', 'value': '5d'},
            {'label': '1M', 'value': '1m'},
            {'label': '3M', 'value': '3m'},
            {'label': '6M', 'value': '6m'},
            {'label': 'YTD', 'value': 'ytd'},
            {'label': '1Y', 'value': '1y'},
            {'label': '2Y', 'value': '2y'},
            {'label': '5Y', 'value': '5y'},
            {'label': 'MAX', 'value': 'max'}
        ],
        value='1D',
        style={'width': '80px', 'margin-right': '10px'}
    ),
    html.Button('Submit', id='submit-button', n_clicks=0, style={'margin-left': '30px'}),
    html.Div(id='output')
], style={'background-color': '#add8e6', 'padding': '20px', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center', 'flex-wrap': 'wrap'})

@app.callback(
    Output('output', 'children'),
    [Input('submit-button', 'n_clicks')],
    [State('my-input', 'value'),
     State('time-range-dropdown', 'value')]
)
def update_output(n_clicks, input_value, time_range_value):
    if n_clicks > 0:
        return f'Input value: {input_value}, Time range selected: {time_range_value}'
    else:
        return ''

if __name__ == '__main__':
    app.run_server(debug=True)
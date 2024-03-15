import dash
from dash import html, dcc, Input, Output, State
from yfinance_data import Yfinance
import plotly.graph_objs as go

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
        dcc.Input(id='my-input', type='text', placeholder='Enter company name', style={'margin-right': '10px'}),
        html.Label("Time range:", style={'margin-right': '10px'}),
        dcc.Dropdown(
            id='time-range-dropdown',
            options=[
                {'label': '1D', 'value': '1d'},
                {'label': '5D', 'value': '5d'},
                {'label': '1M', 'value': '1mo'},
                {'label': '3M', 'value': '3mo'},
                {'label': '6M', 'value': '6mo'},
                {'label': 'YTD', 'value': 'ytd'},
                {'label': '1Y', 'value': '1y'},
                {'label': '2Y', 'value': '2y'},
                {'label': '5Y', 'value': '5y'},
                {'label': 'MAX', 'value': 'max'}
            ],
            value='1D',
            style={'width': '80px', 'margin-right': '10px'}
        ),
        html.Label("Interval time:", style={'margin-right': '10px'}),
        dcc.Dropdown(
             id='interval_time',
                options=[
                    {'label':'1h','value':'1h'},
                    {'label':'1d','value':'1d'},
                    {'label':'1w','value':'1wk'},
                ],
                value='1h',
                style={'marginRight': '10px','width': '100px','marginLeft':'5px'}
        ),
        html.Button('Submit', id='submit-button', n_clicks=0),
    ], style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '20px'}),

    html.Div([
        dcc.Graph(
            id='candlestick-chart',
            style={'width': '1200px'}
        )
    ])
], style={'background-color': '#add8e6', 'padding': '20px', 'display': 'flex', 'flex-direction': 'column', 'align-items': 'center'})

@app.callback(
    Output('candlestick-chart', 'figure'),
    [Input('submit-button', 'n_clicks')],
    [State('my-input', 'value'),
     State('time-range-dropdown', 'value'),
     State('interval_time', 'value')]
)
def update_output(n_clicks, input_value, time_range_value, interval_time):
    if n_clicks:
        try:
            yf_obj = Yfinance(input_value)
            stock_data = yf_obj.fetch_stock_data(time_range_value, interval_time)

            candlestick = go.Candlestick(x=stock_data.index,
                                         open=stock_data['Open'],
                                         high=stock_data['High'],
                                         low=stock_data['Low'],
                                         close=stock_data['Close'])
            
            trading_ticker = input_value.split('.')[0]
            title_html = f'<a href="https://www.tradingview.com/symbols/{trading_ticker}" target="_blank">{input_value}</a>'

            layout = go.Layout(
                title=title_html,
                xaxis_title='Date',
                yaxis_title='Price',
                plot_bgcolor='black', 
                paper_bgcolor='black', 
                xaxis=dict(showgrid=False, zeroline=False, tickfont=dict(color='white'), rangeslider=dict(visible=False)),  
                yaxis=dict(showgrid=False, zeroline=False, tickfont=dict(color='white')),
                font=dict(color='white') 
            )
            fig = go.Figure(data=[candlestick], layout=layout)
            
            return fig

        except Exception as e:
            return {
                'data': [],
                'layout': {
                    'title': 'Error',
                    'annotations': [{
                        'text': f'Error fetching data: {str(e)}',
                        'x': 0.5,
                        'y': 0.5,
                        'showarrow': False,
                    }],
                    'xaxis': {'visible': False},
                    'yaxis': {'visible': False},
                    'plot_bgcolor': 'black',  
                    'paper_bgcolor': 'black'  
                }
            }

    return {}

if __name__ == '__main__':
    app.run_server(debug=True)
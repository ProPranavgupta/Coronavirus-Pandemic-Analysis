import pandas as pd
import plotly.graph_objs as go
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px

external_stylesheets =[
    {
       'href':"https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css",
       'rel':"stylesheet",
       'integrity':"sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC",
       'crossorigin':"anonymous"
    }
 ]

patients = pd.read_csv('state_wise_daily data file.csv')

total = patients.shape[0]
active = patients[patients['Status'] =='Confirmed'].shape[0]
Recovered = patients[patients['Status'] =='Recovered'].shape[0]
Deaths = patients[patients['Status'] =='Deceased'].shape[0]

options=[
    {'label':'All', 'value':'All'},
    {'label':'Hospitalized', 'value':'Hospitalized'},
    {'label':'Recovered', 'value':'Recovered'},
    {'label':'Deceased', 'value':'Deceased'}
]

options1=[
    {'label':'All', 'value':'All'},
    {'label':'Mask','value':'Mask'},
    {'label':'Sanitizer', 'value':'Sanitizer'},
    {'label':'Oxygen', 'value':'Oxygen'},
]

options2=[
    {'label': 'All', 'value': 'Status'},
    {'label':'Red Zone', 'value':'Red Zone'},
    {'label':'Blue Zone','value':'Blue Zone'},
    {'label':'Green Zone', 'value':'Green Zone'},
    {'label':'Orange Zone', 'value':'Orange Zone'},
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1(children='Coronavirus Pandemic',style={'color':'White','textAlign':'center'}),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Total Cases",className='text-light'),
                    html.H4(total ,className='text-light'),
                ],className='card-body')
            ],className='card bg-danger')
        ],className="col-md-3"),
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Active Cases",className='text-light'),
                    html.H4(active ,className='text-light'),
                ],className='card-body')
            ],className='card bg-info')
        ],className="col-md-3"),
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Recovered Cases",className='text-light'),
                    html.H4(Recovered ,className='text-light'),
                ],className='card-body')
            ],className='card bg-warning')
        ],className="col-md-3"),
        html.Div([
                html.Div([
                html.Div([
                    html.H3("Total Deaths",className='text-light'),
                    html.H4(Deaths ,className='text-light'),
                ],className='card-body')
            ],className='card bg-success')
        ],className="col-md-3"),
    ],className="row"),


    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id='plot-graph', options= options1, value='All'),
                    dcc.Graph(id='graph')
                ],className='card-body')
            ],className='card'),
        ],className='col-md-6'),
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id='my_dropdown', options= options2,value='Status'),
                    dcc.Graph(id='the_graph')
                ],className='card-body')
            ],className='card'),
        ],className='col-md-6'),
    ],className="row"),


    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id='picker', options= options, value='All'),
                    dcc.Graph(id='bar')
                ],className='card-body')
            ],className='card')
        ],className="col-md-12"),
    ],className="row")
],className="container")


@app.callback(Output('bar','figure'),[Input('picker','value')])
def update_graph(type):

    if type == 'All':
        return {'data':[go.Bar(x=patients['State'],y=patients['Total'],)],
                'layout':go.Layout(title='Coronavirus Pandemic State Wise',plot_bgcolor='Orange')
                }
    if type == 'Hospitalized':
        return {'data':[go.Bar(x=patients['State'],y=patients['Hospitalized'])],
                'layout':go.Layout(title='Coronavirus Pandemic State Wise',plot_bgcolor='Orange')
                }
    if type == 'Recovered':
        return {'data':[go.Bar(x=patients['State'],y=patients['Recovered'])],
                'layout':go.Layout(title='Coronavirus Pandemic State Wise',plot_bgcolor='Orange')
                }
    if type == 'Deceased':
        return {'data':[go.Bar(x=patients['State'],y=patients['Deceased'])],
                'layout':go.Layout(title='Coronavirus Pandemic State Wise',plot_bgcolor='Orange')
                }
    return None

@app.callback(Output('graph','figure'),[Input('plot-graph','value')])
def generate_graph(type):

    if type == 'All':
        return {'data':[go.Scatter(x=patients['Status'],y=patients['Total'],mode='lines')],
                'layout':go.Layout(title='Commodities Total Count',plot_bgcolor='pink')
                }
    if type == 'Mask':
        return {'data':[go.Scatter(x=patients['Status'],y=patients['Mask'],mode='lines')],
                'layout':go.Layout(title='Commodities Total Count',plot_bgcolor='pink')
                }
    if type == 'Sanitizer':
        return {'data':[go.Scatter(x=patients['Status'],y=patients['Sanitizer'],mode='lines')],
                'layout':go.Layout(title='Commodities Total Count',plot_bgcolor='pink')
                }
    if type == 'Oxygen':
        return {'data':[go.Scatter(x=patients['Status'],y=patients['Oxygen'],mode='lines')],
                'layout':go.Layout(title='Commodities Total Count',plot_bgcolor='pink')
                }
    return None

@app.callback(Output('the_graph','figure'),[Input('my_dropdown','value')])
def generate_graph(my_dropdown):
    piechart=px.pie(data_frame=patients.head(10),names=my_dropdown,hole=0.51)
    return piechart

if __name__ == '__main__':
    app.run(debug=True)
#importing libraries
import plotly.express as px
import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import pandas as pd


#reading data
ds = pd.read_csv('datasets/dataset_clean.csv')


#Dash App
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG, 'assets/style.css'])
app.title = 'App Board'
server = app.server


#DataFrames
ds_prime = ds['Primary_Genre'].value_counts().rename_axis('Genre').reset_index(name='Counts')

ds_dev = ds['Developer_Name'].value_counts().rename_axis('Developer').reset_index(name='Counts')

ds_genre = ds.groupby('Primary_Genre', as_index=False)['Price_USD'].mean()
ds_genre = ds_genre.sort_values('Price_USD', ascending = False).reset_index(drop = True)

ds_rate = ds.groupby('Primary_Genre', as_index=False)[['Total_Average_Rating', 'Total_Number_of_Ratings', 'Average_Rating_For_Version', 'Number_of_Ratings_For_Version']].mean()
ds_rate = ds_rate.sort_values('Total_Average_Rating', ascending = False).reset_index(drop = True)


#Graphs
fig_1 = px.bar(ds_prime.head(7), y='Counts', x='Genre', color_discrete_sequence=["#4895ef"])
fig_1.update_layout(
    template="plotly_dark",
    title={
        'text': "Most Available Genre on App Store",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
        }
    )

fig_2 = px.bar(ds_dev.head(7), y='Counts', x='Developer', color_discrete_sequence=["#4895ef"])
fig_2.update_layout(
    template="plotly_dark",
    title={
        'text': "Developer with most Apps",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
    )

fig_3 = px.bar(ds_genre.head(15), x="Primary_Genre", y="Price_USD", color_discrete_sequence = ['#7b2cbf'])
fig_3.update_layout(
    template="plotly_dark",
    title={
        'text': "Average Price (USD) of Each Genre",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        },
    )

fig_4 = px.line(ds_rate.head(10), x="Primary_Genre", y="Total_Average_Rating", color_discrete_sequence=["#94d2bd"])
fig_4.update_layout(
    template="plotly_dark",
    title={
        'text': "Total Average Rating of Each Genre",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
    )

fig_5 = px.line(ds_rate.head(10), x="Primary_Genre", y="Total_Number_of_Ratings", color_discrete_sequence=["#94d2bd"])
fig_5.update_layout(
    template="plotly_dark",
    title={
        'text': "Total Number of Ratings of Each Genre",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
    )

fig_6 = px.line(ds_rate.head(10), x="Primary_Genre", y="Average_Rating_For_Version", color_discrete_sequence=["#94d2bd"])
fig_6.update_layout(
    template="plotly_dark",
    title={
        'text': "Average Rating for Version of Each Genre",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
    )

fig_7 = px.line(ds_rate.head(10), x="Primary_Genre", y="Number_of_Ratings_For_Version", color_discrete_sequence=["#94d2bd"])
fig_7.update_layout(
    template="plotly_dark",
    title={
        'text': "Number of Ratings for Version of Each Genre",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
    )


#Visulaization
app.layout = html.Div([
                
                dbc.Row(dbc.Col(html.H3("App Board"), style = {'text-align':'center','color':'white', 'font-size':'40px','margin-top':'20px', 'margin-bottom':'20px'},),),
                
                dbc.Row([    
                    dbc.Col
                    (
                        [
                            html.Div([
                                dcc.Graph(id='graph1',figure=fig_1,),
                                ], style = {'margin-left':'20px',},),
                            ], style = {'width': '49%', 'display': 'inline-block',},
                        ),
                    dbc.Col
                    (
                        [
                            html.Div([
                                dcc.Graph(id='graph2',figure=fig_2,),
                                ], style = {'margin-right':'20px',},),
                            ], style = {'width': '49%', 'display': 'inline-block'},
                        ),

                ],),

                dbc.Row([
                    dbc.Col
                    (
                        [
                            html.Div([
                                dcc.Graph(id='graph3',figure=fig_3,),
                                ], style = {'margin-left':'20px', 'margin-right':'20px'},),
                            ], style = {'display': 'inline-block', 'margin-top':'25px', 'margin-bottom':'25px'},
                        ),
                ],),

                dbc.Row([      
                    dbc.Col
                    (
                        [
                            html.Div([
                                dcc.Graph(id='graph4',figure=fig_4,),
                                ], style = {'margin-left':'20px',},),
                            ], style = {'width': '50%', 'display': 'inline-block'},
                        ),
                    dbc.Col
                    (
                        [
                            html.Div([
                                dcc.Graph(id='graph5',figure=fig_5,),
                                ], style = {'margin-right':'20px',},),
                            ], style = {'width': '50%', 'display': 'inline-block',},
                        ),
                ],),

                dbc.Row([
                    dbc.Col
                    (
                        [
                            html.Div([
                                dcc.Graph(id='graph6',figure=fig_6,),
                                ], style = {'margin-left':'20px',},),
                            ], style = {'width': '50%', 'display': 'inline-block', 'margin-top':'25px', 'margin-bottom':'25px'},
                        ),
                    dbc.Col
                    (
                        [
                            html.Div([
                                dcc.Graph(id='graph7',figure=fig_7,),
                                ], style = {'margin-right':'20px',},),
                            ], style = {'width': '50%', 'display': 'inline-block', 'margin-top':'25px', 'margin-bottom':'25px'},
                        ),
                ],),
            ], 
        style = {'background-color':'black'},
    )


if __name__ == '__main__':
    app.run_server()
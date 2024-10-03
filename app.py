import dash
import dash_bootstrap_components as dbc
import os
from typing import Container
import plotly.express as px
import pandas as pd
from dash import dcc,html
from dash.dependencies import Output, Input
import plotly.tools as tls
import plotly.graph_objs
from plotly.tools import mpl_to_plotly
import os
os.getcwd()

# bootstrap theme
# https://bootswatch.com/lux/
external_stylesheets = [dbc.themes.LUX]

app = dash.Dash(
    __name__, 
    meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}],
    assets_external_path='assets/',
    external_stylesheets=external_stylesheets,
    requests_pathname_prefix='/FDMProject_Airline_Satisfaction/',
    )

server = app.server
app.config.suppress_callback_exceptions = True


# building the navigation bar
# https://github.com/facultyai/dash-bootstrap-components/blob/master/examples/advanced-component-usage/Navbars.py
dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Catogorical Visualization", href="/classification"),
        dbc.DropdownMenuItem("Ratings", href="/pie_chart")


    ],
    nav = True,
    in_navbar = True,
    label = "Explore",
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="/assets/icon.png", height="80px")),
                        dbc.Col(dbc.NavbarBrand("AIR U.S.", className="ml-2")),
                    ],
                    align="center",
                ),
                href="/home",
            ),
            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    # right align dropdown menu with ml-auto className
                    [dropdown], className="ml-auto", navbar=True
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ]
    ),
    color="#17252A",
    dark=True,
    className="mb-4 navBar",
)

def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

for i in [2]:
    app.callback(
        Output(f"navbar-collapse{i}", "is_open"),
        [Input(f"navbar-toggler{i}", "n_clicks")],
        [State(f"navbar-collapse{i}", "is_open")],
    )(toggle_navbar_collapse)

# embedding the navigation bar
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
],
style = {
    "background":"#7991ab"
}
)


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/classification':
        return classification.layout
    elif pathname == '/pie_chart':
        return pie_chart.layout
    else:
        return classification.layout

if __name__ == '__main__':
    app.run_server(debug=False)
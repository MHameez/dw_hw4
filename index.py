from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from utils import get_nav_buttons
from app import app
from pages import (
    opening,
    scatter, scatter_intro, scatter_outro,
    genre_analysis, genre_analysis_intro,
    features,features_intro,features_outro,
    lyrics, lyrics_intro, lyrics_outro,
    closing
)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dbc.Container([
        dbc.Row([
            dbc.Col(html.Div([
                html.H3(id="title", children=""),
                html.Div(id="navs")
            ]), className="text-center"),
        ]),
        dbc.Row([
            dbc.Col(
                id="content",
                children=[],
                width=9
            ),
            dbc.Col(id="description", width=3)
        ]),
    ])
])


@app.callback(
    [
        Output('title', 'children'),
        Output('content', 'children'),
        Output('description', 'children'),
        Output('navs', 'children')
    ],
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == "/":
        return opening.title, opening.content, opening.description, \
               get_nav_buttons(None, "#", "oi-media-play", "/scatter/intro", None)
    elif pathname == "/scatter/intro":
        return scatter_intro.title, scatter_intro.content, scatter_intro.description, \
               get_nav_buttons("oi-media-step-backward", "/", "oi-media-step-forward", "/scatter/reff", 1)
    elif pathname == "/scatter/reff":
        return scatter.title, scatter.content, scatter.description, \
               get_nav_buttons("oi-media-step-backward", "/scatter/intro", "oi-media-step-forward", "/scatter/outro", 2)
    elif pathname == "/scatter/outro":
        return scatter_outro.title, scatter_outro.content, scatter_outro.description, \
               get_nav_buttons("oi-media-step-backward", "/scatter/reff", "oi-media-step-forward", "/genres/intro", 3)
    elif pathname == "/genres/intro":
        return genre_analysis_intro.title, genre_analysis_intro.content, genre_analysis_intro.description, \
               get_nav_buttons("oi-media-step-backward", "/scatter/outro", "oi-media-step-forward", "/genres/reff", 4)
    elif pathname == "/genres/reff":
        return genre_analysis.title, genre_analysis.content, genre_analysis.description, \
               get_nav_buttons("oi-media-step-backward", "/genres/intro", "oi-media-step-forward", "/features/intro", 5),
    elif pathname == "/features/intro":
        return features_intro.title, features_intro.content, features_intro.description, \
               get_nav_buttons("oi-media-step-backward", "/genres/reff", "oi-media-step-forward", "/features/reff", 6)
    elif pathname == "/features/reff":
        return features.title, features.content, features.description, \
               get_nav_buttons("oi-media-step-backward", "/features/intro", "oi-media-step-forward", "/features/outro", 7)
    elif pathname == "/features/outro":
        return features_outro.title, features_outro.content, features_outro.description, \
               get_nav_buttons("oi-media-step-backward", "/features/reff", "oi-media-step-forward", "/lyrics/intro", 8)
    elif pathname == "/lyrics/intro":
        return lyrics_intro.title, lyrics_intro.content, lyrics_intro.description, \
               get_nav_buttons("oi-media-step-backward", "/features/outro", "oi-media-step-forward", "/lyrics/reff", 9)
    elif pathname == "/lyrics/reff":
        return lyrics.title, lyrics.content, lyrics.description, \
               get_nav_buttons("oi-media-step-backward", "/lyrics/intro", "oi-media-step-forward", "/lyrics/outro", 10)
    elif pathname == "/lyrics/outro":
        return lyrics_outro.title, lyrics_outro.content, lyrics_outro.description, \
               get_nav_buttons("oi-media-step-backward", "/lyrics/reff", "oi-media-step-forward", "/encore", 11)
    elif pathname == "/encore":
        return closing.title, closing.content, closing.description, \
               get_nav_buttons("oi-media-step-backward", "/lyrics/outro", "oi-home", "/", None)
    return opening.title, opening.content, opening.description, \
           get_nav_buttons(None, "#", "oi-media-play", "/scatter/intro", None)


server = app.server


if __name__ == '__main__':
    app.run_server(debug=True)

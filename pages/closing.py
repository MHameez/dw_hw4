import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from app import app

title = "What's next?"

content = dbc.Row(children=[
    html.Div(children=[
        html.H4("Story recap", className="text-info"),
        dcc.Markdown("""
            The journey for our story began when we noticed a very interesting fact in the Top 2000 chart. *Bohemian Rhapsody* a song performed by *Queen*, a band not active for almost 30 years, has been on the top of the chart consecutively until today. The aforementioned fact got us wondering, thus we formulated the following main question and subquestion:
        """),
        dcc.Markdown("""
            > #### *Why people prefer listening to old music...?*
            > - What drives them to listen to songs from old eras...?
        """),
        dcc.Markdown("""
        In order to adrress these questions, we looked for answers by analysing, combining and aggregating information from the Dutch Top 2000 dataset and the Spotify API. We developed the present story in which we exhibit 4 interactive visualizations. Through these visualizations we attempted to provide a spherical representation of our findings. In the following section a summary of our main findings is presented.   
        """),
    ]),
    html.Div(children=[
        html.H4("Final remarks", className="text-info"),
        dcc.Markdown("""
            Our analysis indeed demonstrates that people prefer listening to songs from older eras. The first two visualizations contain information about the song rankings throughout the years. The derived insights confirm that the top ranked songs until today are from the oldest era i.e. songs released from 1920 to 1989. In addition, the genre that dominates in the top seeds is *Rock*. We observe an emerging *Pop* genre in the top seeds especially in the last decade for the international stage but the Dutch preferences persist the old good *Rock*.  
        """),
        dcc.Markdown("""
            In the last two visualizations we made an effort to address the causality behind these preferences. In the third visualiation, analyzing the song features we discovered that older era songs are substanitally more *instrumental*, more *positive* and contain more *vocals*. This last finding is aligned with our discoveries in the last visualization where we conclude that the lyrics from the old era are more diverse and that songs from the last decade attempt to have lyrics similar to the old era. This indicates, that probably the music industry is aware of the success of the older songs and attempts to releease new songs which might have similar characteristics and lyrics of the old era.
        """),
    ]),
    
    dbc.Row([
        dbc.Col(
            html.Img(
                src=app.get_asset_url('imgs/bob.png'),
                className="img-fluid mx-auto d-block"
            ),
            width=3
        ),
        dbc.Col([
            html.Div([
                html.Em("One good thing about music,"), html.Br(),
                html.Em("when it hits you, you feel no pain.")
            ]),
            html.Div(
                "- Bob Marley"
            )
        ],
            width=4
        ),
    ])
])

description = html.Div([
    html.H5("Data & Methodology", className="text-info"),
    html.P([
        "The ranking data is based on ",
        dcc.Link("NPO Radio 2 Top 2000", href="https://www.nporadio2.nl/top2000"),
        " and retrieved via the corresponding ",
        dcc.Link("Wikipedia page",
                 href="https://nl.wikipedia.org/wiki/Lijst_van_Radio_2-Top_2000%27s"),
        ". Song features are gathered with ",
        dcc.Link("Spotify API",
                 href="https://developer.spotify.com/documentation/web-api/quick-start/"),
        " using the ",
        dcc.Link("spotipy", href="https://github.com/plamere/spotipy"),
        " library."
    ]),
    html.P([
        "Lyrics are collected from ",
        dcc.Link("lyrics.wikia.com", href="http://lyrics.wikia.com/"),
        " using the ",
        dcc.Link("lyricwikia", href="https://pypi.org/project/lyricwikia/"),
        " library and ",
        dcc.Link("musixmatch", href="https://www.musixmatch.com/"),
        ". We use pre-train embeddings from ",
        dcc.Link("Google", href="https://code.google.com/archive/p/word2vec/"),
        " for the English songs and ",
        dcc.Link("dutchembeddings", href="https://github.com/clips/dutchembeddings"),
        " for Dutch."
    ]),
    html.P([
        "Visuals developed with ",
        dcc.Link("Dash", href="https://plotly.com/dash/"),
        " and hosted in ",
        dcc.Link("Heroku", href="https://www.heroku.com/"),
        ". Website template is based on ",
        dcc.Link("Bootswatch", href="https://bootswatch.com/"),
        "."
    ]),
    html.H5("Composed by", className="text-info"),
    html.Ul([
        html.Li(dcc.Link("Chris Papas", href="https://www.linkedin.com/in/christos-papas-a2ba76172/")),
        html.Li(dcc.Link("Hameez Ariz", href="https://www.linkedin.com/in/hameez-ariz/")),
        html.Li(dcc.Link("Nemania Borovits", href="https://www.linkedin.com/in/nemania-borovits-8306b812a/")),
        html.Li(dcc.Link("Yosef Winatmoko", href="https://www.linkedin.com/in/yosef-ardhito-winatmoko-053a5754/")),
    ])
])

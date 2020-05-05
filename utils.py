import dash_html_components as html
import pickle

song_features = [
    'duration_ms', 'followers', 'analysis_loudness', 'analysis_tempo',
    'feature_danceability', 'feature_energy', 'feature_speechiness', 'feature_instrumentalness', 
    'feature_liveness', 'feature_valence'
]


def generate_table(dataframe, max_rows):

    """ A function which returns a responsive html table provided a dataframe """

    return html.Div(children=[
        html.Table([
            html.Thead(
                html.Tr([html.Th(col) for col in dataframe.columns])
            ),
            html.Tbody([
                html.Tr([
                    html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
                ]) for i in range(min(len(dataframe), max_rows))
            ])
        ], className="table-bordered")
    ], className="table-responsive")

def create_initial_era_df(df):

    era_df = df.groupby(["title", "era", "hp"]).count().reset_index()[["title", "era", "hp", "artist"]].rename(columns={"artist": "count"})
    era_df["era_rank"] = era_df.groupby("era").rank(method="first")["hp"]
    best_era_df = df[df["title"].isin(era_df[era_df["era_rank"] < 200]["title"].unique())].copy()[["title", "era"] + song_features].dropna().reset_index()
    first_title_df = best_era_df[["index", "title"]].groupby("title").rank(method="first")
    best_era_df = best_era_df[first_title_df["index"] == 1]
    del best_era_df["index"]
    del best_era_df["title"]
    best_era_df.columns = [
        "era", "Duration", "Mainstream", "Loudness", "Tempo",
        "Danceability", "Energy", "Speechiness", "Instrumentalness",
        "Liveness", "Valence"
    ]

    best_era_df.to_pickle('data/best_era_df2.pkl')

def create_era_df(df):

        with open('data/best_era_df2.pkl', 'rb') as input_file:
            best_era_df2 = pickle.load(input_file)
        
        best_era_df2 = best_era_df2.groupby("era").mean().reset_index().melt(id_vars=["era"])
        compare_oldies_df = best_era_df2[best_era_df2["era"] == "oldies"][["variable", "value"]].rename(columns={"value": "value_oldies"})
        best_era_df2 = best_era_df2.merge(compare_oldies_df, how="left", on="variable")
        best_era_df2["relative_to_oldies"] = (best_era_df2["value"] - best_era_df2["value_oldies"]) * 100 / best_era_df2["value_oldies"]
        best_era_df2["era"] = best_era_df2["era"].map({"oldies": "1920-1989", "90s": "1990-1999", "2000s": "2000-2020"})
        best_era_df2 = best_era_df2[["era", "variable", "relative_to_oldies"]].sort_values(["era", "relative_to_oldies"])
        best_era_df2.columns = ["Song Era", "Song Features", "Compared to Oldies (Song Released < 1990)"]

        return best_era_df2

def get_max_each_feature(df):

    max_songs={}
    for feature in song_features:
        # print(feature)
        row = df.loc[df[feature].idxmax()]
        max_songs[feature] = row['title']+ '_'+row['artist']+'_'+row['main_genre']
    
    return max_songs
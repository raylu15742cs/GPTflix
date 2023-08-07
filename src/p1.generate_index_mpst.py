# Python Standard Library
import warnings

# Third Party Libraries
import pandas as pd

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=FutureWarning)



def combine_text_to_one_column(df):
    df["gpttext"] = (
    "person_id: " + df["person_id"]
    + " first_name: " + df["first_name"]
    + " last_name: " + df["last_name"]
    + " display_first_last: " + df["display_first_last"]
    + " display_last_comma_first: " + df["display_last_comma_first"]
    + " display_fi_last: " + df["display_fi_last"]
    + " player_slug: " + df["player_slug"]
    + " birthdate: " + df["birthdate"]
    + " school: " + df["school"]
    + " country: " + df["country"]
    + " last_affiliation: " + df["last_affiliation"]
    + " height: " + df["height"]
    + " weight: " + df["weight"]
    + " season_exp: " + df["season_exp"]
    + " jersey: " + df["jersey"]
    + " position: " + df["position"]
    + " rosterstatus: " + df["rosterstatus"]
    + " games_played_current_season_flag: " + df["games_played_current_season_flag"]
    + " team_id: " + df["team_id"]
    + " team_name: " + df["team_name"]
    + " team_abbreviation: " + df["team_abbreviation"]
    + " team_code: " + df["team_code"]
    + " team_city: " + df["team_city"]
    + " playercode: " + df["playercode"]
    + " from_year: " + df["from_year"]
    + " to_year: " + df["to_year"]
    + " dleague_flag: " + df["dleague_flag"]
    + " nba_flag: " + df["nba_flag"]
    + " games_played_flag: " + df["games_played_flag"]
    + " draft_year: " + df["draft_year"]
    + " draft_round: " + df["draft_round"]
    + " draft_number: " + df["draft_number"]
    + " greatest_75_flag: " + df["greatest_75_flag"]
)

    df = df.drop(df.columns[[0, 1, 2, 3, 4]], axis=1)

    df.to_csv(f"data_sample/converted_common_player_info.csv")


if __name__ == "__main__":
    # This is a sample converter that takes CSV data from a table
    # (in this case the Kaggle dataset here https://www.kaggle.com/datasets/cryptexcode/mpst-movie-plot-synopses-with-tags )
    # and converts this data into a CSV that contains a single column
    # with a block of text that we want to make accessible on our Pinecone database


    # read sample data
    df = pd.read_csv(
        filepath_or_buffer="data_sample/common_player_info.csv",
        sep=",",
        header=0,
        dtype="string",
        encoding="utf-8",
    )

    combine_text_to_one_column(df=df)

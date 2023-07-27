# Python Standard Library
import warnings

# Third Party Libraries
import pandas as pd

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=FutureWarning)



def combine_text_to_one_column(df):
    df["gpttext"] = (
    "person_id: " + df["person_id"].astype(str)
    + " first_name: " + df["first_name"].astype(str)
    + " last_name: " + df["last_name"].astype(str)
    + " display_first_last: " + df["display_first_last"].astype(str)
    + " display_last_comma_first: " + df["display_last_comma_first"].astype(str)
    + " display_fi_last: " + df["display_fi_last"].astype(str)
    + " player_slug: " + df["player_slug"].astype(str)
    + " birthdate: " + df["birthdate"].astype(str)
    + " school: " + df["school"].astype(str)
    + " country: " + df["country"].astype(str)
    + " last_affiliation: " + df["last_affiliation"].astype(str)
    + " height: " + df["height"].astype(str)
    + " weight: " + df["weight"].astype(str)
    + " season_exp: " + df["season_exp"].astype(str)
    + " jersey: " + df["jersey"].astype(str)
    + " position: " + df["position"].astype(str)
    + " rosterstatus: " + df["rosterstatus"].astype(str)
    + " games_played_current_season_flag: " + df["games_played_current_season_flag"].astype(str)
    + " team_id: " + df["team_id"].astype(str)
    + " team_name: " + df["team_name"].astype(str)
    + " team_abbreviation: " + df["team_abbreviation"].astype(str)
    + " team_code: " + df["team_code"].astype(str)
    + " team_city: " + df["team_city"].astype(str)
    + " playercode: " + df["playercode"].astype(str)
    + " from_year: " + df["from_year"].astype(str)
    + " to_year: " + df["to_year"].astype(str)
    + " dleague_flag: " + df["dleague_flag"].astype(str)
    + " nba_flag: " + df["nba_flag"].astype(str)
    + " games_played_flag: " + df["games_played_flag"].astype(str)
    + " draft_year: " + df["draft_year"].astype(str)
    + " draft_round: " + df["draft_round"].astype(str)
    + " draft_number: " + df["draft_number"].astype(str)
    + " greatest_75_flag: " + df["greatest_75_flag"].astype(str)
)

    df = df.drop(df.columns[[0, 1, 2, 3, 4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]], axis=1)

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

# Python Standard Library
import warnings

# Third Party Libraries
import pandas as pd

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=FutureWarning)



def combine_text_to_one_column(df):
    df["gpttext"] = (
        "team_id: "
        + df["team_id"].astype(str)
        + " city: "
        + df["city"].astype(str)
        + " nickname: "
        + df["nickname"].astype(str)
        + " year_founded: "
        + df["year_founded"].astype(str)
        + " year_active_till: "
        + df["year_active_till"].astype(str)
    )

    df = df.drop(df.columns[[0, 1, 2, 3, 4]], axis=1)

    df.to_csv(f"../data_sample/team_history_converted.csv")


if __name__ == "__main__":
    # This is a sample converter that takes CSV data from a table
    # (in this case the Kaggle dataset here https://www.kaggle.com/datasets/cryptexcode/mpst-movie-plot-synopses-with-tags )
    # and converts this data into a CSV that contains a single column
    # with a block of text that we want to make accessible on our Pinecone database


    # read sample data
    df = pd.read_csv(
        filepath_or_buffer="../data_sample/team_history.csv",
        sep=",",
        header=0,
        dtype="string",
        encoding="utf-8",
    )

    combine_text_to_one_column(df=df)

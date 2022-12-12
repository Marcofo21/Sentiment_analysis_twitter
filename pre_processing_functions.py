import re
import pandas as pd


def find_hashtags(tweet):
    """
    This function extracts text preceded by hashtags (i.e. hashtags in the social media jargon)
    from a string of text.

        Args:
            tweet (string): a string of text.

        Returns:
            out (list): list with all unique hashtags in the tweet (or other type of text).
    """

    out = re.findall("(#[A-Za-z]+[A-Za-z0-9-_]+)", tweet)

    return out


def extract_hashtags(tweet, df):
    """
    This function extracts all unique hashtags from a column of strings in a dataframe
    and returns them in a a DataFrame containing all hashtags.

        Args:
            tweet (string): name of the column to be searched in the dataframe.
            df (DataFrame): dataframe containing the texts to be searched.

        Returns:
            out (list): list with all unique hashtags in the set of texts.

    """

    temp = df.tweet.apply(find_hashtags)
    hashtag_list = temp.to_list()
    out = pd.DataFrame([item for sublist in hashtag_list for item in sublist])

    return out

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

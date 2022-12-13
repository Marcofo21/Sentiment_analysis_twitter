import regex as re
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


def url_cleaner(urls):

    """
    This function cleans strings of URLs so that only the domain and second-level domain
    are left.

        Args:
            urls (string): a string of text.

        Returns:
            out (string): string cleaned of subdomains, top-level domains, and scheme.
    """

    out = re.sub(r"https?:\/\/", "", urls)
    out = re.sub(r"www\.", "", out)
    out = re.sub(r"\.com", "", out)
    out = re.sub(r"\.html", "", out)
    out = re.sub(r"\/.+", "", out)

    return out

import re

def find_hashtags(tweet):
    """
    This function extracts text preceded by hashtags (i.e. hashtags in the social media jargon) from lines of text.

        Args:
            tweet (object): collection of texts.

        Return:
            out (list): list with all unique hashtags in the set of tweets (or other type of text). 
    """

    out = re.findall('(#[A-Za-z]+[A-Za-z0-9-_]+)', tweet)
    
    return out
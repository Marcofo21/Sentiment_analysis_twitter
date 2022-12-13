import pytest
import regex as re
import pandas as pd
import pre_processing_functions as pp


@pytest.fixture
def hashtag_finder_input():
    out = {"tweet": "Watch #BeforeTheFlood123@4dasPè right here"}
    return out


def test_hashtag_finder(hashtag_finder_input):

    hashtag = pp.find_hashtags(**hashtag_finder_input)

    assert hashtag == "#BeforeTheFlood123@4dasPè"

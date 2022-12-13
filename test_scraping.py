import pytest
import regex as re
import pandas as pd
import pre_processing_functions as pp


@pytest.fixture
def hashtag_finder_input():
    out = {"tweet": "Watch #BeforeTheFlood123@4dasPè #ciao right here"}
    return out


@pytest.fixture
def url_cleaner_input():
    out = {
        "url": """https://stackoverflow.com/questions
        /11346283/renaming-column-names-in-pandas?page
        =1&tab=scoredesc#tab-top"""
    }
    return out


def test_hashtag_finder_base(hashtag_finder_input):

    hashtag = pp.find_hashtags(**hashtag_finder_input)

    assert hashtag == ["#BeforeTheFlood123", "#ciao"]


def test_url_cleaner_base(url_cleaner_input):

    domain = pp.url_cleaner(**url_cleaner_input)

    assert domain == "stackoverflow"

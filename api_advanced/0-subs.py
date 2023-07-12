#!/usr/bin/python3
"""return number of subs"""
import requests


def number_of_subscribers(subreddit):
    """func."""
    url = "https://www.reddit.com/r/{}/about.json" \
        .format(subreddit)

    res = requests.get(url,
                       headers={
                           'User-Agent': 'Mozilla/5.0'})

    if res.status_code != 200:
        return 0
    else:
        json_response = res.json()
        return json_response.get('data').get('subscribers')

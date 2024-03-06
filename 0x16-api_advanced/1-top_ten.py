#!/usr/bin/python3
"""
    This is a module that queries the reddit API
    and prints the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    This method returns the first 10 hot posts
    args:
        subreddit: the name of the subreddit to query
    return:
        The number of first 10 hot or 0 on failure.
    """

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Request from Peace (API advanced Project)"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            title = post['data']['title']
            print(title)
    else:
        print(None)

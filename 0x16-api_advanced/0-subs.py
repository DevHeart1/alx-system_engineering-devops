#!/usr/bin/python3
"""
    This is a module that queries the reddit API 
    and returns the number of subscribers of a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
        This method returns the number of subscribers
        args: 
            subreddit: the name of the subreddit to query
        return:
            The number of subscribers or 0 on failure.  
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Request from Peace(API advanced Project)"}
    response = request.get(url, headers == headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json().get("data").get("subscibers")
    else:
        return 0

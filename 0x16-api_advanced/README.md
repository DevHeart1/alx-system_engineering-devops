<h1>0x16. API advanced</h1>
<h3>Python</h3>
<h3>Scripting</h3>
<h3>Back-end</h3>
<h3>API</h3>

<p>Background Context
Questions involving APIs are common for interviews. Sometimes they’re as simple as ‘write a Python script that queries a given endpoint’, sometimes they require you to use recursive functions and format/sort the results.

A great API to use for some practice is the Reddit API. There’s a lot of endpoints available, many that don’t require any form of authentication, and there’s tons of information to be parsed out and presented. Getting comfortable with API calls now can save you some face during technical interviews and even outside of the job market, you might find personal use cases to make your life a little bit easier.</p>

<h3>Learning Objectives</h3>
<p>How to read API documentation to find the endpoints you’re looking for</p>
<br>How to use an API with pagination</br>
</b>How to parse JSON results from an API</br>
</b>How to make a recursive API call</br>
</b>How to sort a dictionary by value</br>

<h3>Tasks</h3>

<p>0. How many subs?
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.

Hint: No authentication is necessary for most features of the Reddit API. If you’re getting errors related to Too Many Requests, ensure you’re setting a custom User-Agent.

<p>Requirements:

Prototype: def number_of_subscribers(subreddit)
If not a valid subreddit, return 0.
NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.</p>
wintermancer@lapbox ~/reddit_api/project $ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
import sys

if __name__ == '__main__':
    number_of_subscribers = __import__('0-subs').number_of_subscribers
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
wintermancer@lapbox ~/reddit_api/project $ python3 0-main.py programming
756024
wintermancer@lapbox ~/reddit_api/project $ python3 0-main.py this_is_a_fake_subreddit
0
Repo:

GitHub repository: alx-system_engineering-devops
Directory: 0x16-api_advanced
File: 0-subs.py</p>
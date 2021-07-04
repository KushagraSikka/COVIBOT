import os
import tweepy as tw
# import pandas as pd

consumer_key= 'tM5jpHmfqiLzoN7kazlQJZW9K'
consumer_secret= '3Sqwl7cjjJ5dFr0ZO8zzusm4GISQpajHxhFJjZVfUWkLjT84ht'
access_token= '1389572192602525704-czbAyP7uWMjHipvLESNzG2T0JkAinM'
access_token_secret= 'QSTHj8hS0Xu1d3nom5hdMbdNs7MD6lm9yCJXHqqEiOuY8'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

date_since = "2021-04-01"

def twi(search_words):
    new_search = search_words + " -filter:retweets" 
    tweets = tw.Cursor(api.search,
              q=new_search,
              since=date_since).items(1)
    for tweet in tweets:
       return tweet.text



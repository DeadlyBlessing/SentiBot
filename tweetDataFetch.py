
import os
import re
import numpy as np
import tweepy as tw
from requests_oauthlib import OAuth1Session
import csv
import json



def json_maker(text):
    consumer_key = "ydKKAoXFmqq97PZWYPs4wfy5S"
    consumer_secret = "G1tFaa0Gop0kGCYsZzUpx1RLYjvIFv8qwS9H5dreZkgqlfCEnR"
    access_token = "856759533640622080-HhlrgshaitB8gR2TXvrBq60XtNeRnXP"
    access_token_secret = "8GYPov3JIJAJD8o2PvkGtdrXwUy5HewqEOXeTdAwKZP5Q"

    auth = tw.OAuthHandler(consumer_key, consumer_secret, callback=None)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth)


    search_words = "arnab goswami"
    date_since = "2018-11-16"

    new_search = search_words + " -filter:retweets"
    item = 100

    coordinates = '77.545,57.487,500mi'
    # Collect tweets
    tweets = tw.Cursor(api.search,
                q=new_search, tweet_mode = 'extended',
                lang="en", geocode = coordinates,
                since=date_since).items(item)

                
    twe_dict = {}
    key = range(item)

    #values = [tweet.text]
    tweet_dict = [[tweet.full_text] for tweet in tweets]
    for i in key:
        twe_dict[i] = tweet_dict[i]
    #print(twe_dict)


    #print(json.dumps(twe_dict, indent = 4 ))
    with open("tweet.json", "w") as outfile: 
        json.dump(twe_dict, outfile) 
    
   

        
        
        
       
    
    


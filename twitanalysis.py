#Imports
import json
import pandas as pd
import matplotlib.pyplot as plt

#We load json data store all tweets in a list.
tweets_data_path = './data/twitter_API_data.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

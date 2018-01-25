import tweepy
from tweepy import OAuthHandler, Stream
from textblob import TextBlob
#Credentials
ACCESS_TOKEN = '878103708357148673-T3qTnMtKUEkCPN7zKUPjmK0zE4TCMSk'
ACCESS_TOKEN_SECRET = 'M5IOVTDQvKcaE7NQLSL94Scrol2OtmPpnSkQT7aav6xT1'
CONSUMER_KEY = 'z2jh1jxHEWHtIc0I0fZUmWalo'
CONSUMER_SECRET = 'TCTLwdn7282qngW9Pq655fWhJ7KYtpzWSVXJqy85MUsxlfskQa'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
public_tweets = api.search('Football')

for tweets in public_tweets:
    print(tweets.text)
    analysis = TextBlob(tweets.text)
    print(analysis.sentiment.polarity)
#WORKED !!

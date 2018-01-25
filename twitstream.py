
#Created simple one in teststream.py

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream

#Credentials
ACCESS_TOKEN = '878103708357148673-T3qTnMtKUEkCPN7zKUPjmK0zE4TCMSk'
ACCESS_TOKEN_SECRET = 'M5IOVTDQvKcaE7NQLSL94Scrol2OtmPpnSkQT7aav6xT1'
CONSUMER_KEY = 'z2jh1jxHEWHtIc0I0fZUmWalo'
CONSUMER_SECRET = 'TCTLwdn7282qngW9Pq655fWhJ7KYtpzWSVXJqy85MUsxlfskQa'

#Listener object
class StdOutListener(StreamListener):

    def on_data(self, data):
        """Just prints out incoming data to the stdout"""
        print (data)
        return True

    def on_error(self, status):
        print (status)

if __name__ == '__main__':

    #Handles Twitter authentification and the connection to Twitter Streaming API.
    l = StdOutListener()
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    stream = Stream(auth, l)

    #Filter the tweets according to your requirements.
    stream.filter(track=['#epl', '#bpl'])
    # Can be set up for python,ruby and javascript.

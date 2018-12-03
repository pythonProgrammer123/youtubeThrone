import urllib.request
import json
import time
import tweepy
import os
import datetime

consumer_key = os.environ.get("consumer_key")
consumer_secret = os.environ.get("consumer_secret")
access_key = os.environ.get("access_key")
access_secret = os.environ.get("access_secret")
YouTubeKey = os.environ.get("YouTubeKey")

def sendMessage(message):
    global consumer_key, consumer_secret, access_key, access_secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    api.update_status(message)
    
sendMessage("We're online! On Heroku!!")
    
#calculation began here
while True:
    pewdsData = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=pewdiepie&key="+YouTubeKey).read()
    pewdsSubs = json.loads(pewdsData)["items"][0]["statistics"]["subscriberCount"]
    Tdata = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=tseries&key="+YouTubeKey).read()
    Tsubs = json.loads(Tdata)["items"][0]["statistics"]["subscriberCount"]
    if int(pewdsSubs) > int(Tsubs):
        print("We're okay!")
        break
    elif int(Tsubs) > int(pewdsSubs):
        sendMessage("T-Series(@TSeries)---" + "{:,d}".format(int(Tsubs)) + "\nPewDiePie(@pewdiepie)---" + "{:,d}".format(int(pewdsSubs)) + "\nthis means that T-Series has officially dethroned PewDiePie and now is the most subscribed YouTube channel, rip PewDiePie")
        sendMessage(datetime.datetime.now().strftime("On this day, %d/%m/%y and at this time, %H:%M:%S, T-Series has successfully dethroned PewDiePie"))
        print("WE'RE NOT OKAY!")
        break

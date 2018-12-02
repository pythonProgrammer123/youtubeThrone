import urllib.request
import json
import time
import tweepy

consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""
YouTubeKey = ""

def sendMessage(message):
    global consumer_key, consumer_secret, access_key, access_secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    api.update_status(message)
    
sendMessage("We're online!")
    
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
        print("WE'RE NOT OKAY!")
        break
sendMessage(pewdsSubs)

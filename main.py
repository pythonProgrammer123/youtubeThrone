import urllib.request
import json
import time
import tweepy

consumer_key = "iVJaO3fNsSn8ePU1jWQWpgwyh"
consumer_secret = "COw8ZPBRjc7gMsupyu5AP0csYCcMeBoaC6ouGz7uYvlTk0Z0Bx"
access_key = "805569973930205184-SRmHhyRz8chFbC4A4g5DbiSOijg6876"
access_secret = "xT8YjbyCFlKIYTKlXqsh5nKEM2R8W8wOCGL7gJo3g97Hx"
YouTubeKey = "AIzaSyAm_9jbzKZX6oBUu_xxmLo45Jv5-l4qjzY"

def sendMessage(message):
    global consumer_key, consumer_secret, access_key, access_secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    api.update_status(message)

#calculation began here
while True:
    pewdsData = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=pewdiepie&key="+YouTubeKey).read()
    pewdsSubs = json.loads(pewdsData)["items"][0]["statistics"]["subscriberCount"]
    Tdata = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=tseries&key="+YouTubeKey).read()
    Tsubs = json.loads(Tdata)["items"][0]["statistics"]["subscriberCount"]
    if int(pewdsSubs) > int(Tsubs):
        print("We're okay!")
    elif int(Tsubs) > int(pewdsSubs):
        sendMessage("T-Series(@TSeries)---" + "{:,d}".format(int(Tsubs)) + "\nPewDiePie(@pewdiepie)---" + "{:,d}".format(int(pewdsSubs)) + "\nthis means that T-Series has officially dethroned PewDiePie and now is the most subscribed YouTube channel, rip PewDiePie")
        print("WE'RE NOT OKAY!")
        break

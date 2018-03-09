"""
This file contains the methods used to notify.
"""


import tweepy
import time
import requests
import config


count = 0

# when product is availible, sends notifications
def notify():

    global count

    # connect to Twitter API
    auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_token, config.access_token_secret)
    api = tweepy.API(auth)


    # sends notification via Twitter and IFTTT
    try:
        api.update_status(config.message)
        ifttt_webhook_url = 'https://maker.ifttt.com/trigger/notify/with/key/' + str(config.iftttKey)
        requests.post(ifttt_webhook_url)
        time.sleep(43200)

    # adds a new number before post to avoid duplicate post error
    except tweepy.error.TweepError:
        count +=1
        api.update_status(str(count) + ' ' + config.message)
        ifttt_webhook_url = 'https://maker.ifttt.com/trigger/notify/with/key/' + str(config.iftttKey)
        requests.post(ifttt_webhook_url)
        time.sleep(43200)

    except requests.exceptions.ConnectionError:
    	pass

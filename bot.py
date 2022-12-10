# Create a twitter bot that tweets when I got live on twitch

import tweepy
import keys
import time
import requests

announced = False

def api():
    auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret)
    auth.set_access_token(keys.access_token, keys.access_secret)

    return tweepy.API(auth)

def tweet(api: tweepy.API, message: str, image_path=None):
    if image_path is None:
        api.update_status(message)
    else:
        api.update_with_media(image_path, message)

# Create a function that requests decapi.me/twitch/uptime
def isOnline():
    # If the uptime is 0, return False
    # If the uptime is not 0, return True
    request = requests.get('https://decapi.me/twitch/uptime?channel=DanFrmSpace')
    if request.text == 'DanFrmSpace is offline':
        return False
    else:
        return True

if __name__ == '__main__':
    api = api()
    # Check if the bot was able to authenticate
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")

    # Make a loop that checks if I'm live on twitch every 5 minutes
    while True:
        
        if isOnline() and not announced:
            tweet(api, "I am currently live streaming on twitch!\nhttps://twitch.tv/DanFrmSpace")
            print("I'm live on twitch")
            announced = True
        elif not isOnline():
            announced = False
            print("I'm not live on twitch")

        time.sleep(5 * 60)


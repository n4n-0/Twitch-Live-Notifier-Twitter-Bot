import tweepy
import keys
import time
import requests
import platform
import urllib.request
import os

announced = False
buffer = 5 * 60 # 5 minutes

request_token_url = f"https://id.twitch.tv/oauth2/token?client_id={keys.twitch_api_key}&client_secret={keys.twitch_api_secret}&grant_type=client_credentials"
reponse = requests.post(request_token_url)
print(reponse)
token = reponse.json()['access_token']
header = {'Client-ID': keys.twitch_api_key, "Authorization": f'Bearer {token}'}

cls = "cls" if platform.system() == "Windows" else "clear"

def api():
    auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret)
    auth.set_access_token(keys.access_token, keys.access_secret)

    return tweepy.API(auth)

def tweet(api: tweepy.API, message: str, image_path=None):
    if image_path is None:
        api.update_status(message)
    else:
        api.update_status_with_media(message, image_path)

def getThumbnail(url):
    folder_path = "./thumbnail/"
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    file_name = 'thumbnail.jpg'

    #if thumbnail already exists, delete it
    if os.path.exists(os.path.join(folder_path, file_name)):
        os.remove(os.path.join(folder_path, file_name))


    local_file = os.path.join(folder_path, file_name)
    urllib.request.urlretrieve(url, local_file)



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
        os.system(cls)
        print("Checking if I'm live on twitch...")
        response = requests.get('https://api.twitch.tv/helix/streams?user_login=DanFrmSpace', headers=header)
        if response.status_code == 200:
            data = response.json()["data"]
            if data:
                broadcaster = data[0]
                broadcaster_id = broadcaster["id"]
                broadcaster_name = broadcaster["user_name"]
                broadcaster_game = broadcaster["game_name"]
                stream_title = broadcaster["title"]
                stream_viewer_count = broadcaster["viewer_count"]
                stream_thumbnail = broadcaster["thumbnail_url"].format(width=1920, height=1080)

                getThumbnail(stream_thumbnail)

                if not announced:
                    tweet(api, f"This is a test for my twitch live notifier\nI am currently live streaming {broadcaster_game} on twitch!\nhttps://twitch.tv/DanFrmSpace", "./thumbnail/thumbnail.jpg")
                    print("Tweeted that I'm live on twitch!")
                    announced = True
                    time.sleep(buffer)
                else:
                    time.sleep(buffer)
            else:
                if announced:
                    tweet(api, "Thanks to everyone who watched my stream!\nI'm no longer live on twitch!\nFollow me at https://twitch.tv/DanFrmSpace so you don't miss the next one <3")
                    print("Tweeted that I'm no longer live on twitch!")
                    announced = False
                    time.sleep(buffer)
                else:
                    print("I'm not live on twitch right now")
                    announced = False
                    time.sleep(buffer)
        else:
            print('Error: ' + str(response.status_code) + ' ' + response.text)
            


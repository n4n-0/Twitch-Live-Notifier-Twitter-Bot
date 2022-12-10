
# Twitch live Notification Twitter Bot

This twitter bot posts a tweet everytime you go live with a screen grab of your stream.
Also includes a message for when you stop streaming to thank eveyone for watching


## Deployment

- You will need to create a twitter and twitch developer accounts
- Then create applications on both as well.
- In the twitter application you will need to apply for elevated status
- make a file called keys.py and insert all your keys

```python
    client_id = ''
    client_secret = ''
    api_key = ''
    api_secret = ''
    access_token = ''
    access_secret = ''
    bearer_token = ''
    twitch_api_key = ''
    twitch_api_secret = ''
```
- Change the username on line 12 of bot.py
- Run the bot using
```bash
python bot.py
```
## Feedback

If you have any feedback, please join the Discord https://discord.gg/zgedTwcTy5


## Screenshots

![App Screenshot](https://i.imgur.com/mWljsAi.png)
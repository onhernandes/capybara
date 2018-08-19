from twitter import *
import requests
import os
import config

config.ensure()

TT_CONSUMER = config.get("TWITTER_CAPYBARA_CONSUMER_KEY")
TT_SECRET = config.get("TWITTER_CAPYBARA_SECRET")

MY_TWITTER_CREDS = os.path.expanduser('.capybara-credentials')

if not os.path.exists(MY_TWITTER_CREDS):
    oauth_dance("Capybara", TT_CONSUMER, TT_SECRET, MY_TWITTER_CREDS)

oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)
auth = OAuth(oauth_token, oauth_secret, TT_CONSUMER, TT_SECRET)

tt = Twitter(auth=auth)

def tweet(img_url):
    img_read = requests.get(img_url).content
    t_upload = Twitter(domain="upload.twitter.com", auth=auth)
    img_id = t_upload.media.upload(media=img_read)["media_id_string"]
    return tt.statuses.update(status="", media_ids=img_id)


import yaml
import sys
import os

current_dir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(current_dir, "config.yaml"), "r") as conf:
    y = yaml.load(conf)

def get(k):
    return os.environ.get(k, y.get(k))

def ensure():
    values = map(lambda k: get(k), list(y.keys()))

    if not all(list(values)):
        print(
            """
            You must set the right env varibles.

            - Set $FLICKR_CAPYBARA_KEY for Flickr API
            - Set $TWITTER_CAPYBARA_CONSUMER_KEY for Twitter API
            - Set $TWITTER_CAPYBARA_SECRET for Twitter API
            """
        )
        sys.exit()


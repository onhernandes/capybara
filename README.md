# capybara
Post capybara photos on Twitter

## Running locally
- `git clone git@github.com:onhernandes/capybara.git`
- `cd capybara`
- `mkdir env && virtualenv --python=$(which python3) env`
- `source env/bin/activate`
- `pip install -r requirements.txt`
- Configure your credentials, exporting the following keys:
  - Flickr API Key: [https://www.flickr.com/services/apps/create/](https://www.flickr.com/services/apps/create/)
  - Twitter's Consumer & Private key: [https://developer.twitter.com/en/apps](https://developer.twitter.com/en/apps)
  - Export them as `$FLICKR_CAPYBARA_KEY`, `$TWITTER_CAPYBARA_CONSUMER_KEY` and `$TWITTER_CAPYBARA_SECRET`
- Run run run `python main.py`

If your photo was posted and you want to remove, please do not mark as spam, just send me a DM and I'll remove as soon as possible

[My Twitter](https://twitter.com/onhernandes)
[The bot's account](https://twitter.com/)

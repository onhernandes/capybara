from urllib import request, parse
from photo import Photo
from tt import tweet
import mongoengine
import sys
import os
import json

FLICKR_KEY = os.environ.get("FLICKR_CAPYBARA_KEY", False)
TT_CONSUMER = os.environ.get("TWITTER_CAPYBARA_CONSUMER_KEY", False)
TT_SECRET = os.environ.get("TWITTER_CAPYBARA_SECRET", False)

if not FLICKR_KEY or not TT_CONSUMER or not TT_SECRET:
    print("You must set the right env varibles")
    print("Set $FLICKR_CAPYBARA_KEY for Flickr API")
    print("Set $TWITTER_CAPYBARA_CONSUMER_KEY for Twitter API")
    print("Set $TWITTER_CAPYBARA_SECRET for Twitter API")
    sys.exit()

mongoengine.connect('capybara')

def get_flickr_photos(page = 1):
    r = request.urlopen("https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=%s&tags=capybara&format=json&nojsoncallback=1&page=%s" % (FLICKR_KEY, page))
    return json.loads(r.read())

def make_photo_url(farm, server, id, secret):
    return "http://farm%s.staticflickr.com/%s/%s_%s.jpg" % (farm, server, id, secret)

def main():
    """Does the job"""
    keep = True
    photos = get_flickr_photos()
    photos = photos["photos"]["photo"]
    photos = iter(photos)
    page = 1
    t = False

    while keep is True:
        p = next(photos, False)

        if p is False:
            photos = get_flickr_photos(page + 1)
            photos = photos["photos"]["photo"]
            photos = iter(photos)
            continue

        trial = Photo.objects(flickr=p["id"]).first()
        print("Trying to find %s in collection" % (p["id"]))

        if trial is not None:
            print("Photo already published, looping again")
            print("Found ID: %s\n" % (p["id"]))
            continue

        print("Found a valid photo, posting")
        keep = False
        url = make_photo_url(p["farm"], p["server"], p["id"], p["secret"])
        t = tweet(url)
        Photo(flickr=p["id"], tweet=t["id_str"]).save()

    return t

if __name__ == "__main__":
    print(main())


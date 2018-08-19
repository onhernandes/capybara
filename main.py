from photo import Photo
from tt import tweet
import mongoengine
import requests
import config

config.ensure()

mongoengine.connect('capybara')

def get_flickr_photos(page = 1):
    r = requests.get("https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=%s&tags=capybara&format=json&nojsoncallback=1&page=%s" % (config.get("FLICKR_CAPYBARA_KEY"), page))
    return r.json()

def make_photo_url(farm, server, id, secret):
    return "http://farm%s.staticflickr.com/%s/%s_%s.jpg" % (farm, server, id, secret)

def request_photos(page = 1):
    photos = get_flickr_photos(page)
    photos = photos["photos"]["photo"]
    photos = iter(photos)

    return photos

def main():
    """Does the job"""
    keep = True
    photos = request_photos()
    page = 1
    t = False

    while keep is True:
        p = next(photos, False)

        if p is False:
            photos = request_photos(page + 1)
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

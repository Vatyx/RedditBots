from instagram.client import InstagramAPI
import urllib
import urllib.request
import pprint
pp = pprint.PrettyPrinter(indent=4)
import json

response = urllib.request.urlopen('http://instagram.com/publicapi/oembed/?url=https://instagram.com/p/9rQSudHCL6/');
str_response = response.read().decode('utf-8')
obj = json.loads(str_response)
#pp.pprint(obj)

media_id = obj['media_id']
print(media_id)

api = InstagramAPI(client_id='ad894ecb14cb4928bd00f5e4d8c2ae67', client_secret='b5deae6b21be45259ccdd272998a2651')
media_object = api.media(media_id)
img = media_object.get_standard_resolution_url()


#popular_media = api.media_popular(count=20)
# f = open("links", 'w')
# for media in popular_media:
# 	f.write(media.images['standard_resolution'].url + "\n")
# 	urllib.urlretrieve("http://www.digimouth.com/news/media/2011/09/google-logo.jpg", "local-filename.jpg")
    # print(media.images['standard_resolution'].url)
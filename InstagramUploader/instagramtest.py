from instagram.client import InstagramAPI

api = InstagramAPI(client_id='ad894ecb14cb4928bd00f5e4d8c2ae67', client_secret='b5deae6b21be45259ccdd272998a2651')
popular_media = api.media_popular(count=20)
f = open("links", 'w')
for media in popular_media:
	f.write(media.images['standard_resolution'].url + "\n")
    # print(media.images['standard_resolution'].url)
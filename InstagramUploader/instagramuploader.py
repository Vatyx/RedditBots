import time
import praw
import OAuth2Util


r = praw.Reddit('Instagram to Imgur uploader by Vatyx')
o = OAuth2Util.OAuth2Util(r)

o.refresh()

def searchSubmissions():
	submissions = r.get_subreddit('all').get_new(limit=50)#(r, r.get_subreddit('dota2'), 10)
	for submission in submissions:
		print(submission.title)

while True:
	try:
		searchSubmissions()
		time.sleep(2)
	except:
		print("wow")

# while True:
#     o.refresh()
#     print(r.get_me().comment_karma)
#     time.sleep(3600)

# r.set_oauth_app_info(client_id='sH8ArC6fMygIbg',
#                       client_secret='RHhh15rjKXHdnmdtH0RV1TsrDow',
#                       redirect_uri='http://127.0.0.1:65010/'
#                                    'authorize_callback')

# user = r.get_redditor('InstagramtoImgur-bot')

# already_done = []

# while True:
# 	comments = alex.get_comments()
# 	curr = next(comments)
# 	if not curr.id in already_done:
# 		already_done.append(curr.id)
# 		print(curr)
# 		textComment(curr)
# 	print(curr.id)
# 	time.sleep(10)
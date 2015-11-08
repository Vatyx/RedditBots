import time
import praw
import OAuth2Util
import datetime


r = praw.Reddit('Instagram to Imgur uploader by Vatyx')
o = OAuth2Util.OAuth2Util(r)

o.refresh()

alreadyChecked = []

def searchSubmissions():
	submissions = r.get_subreddit('all').get_new(limit=5)
	for submission in submissions:
		if not submission.id in alreadyChecked:
			print(submission.title)
			alreadyChecked.append(submission.id)

submissions = r.get_subreddit('all').get_new(limit=None)
for submission in submissions:
	if not submission.id in alreadyChecked and submission.domain == 'instagram.com':
		print(submission.url)
		alreadyChecked.append(submission.id)
print("Done first!")
# time.sleep(30)
# submissions = r.get_subreddit('all').get_new(limit=150)
# for submission in submissions:
# 	if not submission.id in alreadyChecked:
# 		print(submission.domain)
# 		alreadyChecked.append(submission.id)
print("Done second!")

# f = open('outfile.txt', 'w')
# submissions = praw.helpers.submission_stream(r, "all", limit=10)
# for sub in submissions:
# 	#print(str(datetime.datetime.fromtimestamp(sub.created_utc)))
# 	print((sub.title).encode('ascii','ignore'))
# 	f.write(str((sub.title).encode('ascii','ignore')))
# 	f.write('\n')


# submissions = r.get_subreddit('all').get_new(limit=5)
# for submission in submissions:
# 	print(submission.title)

# while True:
# 	try:
# 		searchSubmissions()
# 		time.sleep(10)
# 		print("here!")
# 	except:
# 		print("ERROR wow")
# 		time.sleep(2)

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
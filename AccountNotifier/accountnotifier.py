from twilio.rest import TwilioRestClient
import time
import praw
import datetime

account_sid = "AC04ae25977f10fe51e9d811bf0bf2a07f"
auth_token  = "d820c97f96b72dfb49464b79b4158779"
client = TwilioRestClient(account_sid, auth_token)

r = praw.Reddit('VRCkid made this to do something on reddit. Lets see if it works')
alex = r.get_redditor('8kneekirk8')

already_done = []

def textComment(comment):
	body = comment.body
	subreddit = str(comment.subreddit)
	time = str(datetime.datetime.fromtimestamp(comment.created_utc))
	message = client.messages.create(body="Comment created at " + time + "\nSubreddit: " + subreddit, to="+12144035793", from_="+19723625257")
	message = client.messages.create(body=body, to="+12144035793", from_="+19723625257")

while True:
	comments = alex.get_comments()
	curr = comments.__next__()
	if not curr.id in already_done:
		already_done.append(curr.id)
		print(curr)
		textComment(curr)
	print(curr.id)
	time.sleep(10)
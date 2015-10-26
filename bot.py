import time
import praw

r = praw.Reddit('VRCkid made this to do something on reddit. Lets see if it works')

while True:
	subreddit = r.get_subreddit('all')
	comments = subreddit.get_comments(limit=1)
	for thing in comments:
		print(thing.body)
	time.sleep(1)
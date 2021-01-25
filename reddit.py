import praw

reddit = praw.Reddit('bot1')

user = reddit.user.me()

upvoted = user.upvoted(limit=10)

for up in upvoted:
    print(up.title)

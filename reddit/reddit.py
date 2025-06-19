import os
import dotenv
import json

import praw

# load info from .env file
dotenv.load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

# subreddit = reddit.subreddit("python")

# for post in subreddit.hot(limit=2):
#     print(post.title, post.score, post.url)

# get the full thread
URL = "https://www.reddit.com/r/Westchester/comments/1kl6uh1/congestion_pricing_is_working_in_nyc/"
submission = reddit.submission(url=URL)

# get all content by id
# submission = reddit.submission(id="abc123")

# unlimit the number of comments
# submission.comments.replace_more(limit=None)

# get all comments
for comment in submission.comments:
    print(comment.body)

# get all comments in a list
comments = submission.comments.list()

# store all comments in a file
with open("data/reddit_comments.txt", "w") as f:
    for comment in comments:
        f.write(comment.body + "\n")


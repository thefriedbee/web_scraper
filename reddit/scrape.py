import praw
import json


reddit = praw.Reddit(
    client_id="EMDfMv0me-4ANHREQd1njQ",
    client_secret="-KCg48wuMMUsl294n87YBoFU7-ReyA",
    user_agent="my user agent"
)

# subreddit = reddit.subreddit("python")

# for post in subreddit.hot(limit=2):
#     print(post.title, post.score, post.url)

# get the full thread 
submission = reddit.submission(url="https://www.reddit.com/r/Westchester/comments/1kl6uh1/congestion_pricing_is_working_in_nyc/")

# print(type(submission))
# print(submission)

# json_data = json.loads(submission)
# with open('data.json', 'w') as file:
#     json.dump(json_data, file)


# get all content by id
# submission = reddit.submission(id="abc123")

# unlimite the number of comments
# submission.comments.replace_more(limit=None)

# get all comments
for comment in submission.comments:
    print(comment.body)

# get all comments in a list
comments = submission.comments.list()

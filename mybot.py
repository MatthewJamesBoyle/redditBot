import praw
import re


bot = praw.Reddit(user_agent='mattTest v0.1',
                  client_id='',
                  client_secret='',
                  username='',
                  password='')
subreddit = bot.subreddit('worldnews')
comments = subreddit.stream.comments();
pattern = re.compile("^matt$")
for comment in comments:
    text = comment.body  # Fetch body
    author = comment.author  # Fetch author
    textLower = text.lower()
    for word in textLower.split():
        if pattern.match(word):
            print(text)  # Send message

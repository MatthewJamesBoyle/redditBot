import praw
import re


class redditBot(object):

  def __init__(self):
    self.bot = praw.Reddit(user_agent='mattTest v0.1',
                           client_id='UewGNqfLQjLp7A',
                           client_secret='JU_k-bB-1__6fOFBF9F5HHXJVDs',
                           username='matt182',
                           password='KB!35c^E&rHd^4g#n&dG')

  def crawlSub(self, sub, pattern):
    subreddit = self.bot.subreddit(sub)
    comments = subreddit.stream.comments()
    pattern = re.compile(pattern)
    for comment in comments:
      text = comment.body  # Fetch body
      author = comment.author  # Fetch author
      textLower = text.lower()
      for word in textLower.split():
        if pattern.match(word):
          print(text)  # Send message


def main():
  letsGo = redditBot()
  letsGo.crawlSub("worldnews", "^Immelt$")



if __name__ == "__main__":
    main()

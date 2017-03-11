import praw
import re


class redditBot(object):

  def __init__(self):
    self.bot = praw.Reddit()

  def crawlSub(self, sub, pattern,postWhenFound,*commentBody):
    data={}
    subreddit = self.bot.subreddit(sub)
    comments = subreddit.stream.comments()
    pattern = re.compile(pattern)
    for comment in comments:
      text = comment.body  # Fetch body
      author = comment.author  # Fetch author
      textLower = text.lower()
      for word in textLower.split():
        if pattern.match(word):
            data['author']=author.name
            data['comment']=text
            data['sub']=subreddit.display_name
            print(data)
            if postWhenFound:
                print("commenting..")
                comment.reply(commentBody)




def main():
  bot = redditBot()
  # bot.crawlSub("worldnews", "blink-182",True,"I appericiate that you spelt it blink-182 and not blink 182")
    bot.crawlSub("worldnews", "blink-182",False)




if __name__ == "__main__":
    main()

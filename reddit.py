import praw
import random

with open('praw_settings', 'r') as settings_file:
    reddit = praw.Reddit(client_id=settings_file.readline().replace("\n", ""),
                         client_secret=settings_file.readline().replace("\n", ""),
                         password=settings_file.readline().replace("\n", ""),
                         user_agent="test",
                         username=settings_file.readline().replace("\n", ""))

thoughts = []
for current in reddit.subreddit('ShowerThoughts').top('week'):
    thoughts.append(current.title)

def getThought():
    print len(thoughts)
    thought = thoughts[int(random.random() * 100)]
    print thought
    return thought

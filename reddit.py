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


gifs = []

for gif in reddit.subreddit('gifs').top('week'):
    gifs.append(gif.url)

tils = []

for til in reddit.subreddit('TodayILearned').top('week'):
    tils.append(til.title[4:])


def getThought():
    thought = thoughts[int(random.random() * 100)]
    print thought
    return thought


def getGif():
    cur_gif = gifs[int(random.random() * 100)]
    if cur_gif[-1] == 'v':
        print cur_gif
        return cur_gif[:-1]

    if cur_gif[-3:] != 'gif':
        print cur_gif + " Recursive"
        return getGif()

def getTIL():
    cur_til = tils[int(random.random() * 100)]
    print cur_til
    return cur_til

#def getSize(url): TODO implement getSize() so phone client will work properly

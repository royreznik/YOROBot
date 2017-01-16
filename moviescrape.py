# import requests
import urllib2
import re
# import HTMLParser


def getMovies():
#   hebrew = HTMLParser.HTMLParser()
    tmp_movies = []
    re_movie = re.compile(r"DarkGreenStrong16.*?>(.+?)</a>")
    page = urllib2.urlopen("http://www.seret.co.il/movies/s_theatres.asp?TID=112")
    for line in page.readlines():
        movie = re_movie.findall(line)
        if movie:
            tmp_movies.append(movie)

    for index, f_movie in enumerate(tmp_movies[0]):
        tmp_movies[0][index] = f_movie.decode("cp1255").encode("utf-8")

    movies = tmp_movies[0]

    return movies

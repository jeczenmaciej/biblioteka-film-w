import random
from datetime import datetime

class Video:
    def __init__(self, title, release_year, genre, plays=0):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.plays = plays

    def play(self):
        self.plays += 1

class Movie(Video):
    def __str__(self):
        return f"{self.title} ({self.release_year})"

class Series(Video):
    def __init__(self, title, release_year, genre, episode, season, plays=0):
        super().__init__(title, release_year, genre, plays)
        self.episode = episode
        self.season = season

    def __str__(self):
        return f"{self.title} S{str(self.season).zfill(2)}E{str(self.episode).zfill(2)}"

def get_movies(video_list):
    return sorted([video for video in video_list if isinstance(video, Movie)], key=lambda x: x.title)

def get_series(video_list):
    return sorted([video for video in video_list if isinstance(video, Series)], key=lambda x: x.title)

def search(video_list, title):
    for video in video_list:
        if video.title == title:
            return video
    return None

def generate_views(video_list):
    video = random.choice(video_list)
    video.plays += random.randint(1, 100)

def generate_views_x_times(video_list, x):
    for _ in range(x):
        generate_views(video_list)

def top_titles(video_list, quantity, content_type=None):
    if content_type == "movies":
        video_list = get_movies(video_list)
    elif content_type == "series":
        video_list = get_series(video_list)
    video_list.sort(key=lambda x: x.plays, reverse=True)
    return video_list[:quantity]

print ("BIBLIOTEKA FILMÓW")
print()
video_list = [
    Movie("Pulp Fiction", 1994, "Crime"),
    Movie("The Shawshank Redemption", 1994, "Drama"),
    Movie("The Godfather", 1972, "Crime"),
    Series("The Simpsons", 1989, "Animation", 5, 1),
    Series("Breaking Bad", 2008, "Crime", 1, 1),
    Series("Game of Thrones", 2011, "Drama", 1, 1)
]
generate_views_x_times(video_list, 10)
print("Najpopularniejsze filmy i seriale dnia", datetime.now().strftime("%d.%m.%Y"))

print("\nTop 3 Filmy:")
for video in top_titles(video_list, 3, "movies"):
    print(video)

print("\nTop 3 Seriale:")
for video in top_titles(video_list, 3, "series"):
    print(video)

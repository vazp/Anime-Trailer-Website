from video import Video

class Anime(Video):
    """ This class provides a way to store information related to an anime. It inherits from the class video """

    def __init__(self, anime_title, anime_poster, anime_trailer, anime_year, anime_episodes):
        Video.__init__(self, anime_title, anime_poster, anime_trailer, anime_year)
        self.episodes = anime_episodes
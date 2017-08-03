import webbrowser


class Video():
    """ This class provides a way to store information related to a video """

    def __init__(self, video_title, video_poster, video_youtube_trailer,
                 video_year):
        self.title = video_title
        self.poster_url = video_poster
        self.trailer_url = video_youtube_trailer
        self.year = video_year

    def show_trailer(self):
        webbrowser.open(self.trailer_url)

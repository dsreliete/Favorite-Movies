import webbrowser

class Movie():

    """This class defines a movie"""
    
    def __init__(self, movie_title, movie_story, movie_poster_image, movie_url):
        self.title = movie_title
        self.storyline = movie_story
        self.poster_image_url = movie_poster_image
        self.trailer_youtube_url = movie_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        

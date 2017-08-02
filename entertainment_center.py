from anime import Anime
import fresh_anime_tomatoes

# Six instances of the class Anime are created with their respective information
anime_1 = Anime("My Hero Academia", "https://images-na.ssl-images-amazon.com/images/I/91kjVOEopVL._SY450_.jpg",
                "https://www.youtube.com/watch?v=wIb3nnOeves", "2016 - Present", "30")
anime_2 = Anime("Fullmetal Alchemist", "https://vignette2.wikia.nocookie.net/fma/images/e/e9/Fmab-poster.png/revision/latest?cb=20131124145205",
                "https://www.youtube.com/watch?v=BOm_PAI2goo", "2009 - 2010", "64")
anime_3 = Anime("One-Punch Man", "http://i0.kym-cdn.com/photos/images/original/001/029/377/37d.jpg",
                "https://www.youtube.com/watch?v=2JAElThbKrI", "2015", "12")
anime_4 = Anime("Haikyuu!!", "https://vignette3.wikia.nocookie.net/haikyuu/images/c/c1/4th_Key_Visual.png/revision/latest?cb=20140326213607",
                "https://www.youtube.com/watch?v=DoNqztkdA_M", "2014 - Current", "61")
anime_5 = Anime("Death Note", "https://myanimelist.cdn-dena.com/images/anime/9/9453.jpg",
                "https://www.youtube.com/watch?v=tJZtOrm-WPk", "2006 - 2007", "37")
anime_6 = Anime("Shokugeki no Soma", "http://cdn.jkanime.net/assets/images/animes/image/shokugeki-no-souma.jpg",
                "https://www.youtube.com/watch?v=NBWwdXZyPEU", "2015 - Current", "37")

# The six instances are put in a list and passed as an argument to a function that displays them on a web page
series = [anime_1, anime_2, anime_3, anime_4, anime_5, anime_6]
fresh_anime_tomatoes.open_video_page(series)
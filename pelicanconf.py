AUTHOR = 'haiming, maofeng, yue, wenxiang'
SITENAME = 'Haiming Group'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Theme settings
THEME = "themes/notmyidea"

# Category settings
CATEGORIES = [
    'Haiming\'s Column',
    'Maofeng\'s Column',
    'Yue\'s Column',
    'Wenxiang\'s Column',
    'Group Project'
]

# Author settings
AUTHORS = {
    'haiming': {
        'name': 'Haiming',
        'bio': 'Author Bio',
        'image': 'images/authors/haiming.jpg'
    },
    'maofeng': {
        'name': 'Maofeng',
        'bio': 'Author Bio',
        'image': 'images/authors/maofeng.jpg'
    },
    'yue': {
        'name': 'Yue',
        'bio': 'Author Bio',
        'image': 'images/authors/yue.jpg'
    },
    'wenxiang': {
        'name': 'Wenxiang',
        'bio': 'Author Bio',
        'image': 'images/authors/wenxiang.jpg'
    }
}

# Page settings
PAGES_MENU = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

# Make welcome page the index
INDEX_SAVE_AS = 'index.html'
INDEX_URL = '' # Setting to empty means it's the root

# Pagination settings
DEFAULT_PAGINATION = 10

# Static files
STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

# Plugin settings
PLUGINS = []

# Other settings
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

# Blogroll
LINKS = (
    ("GitHub", "https://github.com/haiminggroup/haiminggroup.github.io"),
)

# Social widget
SOCIAL = (
    ("Made by Maofeng", "#"),
)

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
SUMMARY_MAX_LENGTH = 200

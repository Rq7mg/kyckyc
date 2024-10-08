import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", 23144161))
API_HASH = getenv("API_HASH", "0e156557bde6def9a8541cc8c65d57df")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "6723540039:AAG9mUkRIk9ZYc0Z5STQUCPbKMnk95g0hAk")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://acha:acha@cluster0.pjq3j.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 960))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400")
)
# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1002125936547))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 6563936773))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "gnclkyc")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "HRKU-0580452f-5f10-4047-bf46-86e77e1c5027")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Rq7mg/kyckyc",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/kiyicitayfaa")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/kycmuzik")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", None)

# Time after which you're assistant account will leave chats automatically.

AUTO_LEAVE_ASSISTANT_TIME = int(

    getenv("ASSISTANT_LEAVE_TIME", "3400")

)  # Remember to give value in Seconds

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 314572800))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 3221225472))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BAFhJuEAxqUOjCk6ftkmBLmZrB5DVuFeM9-luSgXaZgbDqzkNqcIUWgZxy3qPmUg8E23iXqrI1LYWoeHljDzzpk9xGBhxsUhM6zmYaeHtKRkTfd63i2pmi8Sjdr6ER_71ynt-3EurNmG1rxLeWNRvyzicBtZJDnwXeetCMkX-1lo8MnXA8zF12yzW8intP98hOVXk_hTt7O-jWuk1-OndxoPUWZ-mWsxW3SvUI27fyT5V0zD965Musd1fg93KNUoKHn4El7XMvrVY8zIQdXeSyHuKaimRGHzYWYXtDKwpvXzA2F86F_YGP5gvkhMFPnYeYNtgGLgeDGTcm3Lh8h2s0oypHs5NgAAAAGcKU3CAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/5a2de8accfd9e7a46cfe5.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/5a2de8accfd9e7a46cfe5.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/321decfc24b08c837626c.jpg"
STATS_IMG_URL = "https://telegra.ph/file/321decfc24b08c837626c.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/321decfc24b08c837626c.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/321decfc24b08c837626c.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/321decfc24b08c837626c.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/321decfc24b08c837626c.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/321decfc24b08c837626c.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/321decfc24b08c837626c.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/321decfc24b08c837626c.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/321decfc24b08c837626c.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))



if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )

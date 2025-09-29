import tweepy
import datetime
import os
import random
from zoneinfo import ZoneInfo

try:
    API_KEY = os.environ["TWITTER_API_KEY"]
    API_SECRET_KEY = os.environ["TWITTER_API_SECRET_KEY"]
    ACCESS_TOKEN = os.environ["TWITTER_ACCESS_TOKEN"]
    ACCESS_TOKEN_SECRET = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]
except KeyError:
    print("Error: Twitter API credentials not found in environment variables.")
    exit()

auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api_v1 = tweepy.API(auth)
client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# --- Countdown Configuration ---
release_date = datetime.date(2025, 11, 1)
countdown_start_date = datetime.date(2025, 9, 29)
today = datetime.datetime.now(tz=ZoneInfo("Asia/Kolkata")).date()


# --- Main Script Logic ---
if today < countdown_start_date:
    print(f"Countdown has not started. It begins on {countdown_start_date}.")
    exit()

days_left = (release_date - today).days

# --- Tweet Composition Logic ---

if days_left > 1: # General countdown for all other days
    tweet_text = f"{days_left} "
elif days_left == 1:
    tweet_text = "ONE DAY TO GO FOR SSMB29 MONTH"
elif days_left == 0:
    tweet_text = "GLOBETROTTER MONTH IT IS"
else:
    tweet_text = "Stay tuned for the latest on #SSMB29 following the recent update! News could drop anytime.\n\n#MaheshBabu #SSRajamouli" 

# --- Post the Tweet (Text Only) ---
try:
    print("Posting a text-only tweet...")
    response = client.create_tweet(text=tweet_text)
    print(f"Tweet sent successfully! Tweet ID: {response.data['id']}")
except Exception as e:
    print(f"An error occurred: {e}")

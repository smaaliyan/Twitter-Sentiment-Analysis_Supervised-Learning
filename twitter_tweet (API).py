import tweepy
import os 
from dotenv import load_dotenv

# Set your API credentials
load_dotenv()
consumer_key = os.env['CONSUMER_KEY']
consumer_secret = os.env['CONSUMER_SECRET']
access_token = os.env['ACCESS_TOKEN']
access_token_secret = os.env['ACCESS_TOKEN_SECRET']

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Get user tweets
def get_user_tweets(username, count):
    try:
        tweets = api.user_timeline(screen_name=username, count=count)
        return tweets
    except tweepy.TweepError as e:
        print(f"Error retrieving tweets: {str(e)}")
        return []

# Example usage
username = 'TwitterUsername'  # Replace with the desired Twitter username
count = 10  # Number of tweets to retrieve

tweets = get_user_tweets(username, count)
for tweet in tweets:
    print(tweet.text)
    print('---')

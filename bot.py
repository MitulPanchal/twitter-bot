import tweepy
import tokens

auth = tweepy.OAuth1UserHandler(
   tokens.consumer_key_value, tokens.consumer_secret_value,
   tokens.access_token_value, tokens.access_secrets_value
)

api = tweepy.API(auth)
tweets = api.mentions_timeline()

for tweet in tweets:
    if '#testtwitterapi' in tweet.text.lower():
        print(str(tweet.id) + '-'+tweet.text)
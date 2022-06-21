import tweepy
import tokens
import time 

auth = tweepy.OAuth1UserHandler(
   tokens.consumer_key_value, tokens.consumer_secret_value,
   tokens.access_token_value, tokens.access_secrets_value
)


api = tweepy.API(auth)

hashtag = "FCBarcelona"
tweetNumber = 5
tweets = tweepy.Cursor(api.search_tweets, hashtag).items(tweetNumber)

def searchbot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet Done!")
            time.sleep(60)
        except tweepy.TweepError as e:
            print(e.reason)

searchbot()
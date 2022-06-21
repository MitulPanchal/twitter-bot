import tweepy
import tokens

auth = tweepy.OAuth1UserHandler(
   tokens.consumer_key_value, tokens.consumer_secret_value,
   tokens.access_token_value, tokens.access_secrets_value
)


api = tweepy.API(auth)

FILE_NAME = 'last_seen.txt'

def read_last_seen(FILE_NAME):
    with open(FILE_NAME, 'r') as file_read:
        last_seen_id = int(file_read.read().strip())
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    with open(FILE_NAME, 'w') as file_write:
        file_write.write(str(last_seen_id))
    return 

tweets = api.mentions_timeline(since_id = read_last_seen(FILE_NAME), tweet_mode = 'extended')


for tweet in reversed(tweets):
    if '#testtwitterapi' in tweet.full_text.lower():
        print(str(tweet.id) + '-'+ tweet.full_text)
        store_last_seen(FILE_NAME, tweet.id)
        api.update_status(status = "@" + tweet.user.screen_name + " Message received! #iamcodernow", in_reply_to_status_id = tweet.id)
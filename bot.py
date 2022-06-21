import tweepy
import tokens
import time 

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



def reply():
    tweets = api.mentions_timeline(since_id = read_last_seen(FILE_NAME), tweet_mode = 'extended')
    for tweet in reversed(tweets):
        if '#testtwitterapi' in tweet.full_text.lower():
            print("Replied to ID - " + str(tweet.id))

            # Reply, retweet and like tweet 
            api.update_status(status = "@" + tweet.user.screen_name + " Message received! #iamcodernow", in_reply_to_status_id = tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)

            # Update Last tweet ID bot reply to in file 
            store_last_seen(FILE_NAME, tweet.id)

while True:
    reply()
    time.sleep(15)        
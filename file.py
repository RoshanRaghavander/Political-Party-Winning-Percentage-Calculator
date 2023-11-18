import tweepy
from collections import Counter

# Twitter API credentials
consumer_key = '-----------'
consumer_secret = '----------'
access_token = '----------'
access_token_secret = '------'

# Set up the Tweepy API object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Define a list of political parties and their corresponding hashtags
parties = {'Conservative': '#Tory, #ConservativeParty', 'Labour': '#Labour, #LabourParty', 'Liberal Democrat': '#LibDem, #LiberalDemocrats'}

# Define a counter to store the number of negative comments for each party
party_negatives = {}

# Iterate through the parties and fetch their tweets
for party, hashtags in parties.items():
    # Fetch the tweets containing the party's hashtags
    tweets = api.search_tweets(q=hashtags, lang='en')
    
    # Filter out retweets and non-English tweets
    tweets = [tweet for tweet in tweets if not tweet.retweeted and tweet.lang == 'en']
    
    # Count the number of negative comments for this party
    party_negatives[party] = len([tweet for tweet in tweets if negative_words(tweet.text)])

# Determine the winning party based on the highest number of negative comments
winning_party = max(party_negatives.items(), key=lambda x: x[1])[0]

print(f"The winning party is {winning_party} with {party_negatives[winning_party]} negative comments.")

def negative_words(text):
    """
    Returns True if the input text contains negative words, False otherwise.
    """
    negative_words = ['not', 'no', 'without', 'never', 'worst', 'bad', 'awful', 'hate']
    for word in negative_words:
        if word in text.lower():
            return True
    return False

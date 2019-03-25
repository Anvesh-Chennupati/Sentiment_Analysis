from emojiExtractor import extract_emojis
from twitterProcessor import TwitterClient
from graphs import genWordCloud,barPlotgraph
import importlib
import re
import warnings



warnings.filterwarnings("ignore", category=DeprecationWarning) 


print('Sentiment Analysis Considering Emoji\n\n')

#tweepy object to authenticate and fetch tweets
api = TwitterClient()

queryText = 'black'

print('Query Text->' +queryText)

#fetching tweets with and without emojis
regularTweets,EmojiTweets = api.get_tweets(query=queryText, count=100)

positveTweetsR = [tweet for tweet in regularTweets if tweet['sentiment'] == 'positive']
positveTweetsE = [tweet for tweet in EmojiTweets if tweet['sentiment'] == 'positive']
negativeTweetsR = [tweet for tweet in regularTweets if tweet['sentiment'] == 'negative']
negativeTweetsE = [tweet for tweet in EmojiTweets if tweet['sentiment'] == 'negative']


#creting the graphs
htl1 = []
nn1 = ""
for temp in positveTweetsE:
    normal_words= "".join(temp['text'])
    nn1 += normal_words
    htl1.append(normal_words)
# normal_words = ''.join([for tweet in positveTweetsE:tweet['text'])])
genWordCloud('Positive Words', nn1)
# negative_words = ''.join([text for text in negativeTweetsE['tweet']])

nn2 = ""
for temp in negativeTweetsE:
    normal_words= "".join(temp['text'])
    nn2 += normal_words
# normal_words = ''.join([for tweet in positveTweetsE:tweet['text'])])
genWordCloud('Negative', nn2)

#hastags

def hashtag_extract(x):
    hashtags = []
    # Loop over the words in the tweet
    for i in x:
        ht = re.findall(r"#(\w+)", i)
        hashtags.append(ht)

    return hashtags

# for temp in negativeTweetsE:
#     htl1.append("".join(temp['text']))

# HT_regular = hashtag_extract(htl1)

# extracting hashtags from racist/sexist tweets
# HT_negative = hashtag_extract(
#     combination['tidy_tweet'][combination['label'] == 1])

# unnesting list
# HT_regular = sum(HT_regular, [])
# # HT_negative = sum(HT_negative, [])

# print(HT_regular)

# barPlotgraph(HT_regular)
# barPlotgraph(HT_negative)
#printing the output

print('Sentiment Analysis with out Taking Emojis into Consideration')
print("Positive tweets percentage: {} %".format(100*len(positveTweetsR)/len(regularTweets)))
print("Negative tweets percentage: {} %".format(100*len(negativeTweetsR)/len(regularTweets)))
print("Neutral tweets percentage: {} %  ".format(100*len(regularTweets) /len(regularTweets) - 100*len(negativeTweetsR)/len(regularTweets) - 100*len(positveTweetsR)/len(regularTweets)))

print('\n\n\nSentiment Analysis with Taking Emojis into Consideration')
print("Positive tweets percentage: {} %".format(100*len(positveTweetsE)/len(EmojiTweets)))
print("Negative tweets percentage: {} %".format(100*len(negativeTweetsE)/len(EmojiTweets)))
print("Neutral tweets percentage: {} %  ".format(100*len(EmojiTweets) /len(EmojiTweets) - 100*len(negativeTweetsE)/len(EmojiTweets) - 100*len(positveTweetsE)/len(EmojiTweets)))

if ((100*len(positveTweetsR)/len(regularTweets)) == (100*len(positveTweetsE)/len(EmojiTweets))) and ((100*len(negativeTweetsR)/len(regularTweets)) == (100*len(negativeTweetsE)/len(EmojiTweets))):
    print('\n\n\nEmojis Not detected in Tweets')

# printing first 5 positive tweets
# print("\n\nPositive tweets:")
# for tweet in positveTweetsE[:10]:
#     print(tweet['text'])

# printing first 5 negative tweets
# print("\n\nNegative tweets:")
# for tweet in negativeTweetsE[:10]:
#     print(tweet['text'])
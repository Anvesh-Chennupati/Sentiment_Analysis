import matplotlib.pyplot as plt
import seaborn as sns
import string
import nltk
import pandas as pd
from wordcloud import WordCloud
import warnings


warnings.filterwarnings("ignore", category=DeprecationWarning)


def genWordCloud(graphName, words):
    wordcloud = WordCloud(width=800, height=500,random_state=21, max_font_size=110).generate(words)
    plt.figure(figsize=(10, 7))
    plt.title(graphName)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis('off')
    plt.show()

def barPlotgraph(hashTagsvalues):
    a = nltk.FreqDist(hashTagsvalues)
    d = pd.DataFrame({'Hashtag': list(a.keys()), 'Count': list(a.values())})
    # selecting top 10 most frequent hashtags
    d = d.nlargest(columns="Count", n=10)
    plt.figure(figsize=(16, 5))
    ax = sns.barplot(data=d, x="Hashtag", y="Count")
    ax.set(ylabel='Count')
    plt.show()
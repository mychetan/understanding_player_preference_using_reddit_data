#Imported Libraries
import pandas as pd 
import seaborn as sns 
from textblob import TextBlob
import matplotlib.pyplot as plt 

#Creates a new column called word_count, sum of words per post, and separate data into two dataframes
def word_count(df):
    df['word_count'] = df['text'].map(lambda x: len(x.split()))
    xbox = df.loc[df['subreddit'] == 0]
    ps = df.loc[df['subreddit'] == 1]
    return xbox, ps

#Creates a bar plots that examines distribution of two dataframes
def dist_word_count(df1, df2):
    plt.figure(figsize=(15,7))
    ax1 = plt.subplot(2,1,1)
    ax1.hist([df1['word_count'],  df2['word_count']],  range=[0,1000])
    ax1.set_title('Xbox vs PS Distribution of 1000 Words')
    ax1.legend(['Xbox', 'PS'])
    ax1.set_xlabel('word count')
    ax1.set_ylabel('frequency');

    ax2 = plt.subplot(2,1,2)
    ax2.hist([df1['word_count'],  df2['word_count']],  range=[0,500])
    ax2.set_title('Xbox vs PS Distribution of 500 Words')
    ax2.legend(['Xbox', 'PS'])
    ax2.set_xlabel('word count')
    ax2.set_ylabel('frequency')

    plt.tight_layout();
    
#Creates a box plot for word count
def box_word_count(df1, df2):
    plt.figure(figsize=(15,5))
    plt.subplot(2,1,1)
    sns.boxplot(df1['word_count'])
    plt.title('Xbox One Word Count');

    plt.subplot(2,1,2)
    sns.boxplot(df2['word_count'], color='orange')
    plt.title('PS4 Word Count')
    plt.tight_layout();
    
#Separates the document-term matrix (organize data) into two dataframes (xbox and ps)
def separate(df):
    xbox = df.loc[df['subreddit'] == 0]
    ps = df.loc[df['subreddit'] == 1]
    return xbox, ps

#Creates a dataframe of top words 
def top_words(dataframe):
    """Finds the top words and return results into a sorted dataframe"""
    top = {}
    for i in dataframe:
        top[i] = dataframe[i].sum()
    return pd.DataFrame(sorted(top.items(), key = lambda x: x[1], reverse=True))

#Creates a bar plot of the top nth words
def bar_plot(dataframes, title_list, start_index, end_index, color_list):
    """Creates a bar plot of the top nth words"""
    fig, ax = plt.subplots(figsize=(15,10), nrows=2, ncols=1)
    ax = ax.ravel()
    for i, df in enumerate(dataframes): 
        ax[i].barh(df[0][start_index: end_index], df[1][start_index: end_index], color=color_list[i])
        ax[i].set_title(title_list[i])
        ax[i].set_xlabel('frequency')
        plt.tight_layout();

#Calculates polarity and subjectivity scores 
def sentiment_measure(df):
    '''Creates a polarity and subjectivity columns that contains the values of both sentiment metrics'''
    df = df.copy() #Removes pandas error
    df['polarity'] = df['text'].map(lambda x: TextBlob(x).sentiment.polarity)
    df['subjectivity'] = df['text'].map(lambda x: TextBlob(x).sentiment.subjectivity)
    return df

#Creates a histogram
def histogram(dataframes, title_list, sentiment, color_list):
    '''Creates a histogram plot for each sentiment metric'''
    fig, ax = plt.subplots(figsize=(15,5), nrows=1, ncols=2)
    ax = ax.ravel()
    for i, df in enumerate(dataframes): 
        ax[i].hist(df[sentiment], color=color_list[i])
        ax[i].set_title(title_list[i])
        ax[i].set_xlabel(sentiment + " score")
        ax[i].set_ylabel('frequency')
        plt.tight_layout();
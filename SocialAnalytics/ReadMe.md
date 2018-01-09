

```python
# %load TweetHappiness.py
# Dependencies
import pandas as pd
import numpy as np
import tweepy
import time
import matplotlib.pyplot as plt
import random
from textblob import TextBlob
import datetime

# Initialize Sentiment Analyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

```


```python

# Twitter API Keys
consumer_key = "Kw6QdU3K6aevWMo7cmOxzThLD"
consumer_secret = "dyMMRVQaDsvJZoBrZGdy1zlk1tHGlgcjijFNhT13oKc3GqJFPy"
access_token = "75068443-RZcsP8ypDdOiQWrQyqiMLic7cgvknrlO6DG5FqAry"
access_token_secret = "Loky5gOKJ3EpYPoYXdDkuOI2BpMKnp7N9cJPq7F1Yxp11"
```


```python
# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
```

## Analyze Five Major Media Twitter Account using Vader


```python
# Target Account
target_users = ("@BBC", "@CBS", "@CNN",
                "@Fox", "@nytimes")

# Variables for holding sentiments
sentiments = []
for user in target_users:
    # Counter
    counter = 1
    # Loop through 5 pages of tweets (total 100 tweets)
    for x in range(5):

        # Get all tweets from home feed
        public_tweets = api.user_timeline(user)

        # Loop through all tweets 
        for tweet in public_tweets:

            # Print Tweets
            # print("Tweet %s: %s" % (counter, tweet["text"]))

            # Run Vader Analysis on each tweet
            compound = analyzer.polarity_scores(tweet["text"])["compound"] #how come I don't need to do tweet
            pos = analyzer.polarity_scores(tweet["text"])["pos"]
            neu = analyzer.polarity_scores(tweet["text"])["neu"]
            neg = analyzer.polarity_scores(tweet["text"])["neg"]
            tweets_ago = counter
#             media = user

            # Add sentiments for each tweet into an array
            sentiments.append({"Date": tweet["created_at"], 
                               "Compound": compound,
                               "Positive": pos,
                               "Negative": neu,
                               "Neutral": neg,
                               "Tweets Ago": counter,
                               "Media Source": user})

            # Add to counter 
            counter = counter + 1

```


```python
sentiments_pd = pd.DataFrame.from_dict(sentiments)
sentiments_pd = sentiments_pd.replace({'Media Source':{'@BBC': 'BBC',
                                       '@CBS': 'CBS',
                                       '@CNN': 'CNN',
                                       '@Fox': 'Fox',
                                        '@nytimes': 'New York TImes'
                                        }})
sentiments_pd.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Compound</th>
      <th>Date</th>
      <th>Media Source</th>
      <th>Negative</th>
      <th>Neutral</th>
      <th>Positive</th>
      <th>Tweets Ago</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.2960</td>
      <td>Mon Jan 08 21:29:44 +0000 2018</td>
      <td>BBC</td>
      <td>0.905</td>
      <td>0.000</td>
      <td>0.095</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.0000</td>
      <td>Mon Jan 08 21:29:01 +0000 2018</td>
      <td>BBC</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>0.000</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.1655</td>
      <td>Mon Jan 08 21:28:07 +0000 2018</td>
      <td>BBC</td>
      <td>0.831</td>
      <td>0.099</td>
      <td>0.069</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.3182</td>
      <td>Mon Jan 08 21:27:12 +0000 2018</td>
      <td>BBC</td>
      <td>0.905</td>
      <td>0.000</td>
      <td>0.095</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-0.2500</td>
      <td>Mon Jan 08 21:23:06 +0000 2018</td>
      <td>BBC</td>
      <td>0.882</td>
      <td>0.118</td>
      <td>0.000</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
sentiments_pd['Media Source'].unique()
```




    array(['BBC', 'CBS', 'CNN', 'Fox', 'New York TImes'], dtype=object)




```python
sentiments_pd.to_csv('analysis/social_analytics_GSu.csv', sep=',' )
```


```python
# x_axis_urban = ride_by_city_df[ride_by_city_df['type'] == 'Urban']['Total Rides']
x_axis = sentiments_pd['Tweets Ago']

# Create a random array of data that we will use for our y values
# y_axis_urban = ride_by_city_df[ride_by_city_df['type'] == 'Urban']["Avg Fare"]
y_axis = sentiments_pd['Compound']

size = 80

```


```python
colors = {'BBC':'Gold', 'CBS':'lightskyblue', 'CNN':'lightcoral', 'Fox':'pink', 'New York Times': 'red'}

fig, ax = plt.subplots(1, 1, figsize=(25,8))
# Tells matplotlib that we want to make a scatter plot
# The size of each point on our plot is determined by their x value
plt.scatter(x_axis[sentiments_pd['Media Source'] == 'CNN'], y_axis[sentiments_pd['Media Source'] == 'CNN'], marker="o", c="gold", s=size*2, alpha=0.75, label = "BBC")
plt.scatter(x_axis[sentiments_pd['Media Source'] == 'CBS'], y_axis[sentiments_pd['Media Source'] == 'CBS'], marker="o", c="lightskyblue", s=size*2, alpha=0.75, label = "CBS")
plt.scatter(x_axis[sentiments_pd['Media Source'] == 'CNN'], y_axis[sentiments_pd['Media Source'] == 'CNN'], marker="o", c="lightcoral", s=size*2, alpha=0.75, label = "CNN")
plt.scatter(x_axis[sentiments_pd['Media Source'] == 'Fox'], y_axis[sentiments_pd['Media Source'] == 'Fox'], marker="o", c="pink", s=size*2, alpha=0.75, label = "Fox")
plt.scatter(x_axis[sentiments_pd['Media Source'] == 'New York Times'], y_axis[sentiments_pd['Media Source'] == 'New York Times'], marker="o", c="red", s=size*2, alpha=0.75, label = "New York Times")

plt.title("Sentiment Analysis of Media Tweets (%s)" %datetime.date.today())
plt.xlabel("Tweet Ago")
plt.ylabel("Polarity Score")
plt.legend(title = "Media Source")

plt.style.use('ggplot')

# The y limits of our scatter plot is 0 to 1
plt.ylim(-1, 1)
# The x limits of our scatter plot is 0 to 100
plt.xlim(100, 0)

```




    (100, 0)



## Scatterplot among Five Media Source as 2018-01-07 (each dot is a tweet)


```python
plt.show()
```


![png](ReadMe_files/ReadMe_11_0.png)



![png](ReadMe_files/ReadMe_11_1.png)


## Analyze Five Major Media Twitter Account using TextBlob


```python

# Variables for holding sentiments
sentiments_textblob = []
for user in target_users:
    # Counter
    counter = 1
    # Loop through 5 pages of tweets (total 100 tweets)
    for x in range(5):

        # Get all tweets from home feed
        public_tweets = api.user_timeline(user, page=x)

        # Loop through all tweets 
        for tweet in public_tweets:

            # Print Tweets
            # print("Tweet %s: %s" % (counter, tweet["text"]))

            # Run Vader Analysis on each tweet
            testimonial = TextBlob(tweet['text'])
            polarity = testimonial.sentiment.polarity
            tweets_ago = counter
#             media = target

            # Add sentiments for each tweet into an array
            sentiments_textblob.append({"Date": tweet["created_at"], 
                               "Polarity" : polarity,
                               "Tweets Ago": counter,
                               "Media Source": user})

            # Add to counter 
            counter = counter + 1

```


```python
sentiments_textblob_pd = pd.DataFrame.from_dict(sentiments_textblob)
sentiments_textblob_pd = sentiments_textblob_pd.replace({'Media Source':{'@BBC': 'BBC',
                                                                           '@CBS': 'CBS',
                                                                           '@CNN': 'CNN',
                                                                           '@Fox': 'Fox',
                                                                            '@nytimes': 'New York TImes'
                                                                            }})
sentiments_textblob_pd.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Media Source</th>
      <th>Polarity</th>
      <th>Tweets Ago</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Mon Jan 08 21:29:44 +0000 2018</td>
      <td>BBC</td>
      <td>-0.050000</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Mon Jan 08 21:29:01 +0000 2018</td>
      <td>BBC</td>
      <td>0.114042</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Mon Jan 08 21:28:07 +0000 2018</td>
      <td>BBC</td>
      <td>0.000000</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Mon Jan 08 21:27:12 +0000 2018</td>
      <td>BBC</td>
      <td>0.250000</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Mon Jan 08 21:23:06 +0000 2018</td>
      <td>BBC</td>
      <td>0.136364</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
# x_axis_urban = ride_by_city_df[ride_by_city_df['type'] == 'Urban']['Total Rides']
x_axis = sentiments_textblob_pd['Tweets Ago']

# Create a random array of data that we will use for our y values
# y_axis_urban = ride_by_city_df[ride_by_city_df['type'] == 'Urban']["Avg Fare"]
y_axis = sentiments_textblob_pd['Polarity']

size = 80

```


```python
colors = {'BBC':'Gold', 'CBS':'lightskyblue', 'CNN':'lightcoral', 'Fox':'pink', 'New York Times': 'red'}

fig, ax = plt.subplots(1, 1, figsize=(25,8))
# Tells matplotlib that we want to make a scatter plot
# The size of each point on our plot is determined by their x value
plt.scatter(x_axis[sentiments_textblob_pd['Media Source'] == 'BBC'], y_axis[sentiments_textblob_pd['Media Source'] == 'BBC'], marker="o", c="Gold", s=size*2, alpha=0.75, label = "BBC")
plt.scatter(x_axis[sentiments_textblob_pd['Media Source'] == 'CBS'], y_axis[sentiments_textblob_pd['Media Source'] == 'CBS'], marker="o", c="lightskyblue", s=size*2, alpha=0.75, label = "CBS")
plt.scatter(x_axis[sentiments_textblob_pd['Media Source'] == 'CNN'], y_axis[sentiments_textblob_pd['Media Source'] == 'CNN'], marker="o", c="lightcoral", s=size*2, alpha=0.75, label = "CNN")
plt.scatter(x_axis[sentiments_textblob_pd['Media Source'] == 'Fox'], y_axis[sentiments_textblob_pd['Media Source'] == 'Fox'], marker="o", c="pink", s=size*2, alpha=0.75, label = "Fox")
plt.scatter(x_axis[sentiments_textblob_pd['Media Source'] == 'New York Times'], y_axis[sentiments_textblob_pd['Media Source'] == 'New York Times'], marker="o", c="red", s=size*2, alpha=0.75, label = "New York Times")

plt.title("Media Polarity w/ TextBlob (%s)" %datetime.date.today())
plt.xlabel("Tweet Ago")
plt.ylabel("Polarity Score")
plt.legend(title = "Media Source")
# plt.text(45, 35,"Note: \n Circle Size represents the drivers count per city", horizontalalignment='left')
plt.style.use('ggplot')

# The y limits of our scatter plot is 0 to 1
plt.ylim(-1, 1)
# The x limits of our scatter plot is 0 to 100
plt.xlim(100, 0)
```




    (100, 0)



## Scatterplot among Five Media Source as 2018-01-07 (each dot is a tweet)


```python
plt.show()
```


![png](ReadMe_files/ReadMe_18_0.png)



```python
grouped_sentiments_pd = sentiments_pd.groupby('Media Source')
sentiment_avg_pd = grouped_sentiments_pd.mean()
sentiment_avg_pd.sort_values(by=['Compound'], ascending=False, inplace=True)
sentiment_avg_pd = sentiment_avg_pd.reset_index()
sentiment_avg_pd
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Media Source</th>
      <th>Compound</th>
      <th>Negative</th>
      <th>Neutral</th>
      <th>Positive</th>
      <th>Tweets Ago</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>CNN</td>
      <td>0.231815</td>
      <td>0.91685</td>
      <td>0.00000</td>
      <td>0.08315</td>
      <td>50.5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Fox</td>
      <td>0.131340</td>
      <td>0.77270</td>
      <td>0.08750</td>
      <td>0.13980</td>
      <td>50.5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>BBC</td>
      <td>0.080320</td>
      <td>0.92910</td>
      <td>0.01910</td>
      <td>0.05175</td>
      <td>50.5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>New York TImes</td>
      <td>0.044705</td>
      <td>0.90050</td>
      <td>0.04025</td>
      <td>0.05925</td>
      <td>50.5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>CBS</td>
      <td>0.029320</td>
      <td>0.90665</td>
      <td>0.03905</td>
      <td>0.05430</td>
      <td>50.5</td>
    </tr>
  </tbody>
</table>
</div>



## Bar Plot of Vader using Seaborn


```python
import seaborn as sns

sns.set(style='whitegrid', color_codes=True)
```


```python
# tips = sns.load_dataset(sentiment_avg_pd)
# sns.barplot(x='Media Source', y = 'Compound', data = tips)

sns.barplot(x=sentiment_avg_pd['Media Source'], y = sentiment_avg_pd.Compound, 
            )
plt.title("Overall Media Sentiment based on Twitter (%s)" %datetime.date.today())

plt.show()



```


![png](ReadMe_files/ReadMe_22_0.png)


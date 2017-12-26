# Twitter_Bot
A simple python bot to delete unwanted tweets

## Requirements:

* Python 3 and above
* Pip
* Tweepy module


## Setup

* Install python 3 and pip if you do not already have them installed
* Install tweepy by running pip instal tweepy in your terminal

``` sh
$ pip install tweepy
```


## Running instructions

* Head over to <https://apps.twitter.com> and get your **access keys**

* Create file **credentials.py** in config folder

``` python
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_key = 'YOUR_ACCESS_KEY'
access_secret = 'YOUR_ACCESS_SECRET'
```

* Run **tweet_from_file.py** and see the magic

``` sh
$ python tweet_from_file.py
```
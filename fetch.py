import tweepy #https://github.com/tweepy/tweepy
import csv
import json

from credentials import *

def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print ("getting tweets before %s" % (oldest))
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		x = 0
		ids =[]
		i = 0
		avoid = [833609373121384448]
		for tweet in alltweets:
			# print(str(tweet.id_str) + " -------" + str(tweet.text) + "\n\n")
			tweetid = tweet.id_str
			text = tweet.text
			
			
			if (text[0:11] == "RT @abiudrn" or text[0:19] == "RT @tacklechronicle"):
				#print(str(x) + "______" + str(tweet.id_str) + " -------" + str(tweet.text) + "\n\n")
				ids.append(tweetid)
				#print(str(x) + "______" + str(tweet.id_str) + " -------" + str(tweet.text) + "\n\n")
				try:
					if tweetid in avoid:
						print(str(x) + "______" + str(tweet.id_str) + " -------" + str(tweet.text) + "\n\n")
					else:
						# print(str(x) + "______" + str(tweet.id_str) + " -------" + str(tweet.text) + "\n\n")
						api.destroy_status(tweetid)
						x = x+1
				except :
					avoid.append(tweetid)
					print("New avoid list is " + str(avoid))
				
			# elif (text[0:19] == "RT @tacklechronicle"):
			# 	#print(str(x) + "______" + str(tweet.id_str) + " -------" + str(tweet.text) + "\n\n")
			# 	# x = x+1
			# 	ids.append(tweetid)
			# 	#api.destroy_status(tweetid)
			else:
				pass
		# print (ids)
		print ("...%s tweets downloaded so far" % (len(alltweets)))
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
	
	#write the csv	
	with open('%s_tweets.csv' % screen_name, 'w') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text"])
		writer.writerows(outtweets)
	
	pass


if __name__ == '__main__':
	username = raw_input("Enter your twitter username")
	#pass in the username of the account you want to download
	get_all_tweets(username)
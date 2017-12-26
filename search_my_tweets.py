import tweepy
from time import sleep
from auth.auth import authorise_twitter_app

# list of all unwanted handles
unwanted_retweets = ["@abiudrn:", "@tacklechronicle:", "@LordTanui_:", "@GoldenMbali:", "@Osindewilson:", "@ClintonMwangi_:", "@AmPurityKE:"]


def delete_tweet(my_api):
    try:
        api.destroy_status(tweet.id_str)
        print("Status deleted <---")
        print("\n")
        sleep(5)
    except tweepy.TweepError as e:
        print(e.reason)
        sleep(2)

# ==========================================================================
# Main function
# ==========================================================================

if __name__ == '__main__':
    api = authorise_twitter_app()

    for tweet in tweepy.Cursor(api.user_timeline).items():
        screen_name = tweet.text.split()[1]
        try:
            if screen_name in unwanted_retweets:
                print('Tweet by: ' + tweet.user.name)
                print('Tweet about: ' + tweet.text)
                print('Tweet created on: ' + str(tweet.created_at))

                # delete tweet
                delete_tweet(api)

            else:
                print('Tweet by: ' + tweet.user.name)
                print('Tweet created on: ' + str(tweet.created_at))
                print("Not deleting this!")
                print("\n")

        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break

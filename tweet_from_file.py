import tweepy
from time import sleep
from auth.auth import authorise_twitter_app


# tweet function
def tweet(my_api, time_interval):
    for line in file_lines:
        try:
            print(line)
            if line != '\n':
                my_api.update_status(line)
                sleep(time_interval)
            else:
                print("My tweeting job is done Sir. Ochomoswill")
        except tweepy.TweepError as e:
            print(e.reason)
            sleep(2)


# ==========================================================================
# Main function
# ==========================================================================
if __name__ == '__main__':
    api = authorise_twitter_app()

    # Open text file verne.txt (or your chosen file) for reading
    my_file = open('bin/lines_to_tweet.txt', 'r')

    # Read lines one by one from my_file and assign to file_lines variable
    file_lines = my_file.readlines()

    # Close file
    my_file.close()

    tweet(api, 10)

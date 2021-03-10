import tweepy
 
consumer_key = 'UIQJkKaiyv2ItgGFjLBgIOlWT'
consumer_secret = 'bJT49lVcnpLZvWc1SrV4bm1eo6PepX1qNAHVdlkW7OXdByMdfa'
access_token = '1368358352980500483-3ExS2MuCCHtn8uGQtu9F3YmI4e0n9V'
access_token_secret = 'LocQRak1UlaCJH819lzopPF4dYHc5fxbchHeVmkcIAuPQ'
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
 
user = api.me()
print(user.name)
 
def main():
    search = ("mihyun")
 
    numberofTweets = 50
    for tweet in tweepy.Cursor(api.search, search).items(numberofTweets):
        try:
            tweet.retweet()
            print("Tweet Retweeted")
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
main()

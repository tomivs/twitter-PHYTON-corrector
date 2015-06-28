import tweepy
from twitter_tokens import api_key, api_secret, access_token, access_token_secret

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

twts = api.search(q="phyton")


for s in twts:
    sn = s.user.screen_name
    m = "@%s Buen intento!, pero se dice PYTHON" % (sn)
    s = api.update_status(m, s.id)

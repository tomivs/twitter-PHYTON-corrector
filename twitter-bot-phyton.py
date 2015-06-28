from twitter_tokens import api_key, api_secret, access_token, access_token_secret
from random import randint
import tweepy, time

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

twts = api.search(q="phyton")

frases = ['@%s Buen intento!, pero se dice PYTHON', '@%s Cada vez que dicen PHYTHON, miles de especies "Python" se extinguen en el mundo', '@%s Creo que se dice "Python" en lugar de PHYTON']

for s in twts:
    sn = s.user.screen_name
    m = frases[randint(0, len(frases)-1)] % (sn)
    s = api.update_status(m, s.id)

    time.sleep(600) # hay que dar un poco de tiempo para que no me baneen

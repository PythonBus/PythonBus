import os

mobileme_enabled = False
mobileme_username = ''
mobileme_password = ''

if os.environ['SERVER_SOFTWARE'] == 'Development/1.0':
    twitter_consumer_key = ''
    twitter_consumer_secret = ''
else:
    twitter_consumer_key = ''
    twitter_consumer_secret = ''
    
fts_enabled = False
fts_server = ''
fts_username = ''
fts_password = ''

# change this for deploy is you can registration from http://www.google.com/recaptcha
recaptcha_public_key = '6LdjmR8UAAAAADkl5U54FxWm3KHN9aB2u5lukpRU'
recaptcha_private_key = '6LdjmR8UAAAAAFL6sqcMPpme92egWLDi9zRd5GBg'

daydream_secret = ''

site_key = ''
#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import packages for twitter crawler
import tweepy
from tweepy import OAuthHandler
import json
import pandas as pd

from IPython.display import display
import folium
from folium import plugins

#tweepy method
@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status

cities = pd.read_csv("uscities.csv") 


# In[2]:


#get auth and set up api
consumer_key = #####################
consumer_secret = ##################
access_token = ######################
access_secret = ######################

#username = input("Input your twitter handle (it's what follows the @ symbol): ")
username = 'sleuth3000

# Status() is the data model for a tweet
tweepy.models.Status.first_parse = tweepy.models.Status.parse
tweepy.models.Status.parse = parse
# User() is the data model for a user profil
tweepy.models.User.first_parse = tweepy.models.User.parse
tweepy.models.User.parse = parse
# You need to do it for all the models you need

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)


# In[3]:


#get users friends 
user = api.friends_ids(username)

#get location for each authorized friend
locs = []
for usr in user:
    loc = api.get_user(usr).location
    if len(loc) > 0:
        locs.append(loc)


# In[4]:


#get latlong and verify locations
latlong = []
for place in locs:
    for i, city in enumerate(cities.city):
        if city in place:
            latlong.append([cities.lat[i],cities.lng[i]])


# In[6]:


# center and zoom heatmap
m = folium.Map([35.4676,-97.5136],zoom_start = 4)
# plot heatmap
m.add_child(plugins.HeatMap(latlong, radius=13))
display(m)


# In[ ]:





import twint
import pandas as pd
from collections import Counter
users = [
 'shakira',
 'KimKardashian',
 'rihanna',
 'jtimberlake',
 'KingJames',
 'neymarjr',
]
Now let’s start by scraping Twitter with python and to analyze the relationships between all the 
Twitter accounts in our list above, I’ll write a function named get_followings which will send a 
request to the twint library with a username. This function will return a list of users that our input 
user follows:
ef get_followings(username):
 c = twint.Config()
 c.Username = username
 c.Pandas = True
 twint.run.Following(c)
 list_of_followings = twint.storage.panda.Follow_df
 return list_of_followings['following'][username]
The for loop below will create two variables, as sometimes we get index error when Twitter does 
not respond to our request. For such cases, I added an exception to the code to ignore these users
followings = {}
following_list = []
for person in users:
 print('#####\nStarting: ' + person + '\n#####')
 try:
 followings[person] = get_followings(person)
 following_list = following_list + followings[person]
 except KeyError:
 print('IndexError')
After getting all of the following lists, we can just calculate the most common values in the 
following_list variable to get the most popular accounts among our users. To get the 10 most 
followed accounts, we will use the Counter function of the collection library:
Counter(following_list).most_common(10)
What if we want to see who’s following who in our user group? To study it, I wrote a for loop 
that checks if anyone among the users is in the following list of another person. As a result, it 
creates a list dictionary displaying the following states represented by True and False:
follow_relations ={}
for following_user in followings.keys():
 follow_relation_list = []
 for followed_user in followings.keys():
 if followed_user in followings[following_user]:
 follow_relation_list.append(True)
 else:
 follow_relation_list.append(False)
 follow_relations[following_user] = follow_relation_list
In the code below, the resulting dictionary is transformed into a pandas dataframe for a more 
user-friendly visualization. The rows of the dataframe show the users who follow, while the 
columns show the users who are followed:
following_df = pd.DataFrame.from_dict(follow_relations, 
 orient='index', columns=followings.keys())
following_df
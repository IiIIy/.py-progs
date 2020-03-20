#A python script that finds ppl who subrcribed on publics that could be found with _ keyword
import requests
import time
import json
ID = []
traitors = []
keyword = 'Music'  # keyword

api_key_file = open('api_here.txt', 'r')
api_key = api_key_file.read()
api_key = api_key.rstrip()
api_key_file.close()
r = requests.get('https://api.vk.com/method/groups.search?q='+keyword+'&offset=0&count=100&access_token='+api_key+'&v=5.103') #first request
item = r.json()
for i in item['response']['items']: #request to ID
    ID.append(i['id'])
print("we got" , len(ID), "publics!")

#now is block 2
time.sleep(1)
for i in range(len(ID)):
    r = requests.get('https://api.vk.com/method/groups.getMembers?group_id='+(str(ID[i]))+'&sort=id_asc&offset=0&filter=friends&access_token='+api_key+'&v=5.103')
    item = r.json()
    if ((str(item['response']['items'])) != "[]"):
        traitors.append(item['response']['items'][0])
    time.sleep(0.34)
traitors = set(traitors)
#print(traitors)
if len(traitors) > 0:
    print("ppl found")
else:
    print("no ppl found")

#now is block 3
traitors = list(traitors)
for i in range(len(traitors)):
    r = requests.get('https://api.vk.com/method/users.get?user_ids='+(str(traitors[i]))+'&name_case=Nom&access_token='+api_key+'&v=5.103')
    item = r.json()
    print(str(traitors[i]), str(item['response'][0]['first_name']), str(item['response'][0]['last_name']))

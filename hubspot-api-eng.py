import requests

# setup globals
LOCAL_FINAL_OUTPUT = r"C:\Users\jparsons\PycharmProjects\jwp-alooma\engagements.csv"

# setup url and list
url = "https://api.hubapi.com/engagements/v1/engagements/paged"
querystring = {"hapikey":"demo"}
headers = {'cache-control': "no-cache"}
all_engagements = []

# get the first results hasMore and offset
response = requests.request("GET", url, headers=headers, params=querystring).json()
for r in response['results']:
    all_engagements.append(r)
hasMore = response['hasMore']
offset = response['offset']

# the main loop for getting fields
stoplimit = 0   # self-induced throttle
while hasMore and stoplimit <= 100:
    querystring = {"hapikey": "demo", "offset": offset}
    response = requests.request("GET", url, headers=headers, params=querystring).json()
# send engagements to local file system as csv
    with open(LOCAL_FINAL_OUTPUT, mode='w', buffering=99) as engs:
        count = 0
        for r in response['results']:
            # print(r)
            all_engagements.append(r.get('engagement'))
        for e in all_engagements:
            # header
            if count == 0:
                engs.write('id,' + 'portalId,' + 'createdAt,' + 'lastUpdated,' + 'type' + '\n')
                count += 1
            # little cleanup in-flight
            if str(e.get('id')).lower() == 'none':
                pass
            else:
                # print(str(e.get('id')) + ',' + str(e.get('portalId')) + ',' + str(e.get('createdAt')) + ',' + str(e.get('lastUpdated')) + ',' + str(e.get('type')) + '\n')
                engs.write(str(e.get('id')) + ',' + str(e.get('portalId')) + ',' + str(e.get('createdAt')) + ',' + str(e.get('lastUpdated')) + ',' + str(e.get('type')) + '\n')
    hasMore = response['hasMore']
    offset = response['offset']
    stoplimit += 1
engs.close()


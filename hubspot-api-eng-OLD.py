import requests
import json

# setup globals
APIKEY_VALUE = "demo"
APIKEY = "?hapikey=" + APIKEY_VALUE
HS_API_URL = "https://api.hubapi.com"
LIMIT = "250"
LIMITKEY = "&limit=" + LIMIT

# fields to query "id", "portalId", "createdAt", "lastUpdated", "type"

# build the url and use requests to get data
xurl = "/engagements/v1/engagements/paged"
url = HS_API_URL + xurl + APIKEY + LIMITKEY
s = requests.Session()
response = s.get(url)
raw = json.loads(response.text)

# open the output file dig into results.engagement data and pull out fields of interest.
with open(LOCAL_FINAL_OUTPUT, mode='w') as engs:
    count = 0
    for r in raw['results']:
        newList = []
        newList.append(dict(r.get('engagement')))
        for nl in newList:
            # write header to file
            if count == 0:
                engs.write('id,' + 'portalId,' + 'createdAt,' + 'lastUpdated,' + 'type' + '\n')
                count += 1
            # print(str(nl['id']) + ',' + str(nl['portalId']) + ',' + str(nl['createdAt']) + ',' + str(nl['lastUpdated']) + ',' + str(nl['type']))
            engs.write(str(nl['id']) + ',' + str(nl['portalId']) + ',' + str(nl['createdAt']) + ',' + str(nl['lastUpdated']) + ',' + str(nl['type']) + '\n')

engs.close()






import requests
# print(requests)
url = "http://getbible.net/json?passage="
# added for python applications
end = "&raw=true"
url_response = url + "genesis" + "1" + ":" + "3" +end + "&version=kjv"
response = requests.get(url_response).json()
verse_upper = response["book"][0]["chapter"]
verse_lower = verse_upper["3"]["verse"]
print(verse_lower)
# print(response)

#    url_response = url + book + chapter + ":" + verse +end + "&version=kjv"
#         response = requests.get(url_response).json()
#         verse_upper = response["book"][0]["chapter"]
#         verse_lower = verse_upper[verse]["verse"]
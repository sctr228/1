import urllib.request
import requests

#opener = urllib.request.build_opener()
#response = opener.open('https://httpbin.org/get')
#print(response.read())



#response = requests.get('https://httpbin.org/get')
#print(response.text)
#print(f'Datatype - {type(response.text)}')



# respons = requests.post('https://httpbin.org/get', data='Test data', headers={'h1': 'Test Title'})
# print(respons.text)



res_parse_list = []

response = requests.get('https://coinmarketcap.com/')
response_text = response.text
response_parse = response_text.split('<span>')
for parse_elem1 in response_parse:
    if parse_elem1.startswith('$'):
        for parse_elem2 in parse_elem1.split('</span>'):
            if parse_elem2.startswith('$') and parse_elem2[1].isdigit():
                res_parse_list.append(parse_elem2)

bitcoin_exchange_rate = res_parse_list[0]
print('BTC = ', bitcoin_exchange_rate)

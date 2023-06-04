import urllib.request
import requests

res_parse_list = []

response = requests.get('https://bank.gov.ua/ua/markets/exchangerates')
response_text = response.text
response_parse = response_text.split('<td data-label="Офіційний курс">')
for parse_elem1 in response_parse:
    if parse_elem1.startswith('36'):
        for parse_elem2 in parse_elem1.split('</td>'):
            if parse_elem2.startswith('36') and parse_elem2[1].isdigit():

                res_parse_list.append(parse_elem2)

a = res_parse_list[0]
print('Dolar = ', a)


b = input('Введіть чило гривень: ')
summa = b/a

print(summa)
import requests


secret_key = "61b113ac679d5d0e2ab28c82bb2c3f9c"
short_url = "sz7aqn"
# url = "http://google.com"

with open('URL Bank.txt') as r:  # text file with URLs
    url = r.readlines(1)  # need to clean url
r.close()
print(url)

r = requests.get(f'https://free.qrd.by/api/short?secretkey={secret_key}&shorturl={short_url}&url={url}')  # change URL

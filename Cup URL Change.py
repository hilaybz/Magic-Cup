import requests


secret_key = "61b113ac679d5d0e2ab28c82bb2c3f9c"
short_url = "sz7aqn"
# url = "http://google.com"

with open('URL Bank.txt', "r") as f:  # text file with URLs
    url = f.readline()  # reads URL line
f.close()

print(url)  # check

r = requests.get(f'https://free.qrd.by/api/short?secretkey={secret_key}&shorturl={short_url}&url={url}')  # change URL

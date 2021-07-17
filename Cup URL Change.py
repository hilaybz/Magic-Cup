import requests


secret_key = "61b113ac679d5d0e2ab28c82bb2c3f9c"
short_url = "sz7aqn"


def read_url():
    with open('URL Bank.txt') as f:  # text file with URLs
        url_list = f.readlines()  # reads updated URL line
    f.close()
    for i in url_list:
        i.replace("\n", "")
    url = url_list[int(url_list[0])]
    url_check = str(int(url_list[0])+1) + "\n"
    url_list[0] = url_check
    with open('URL Bank.txt', "w") as f:
        f.writelines(url_list)
    f.close()
    return url


link = read_url()

print(link)
# r = requests.get(f'https://free.qrd.by/api/short?secretkey={secret_key}&shorturl={short_url}&url={url}')  # change URL

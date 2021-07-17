import requests


secret_key = "61b113ac679d5d0e2ab28c82bb2c3f9c"
short_url = "sz7aqn"
url = "http://google.com"
a = 1

with open('URL Bank.txt') as f:  # text file with URLs
    line_number = f.readline()  # reads updated URL line
    print("line_number =", line_number)
    change_number = f.readlines()
    print("change number = ", change_number)
    for line in f:
        a += 1
        print("a =", a)
        if a == int(line_number):
            print("aaaaaaaaaa")
            url = f.readline()
            print("url =", url)
            change_number[0] = "int(line_number) + 1"
            print("change number = ", change_number)
            break
        else:
            f.readline()

# with open('URL Bank.txt', "w") as f:
#     f.writelines(change_number)
    f.close()

    # print(line_number)
# print(url)  # check

# r = requests.get(f'https://free.qrd.by/api/short?secretkey={secret_key}&shorturl={short_url}&url={url}')  # change URL

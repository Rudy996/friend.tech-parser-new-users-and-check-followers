import re
import time
import requests




while True:
    print("start")
    response = requests.get("https://prod-api.kosetto.com/lists/recently-joined").json()
    t = response.get("users")


    n = 0
    while n != 10:
        g = t[n].get("twitterUsername")


        with open(f'full.txt', 'a', encoding="utf8") as file:
            file.write(f'{g}\n')

        with open(f'{g}.txt', 'wb'):
            pass

        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "uk,ru-RU;q=0.9,ru;q=0.8,en-US;q=0.7,en;q=0.6,bg;q=0.5,es;q=0.4",
            "Content-Length": "144",
            "Content-Type": "text/plain",
            "Origin": "https://socialblade.com",
            "Referer": "https://socialblade.com/",
            "Sec-Ch-Ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "Windows",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
        }

        mb = {"n": "pageview", "u": f"https://socialblade.com/twitter/user/{g}", "d": "socialblade.com",
              "r": f"https://socialblade.com/twitter/user/{g}"}

        resp = requests.post(f"https://socialblade.com/twitter/user/{g}", headers=headers, data=mb)
        h = resp.text
        with open(f'{g}.txt', 'a', encoding="utf8") as file:
            file.write(f'{h}\n')
        f = open(f"{g}.txt", "rb+")
        h = 0
        while h != 494:
            f.readline()
            h = h + 1

        q = str(f.readline())
        # print(q)


        def func(x):
            return (re.findall(r'-[0-9,]+|[0-9,]+', x))

        o = func(q)
        try:
            a = int(o[0].replace(',', ""))

            if a > 5000:
                v = t[n].get('address')
                print(f"У {g} подписчиков {a}, его адресс - {v}")
                # re = requests.get(f"https://prod-api.kosetto.com/users/{t[n].get('address')}")
                # print(re.json())
            elif a > 1:
                print(f"{a} подписчиков у {g}")
        except:
            print("pizdaaaa " + g)
        try:
            a = int(o[0])
            with open(f'{g}.txt', 'a', encoding="utf8") as file:
                file.write(f'{h}\n')
            f = open(f"{g}.txt", "rb+")
            h = 0
            while h != 499:
                f.readline()
                h = h + 1
            q = str(f.readline())
            a = func(q)
            k = a[0].replace(',', "")

            # print(g)
            v = t[n].get('address')
            if int(k) > 5000:
                print(f"У {g} подписчиков {k}, его адресс - {v}")
                # re = requests.get(f"https://prod-api.kosetto.com/users/{v}").json()
                # z = re.get("displayPrice")
                # print(z)
            else:
                print(f"{k} подписчиков у {g}")


        except:
            pass

        n = n + 1





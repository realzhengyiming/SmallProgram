#!/usr/bin/env python
# coding: utf-8

import requests
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import json
import time
import os

def getLocalProxyIP()->str:      # 只要使用这个就可以了。提取api中的东西。
    return requests.get("http://127.0.0.1:5010/get/").text

def delprosy(address):
    requests.get(f"http://127.0.0.1:5010/delete?proxy={address}") # 这样子也是很方便进行带入进去的
    print(f"已经删除了{address}")


# 直接莽，直接莽刷自己csdn的阅读量来做一个测试看看先，能不能刷到首页。哈哈哈哈。
# chrome_options = Options()
# chrome_options.add_argument('--headless')  # 使用无头谷歌浏览器模式
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--no-sandbox')
# # 指定谷歌浏览器路径
# webdriver.Chrome(chrome_options=chrome_options,executable_path='/root/zx/spider/driver/chromedriver')

# 留下一个单一的请求的。
#作为一个demon，还可以的了。
# 创建chrome浏览器驱动，无头模式（超爽）
def checkPath(path=os.path.dirname(__file__)+"/cookieData"):  # 检查是否存在路径，没有就创建
    if not os.path.exists(path):
        os.makedirs(path)  # 没有就创建，有就不管



def getCookie(account,password):  # 一周内的第一次登陆都需要使用这个东西
    ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36 Edg/80.0.361.66"
    chrome_options = Options()
    html = None
    for i in range(1,2):  #请求次数
        chrome_options.add_argument('--headless')  # 使用无头模式
        chrome_options.add_argument('user-agent="{}"'.format(ua))  # 试一下uc的ua  切换成了uc浏览器
    #     chrome_options.add_argument('cookie="{}"'.format(cookie))  # 试一下uc的ua  切换成了uc浏览器
        print(ua)
        chrome_options.add_argument('blink-settings=imagesEnabled=false')
        chrome_options.add_argument('--disable-gpu') # 谷歌文档提到需要加上这个属性来规避bug
        # 设置开发者模式启动，该模式下webdriver属性为正常值   一般反爬比较好的网址都会根据这个反爬
        chrome_options.add_argument("--disable-javascript")  # 禁用js  试试这个
        driver = webdriver.Chrome(chrome_options=chrome_options)
        try:
            driver.get("http://210.38.250.43/")   # 学校的教务系统
            html = driver.execute_script("return document.documentElement.outerHTML")
            # 这儿开始想办法进行登陆
            # feifei  17054630130   17053640140
            # 别人  17034480220 970416
            
            driver.find_element_by_name('account').send_keys(account)    #找到用户名定位，传入用户名
            driver.find_element_by_name('password').send_keys(password)   #找到用
            time.sleep(2)
            driver.find_element_by_id("submit_btn").click() #登陆
            cookie = driver.get_cookies()
            # print(cookie)
            jsonCookies = json.dumps(cookie)
            checkPath()  # 创建路径
            with open(f'{os.path.dirname(__file__)}/cookieData/{account}.json', 'w') as f:  # 文件名字就是这个用户名（学号不会重复的）
                f.write(jsonCookies)
            print("访问成功并且写入cookie")  # 大概能持续一段时间
            time.sleep(2)     # 太快关闭了，可能都还没打开有时候，所以给个三秒钟打开
        except Exception as e:
            print(e)  # 输出错误的东西放在这儿。
            print("出现问题跳过执行这个selenium")
        finally:  # 无论如何最后都要关闭的
            driver.quit()


def getCourseByCookie(account): # 如果2小时内登陆过一次，那后面的操作都可以直接读取cookie
    str=''
    checkPath()  # 创建路径
    with open(f'{os.path.dirname(__file__)}/cookieData/{account}.json','r',encoding='utf-8') as f:
        listCookies=json.loads(f.read())
    cookie = [item["name"] + "=" + item["value"] for item in listCookies]
    cookiestr = '; '.join(item for item in cookie)
    print(cookiestr)
     
    url='http://210.38.250.43/xsgrkbcx!getKbRq.action?xnxqdm=201902&zc=4'  # 这个是获得课程表的url地址
    headers={
        'cookie':cookiestr,
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    }

    # 输出提取到一周的课程
    html=requests.get(url=url,headers=headers)
    result = None
    try :
        result = json.loads(html.text)
    except Exception as e:
        result = None  # 没有就返回空
           # print(html.text)
    # for i in json.loads(html.text)[0]:
        # print(i)
        # print()
    return result


if __name__ == '__main__':
    # main()
    account = '17034480220'
    password = '970416'

    # todo
    # 1. 微信登陆，获得对并绑定account和密码。把用户密码保存下来吗 
    # 1.先读取数据库，前端的，后端不处理这个，
    # ，看看有没有这周的课程表，或者存两周的
    # 2.前端如果发送请求到后端，那就说明前端没有了。返回给前就行了
    # 3.还有老师需要进行区分，老师的话就使用默认账号来进行登陆操作等。就可以
    # 4.还需要封装很多的url的东西，作为api登陆后提取出来进行使用。加油，还挺多东西要做的
    # 5.可能还需要使用https，django这个要怎么搞才可以是https协议的呢。
    # 别人   970416
    # getCookie(account,password)  todo 晚点再试试这个cookie过期的话要怎么处理
    result = getCourseByCookie(account)
    if result :
        print(result)
    
    # checkPath()
    # if  


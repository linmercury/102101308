import requests
import re
import jieba
import json
import argparse
import time
import wordcloud
import imageio
from PIL import Image
import numpy as np

def get_search(v_keyword,v_max_page):
    for page in range(1, v_max_page+1):
        #print('开始爬取第{}页'.format(page))
        # 请求地址
        url ='https://api.bilibili.com/x/web-interface/wbi/search/type'
        #请求头
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.202.400 QQBrowser/11.9.5355.400',
            'cookie': "buvid3=70501EB5-E653-4E02-9376-2E1DD360C20E167609infoc; LIVE_BUVID=AUTO6916333422156997; buvid4=3F2ABD8C-E3A2-2D39-1EAD-704A3E583FD302604-022012016-vOzn9I7noT9QVOz1iMrijQ%3D%3D; i-wanna-go-back=-1; CURRENT_BLACKGAP=0; buvid_fp_plain=undefined; _uuid=810DEDC10E-B108B-10FFE-2293-1910FE217D58F02564infoc; DedeUserID=503447892; DedeUserID__ckMd5=e9487ca903c0999f; b_ut=5; b_nut=100; rpdid=|(u))kkYu|lu0J'uYY)~Yllkl; is-2022-channel=1; CURRENT_FNVAL=4048; hit-new-style-dyn=1; CURRENT_PID=bf2d44b0-cf7d-11ed-b93c-35fd18e80dea; CURRENT_QUALITY=80; nostalgia_conf=-1; hit-dyn-v2=1; fingerprint=4724177ae5b07159c5d94493382f3aeb; buvid_fp=4724177ae5b07159c5d94493382f3aeb; FEED_LIVE_VERSION=undefined; header_theme_version=CLOSE; SESSDATA=ebe72160%2C1709982534%2C8086b%2A92CjDNe3aNRyq-W7bLrr-4u3hvPXtIvjeIuxZSQwVlDhtVMT--4_uIgf2aUaS3pf3eUFYSVjhENklOQWRGbjY0Sk9LU1JqTTF1anhOZnZVYWpGQ2szbkNtcmVka3dpQWtvQ01ONkZiUndjYUM3YkU2eVVwb1BiSXpCa243NHBCZkFTQ3Vycl9mZ2t3IIEC; bili_jct=ed33257a1a172e704352a5df0923618d; sid=8euu4fj0; bili_ticket_expires=1694689807; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQ2ODk4MDcsImlhdCI6MTY5NDQzMDYwNywicGx0IjotMX0.V9TCtCkBerPgxW8jUFB6WepyxHSkGWsyQDfhwyH-N54; home_feed_column=5; bp_video_offset_503447892=840463338204823702; PVID=3; bsource=search_sougo; browser_resolution=1658-800; b_lsid=E31E45E5_18A8E42192C",
            'referer': 'https://search.bilibili.com/all?keyword=%E6%97%A5%E6%9C%AC%E6%A0%B8%E6%B1%A1%E6%9F%93%E6%B0%B4%E6%8E%92%E6%B5%B7&from_source=webtop_search&spm_id_from=333.1007&search_source=3&page=3&o=84',
            'accept': 'application / json, text / plain, * / *'

        }
        #请求参数
        params = {
            '__refresh__': 'true',
            '_extra': ' ',
            'context': '',
            'page': page,
            'page_size': 30,
            'from_source': '',
            'from_spmid': '333.337',
            'platform': 'pc',
            'highlight': '1',
            'single_column': '0',
            'keyword': v_keyword,
            'qv_id': 'mjWq9JN3dfXzBmLK202ofAfeeHEA80HR',
            'ad_resource': '5654',
            'source_tag': '3',
            'gaia_vtoken': '',
            'category_id': '',
            'search_type': 'video',
            'dynamic_offset': 60,
            'web_location': '1430654',
            'w_rid': 'ac94c01c5e02305d11e98c28c3b37808',
            'wts': '1694603980'
        }
        # 向页面发送请求
        response_1 = requests.get(url=url,headers=headers,params=params)
        # 获取BV号
        # bv_num=[]
        for index in response_1.json()['data']['result']:
            bv_num = index['bvid']
            with open('BV号.txt',mode='a',encoding='utf-8') as f:
                f.write(bv_num)
                f.write('\n')
                cid_url = "https://api.bilibili.com/x/player/pagelist?bvid=" + str(bv_num) + "&jsonp=jsonp"
                response_2 = requests.get(url=cid_url,headers=headers).content.decode('utf-8')
                response_2_dict = json.loads(response_2)
                values = response_2_dict['data']
                for cid_values in values:
                    cid = cid_values.get('cid')
                    cid = str(cid)
                    # dirt = json.loads(response_2.text)
                    # cid = dirt['data'][0]['cid']
                    dm_url = "https://api.bilibili.com/x/v1/dm/list.so?oid=" + cid
                    response_3 = requests.get(url=dm_url, headers=headers)
                    response_3.encoding = response_3.apparent_encoding
                    # 2.获取数据
                    #print(response_3.text)
                   # print(response_3)
                    # 3.解析数据
                    data_list = re.findall('<d p=".*?">(.*?)</d>', response_3.text)
                    print(data_list)
                    for data in data_list:
                        with open('弹幕.txt', mode='a', encoding='utf-8') as f:
                            f.write(data)
                            f.write('\n')
                        print(data)
                    # time.sleep(0.2)

if __name__=='__main__':
    search_keyword='日本核污染水排海'
    max_page=10
    get_search(v_keyword=search_keyword.encode('utf8'),v_max_page=max_page)



#img = imageio.imread('2.png')
img = np.array(Image.open('3.png'))
# 1读取弹幕数据
f = open('弹幕.txt',encoding='utf-8')
text = f.read()
# print(text)
# 2.分词，把一句话分成很多词汇
text_list = jieba.lcut(text)
#print(text_list)
text_str = ' '.join(text_list)
#print(text_str)
# 3.词云图配置
wc = wordcloud.WordCloud(
    width=500,
    height=500,
    background_color='white',
    mask =img,
    stopwords= { '的','了','吗','吧','这','人','不','但','好','让','给','他','还','我','在','有','那','也','是','菇','来','一下','去','谁','吃'},
    font_path='msyh.ttc'
)
wc.generate(text_str)
wc.to_file('词云.png')

"""
            with open('BV号.txt',mode='a',encoding='utf-8') as f:
                f.write(bv_num)
                f.write('\n')
                #print(bv_num)
                cidget(bv_num)
         


def cidget(bvid, response_2=None):
    url = "https://api.bilibili.com/x/player/pagelist?bvid=" + str(bvid) + "&jsonp=jsonp"
    response_2=requests.get(url)
    dirt=json.loads(response_2.text)
    cid=dirt['data'][0]['cid']
    #print(cid)
    DMget(cid)


def DMget(cid):
# 1.发送请求
    url="https://api.bilibili.com/x/v1/dm/list.so?oid="+str(cid)
    headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.202.400 QQBrowser/11.9.5355.400',
            'cookie': "buvid3=70501EB5-E653-4E02-9376-2E1DD360C20E167609infoc; LIVE_BUVID=AUTO6916333422156997; buvid4=3F2ABD8C-E3A2-2D39-1EAD-704A3E583FD302604-022012016-vOzn9I7noT9QVOz1iMrijQ%3D%3D; i-wanna-go-back=-1; CURRENT_BLACKGAP=0; buvid_fp_plain=undefined; _uuid=810DEDC10E-B108B-10FFE-2293-1910FE217D58F02564infoc; DedeUserID=503447892; DedeUserID__ckMd5=e9487ca903c0999f; b_ut=5; b_nut=100; rpdid=|(u))kkYu|lu0J'uYY)~Yllkl; is-2022-channel=1; CURRENT_FNVAL=4048; hit-new-style-dyn=1; CURRENT_PID=bf2d44b0-cf7d-11ed-b93c-35fd18e80dea; CURRENT_QUALITY=80; nostalgia_conf=-1; hit-dyn-v2=1; fingerprint=4724177ae5b07159c5d94493382f3aeb; buvid_fp=4724177ae5b07159c5d94493382f3aeb; FEED_LIVE_VERSION=undefined; header_theme_version=CLOSE; SESSDATA=ebe72160%2C1709982534%2C8086b%2A92CjDNe3aNRyq-W7bLrr-4u3hvPXtIvjeIuxZSQwVlDhtVMT--4_uIgf2aUaS3pf3eUFYSVjhENklOQWRGbjY0Sk9LU1JqTTF1anhOZnZVYWpGQ2szbkNtcmVka3dpQWtvQ01ONkZiUndjYUM3YkU2eVVwb1BiSXpCa243NHBCZkFTQ3Vycl9mZ2t3IIEC; bili_jct=ed33257a1a172e704352a5df0923618d; sid=8euu4fj0; bili_ticket_expires=1694689807; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQ2ODk4MDcsImlhdCI6MTY5NDQzMDYwNywicGx0IjotMX0.V9TCtCkBerPgxW8jUFB6WepyxHSkGWsyQDfhwyH-N54; home_feed_column=5; bp_video_offset_503447892=840463338204823702; PVID=3; bsource=search_sougo; browser_resolution=1658-800; b_lsid=E31E45E5_18A8E42192C",
            'referer': 'https://search.bilibili.com/all?keyword=%E6%97%A5%E6%9C%AC%E6%A0%B8%E6%B1%A1%E6%9F%93%E6%B0%B4%E6%8E%92%E6%B5%B7&from_source=webtop_search&spm_id_from=333.1007&search_source=3&page=3&o=84'
    }
    response_3=requests.get(url=url,headers=headers)
    response_3.encoding=response_3.apparent_encoding
# 2.获取数据
    print(response_3.text)
# 3.解析数据
    data_list = re.findall('<d p=".*?">(.*?)</d>',response_3.text)
    for index in data_list:
        with open('弹幕.txt',mode='a',encoding='utf-8')as f:
            f.write(index)
            f.write('\n')
            print(index)
"""


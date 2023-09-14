import jieba
import wordcloud
import imageio
from PIL import Image
import numpy as np
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
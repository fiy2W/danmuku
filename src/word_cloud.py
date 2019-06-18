# -*- coding: utf8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import jieba
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import skimage

d_lst = np.load('../data/danmu.npz')['danmuku']

danmu = ''
for d in d_lst:
    danmu += '{}\n'.format(d['danmu'])
    

#cut_danmu= jieba.cut(danmu)
#result = "/".join(cut_danmu)

im = skimage.io.imread('../ext/background.png')

wc = WordCloud(font_path='../ext/chinese.msyh.ttf',
               background_color='white',
               width=1920, height=1080,
               max_font_size=50, max_words=1000,
               mask=im)
wc.generate(danmu)
image_color = ImageColorGenerator(im)
wc.recolor(color_func=image_color)
wc.to_file('../data/wordcloud.png')
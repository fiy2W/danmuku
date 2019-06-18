# -*- coding: utf8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import requests
from bs4 import BeautifulSoup as bs
import re
import numpy as np

main_url = 'https://www.bilibili.com/bangumi/media/md3054/?from=search&seid=18096115107428450330'
req = requests.get(main_url)
req.encoding = 'utf8'
cid_lst = re.findall("\"cid\":(.+?),", str(req.content))

d_lst = []
for cid in cid_lst:
    url = 'https://comment.bilibili.com/{}.xml'.format(cid)

    req = requests.get(url)
    req.encoding = 'utf8'
    
    soup = bs(req.text, 'lxml')
    d = soup.find_all('d')
    
    for d_v in d:
        danmuku = {
            'danmu': d_v.text,
            'url': url,
            'time': d_v.attrs['p'].split(',')[0],
            }
        d_lst.append(danmuku)

np.savez('../data/danmu.npz', danmuku=d_lst)

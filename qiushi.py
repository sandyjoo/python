# -*- coding:gbk -*-

import requests
import urllib
import re
import thread
import time


def get_imgurl(first_url, page):
    url = first_url + "page/" + str(page)
    contents = requests.get(url).text
    reg = r'src="(.+?\.jpe?g)" alt='
    imgre = re.compile(reg)
    imgurllist = re.findall(imgre, contents)
    return imgurllist


def download_img(imgurl):
    imghttp = 'http:' + imgurl
    imgname = imgurl.split('/')[-1]
    urllib.urlretrieve(imghttp, 'pics\%s' % imgname)
    print '%s �������, ��ʱ %f s' % (str(imgname), time.time()-start_time)


if __name__ == "__main__":
    first_url = "https://www.qiushibaike.com/imgrank/"
    start_page = int(raw_input('��������ʼҳ��'))
    end_page = int(raw_input('��������ֹҳ��'))
    print '��ʼ����'
    start_time = time.time()
    for page in range(start_page, end_page+1):
        imgurllist = get_imgurl(first_url, page)
        for imgurl in imgurllist:
            thread.start_new_thread(download_img, (imgurl,))
            time.sleep(0.05)
    raw_input("press ENTER to exit...\n")

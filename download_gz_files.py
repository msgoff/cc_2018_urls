import re
<<<<<<< HEAD
import urllib
=======
import requests
>>>>>>> 4407173048c48268e6f7c2733f3c3a54bd3371e4
import os

f = open('2018_urls.dat')
urls = [x.replace('\n','') for x in f.readlines() if 'gz' in x]

folders = set()
for url in urls:
    folder = [x for x in re.split('/',url) if 'CC' in x]
    if folder:
        folders.add(folder[0])

for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)


<<<<<<< HEAD
=======
import urllib
>>>>>>> 4407173048c48268e6f7c2733f3c3a54bd3371e4

def download_gz(url):
    f_name = re.split('/',url)[-1]
    print f_name
    for folder in folders:
        if folder in url:
             fullfilename = os.path.join(folder,f_name)
    urllib.urlretrieve(url, fullfilename)

<<<<<<< HEAD
for url in urls: 
    download_gz(urls)
=======
download_gz(urls[0])
>>>>>>> 4407173048c48268e6f7c2733f3c3a54bd3371e4


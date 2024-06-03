import requests
import threading
import time
import shutil

urls = ['https://deepskyhosting.com/img/p/full/32051628155402.jpg',
'https://spacegid.com/wp-content/uploads/2014/09/m31.jpg',
'https://www.sai.msu.ru/news/2018/12/12/Map_Moon_2018.jpg',
'https://kartin.papik.pro/uploads/posts/2023-06/1688139170_kartin-papik-pro-p-kartinki-karta-zvezdnogo-neba-s-sozvezdiya-58.jpg'
]
def download(url):
    filename = 'threading_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.jpg'
    res = requests.get(url, stream = True)
    if res.status_code == 200:
        with open(filename,'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print(f"Downloaded {url} in {time.time()-start_time:.2f}seconds")

threads = []
start_time = time.time()

for url in urls:
    thread = threading.Thread(target=download, args=[url])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

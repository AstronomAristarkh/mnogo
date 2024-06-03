import asyncio
import aiohttp
import time
import requests
import shutil

urls = ['https://deepskyhosting.com/img/p/full/32051628155402.jpg',
'https://spacegid.com/wp-content/uploads/2014/09/m31.jpg',
'https://www.sai.msu.ru/news/2018/12/12/Map_Moon_2018.jpg',
'https://kartin.papik.pro/uploads/posts/2023-06/1688139170_kartin-papik-pro-p-kartinki-karta-zvezdnogo-neba-s-sozvezdiya-58.jpg'
]
async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            res = requests.get(url, stream = True)
            filename = 'asincio_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.jpg'
            if res.status_code == 200:
                with open(filename,'wb') as f:
                    shutil.copyfileobj(res.raw, f)
                print(f"Downloaded {url} in {time.time()-start_time:.2f}seconds")
            

async def main():
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)

start_time = time.time()
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
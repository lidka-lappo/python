import requests
from bs4 import BeautifulSoup
import time
from PIL import Image, ImageFilter 
import numpy as np
from concurrent.futures import ProcessPoolExecutor, as_completed

url = 'https://www.if.pw.edu.pl/~mrow/dyd/wdprir/'
req = requests.get(url)
#print(req.status_code)
soup = BeautifulSoup(req.text, 'html.parser')
#print(req.text)
#print(req.request.headers)

def fun(w):
  if w.text.endswith(".png") :
    print(w.text)
    r=requests.get(url+w.text).content
    f=open(w.text,'wb')
    f.write(r)
    img = Image.open(w.text)
    img.convert("1")
    img = img.filter(ImageFilter.GaussianBlur(radius = 5))
    f.write(r)

if __name__ == '__main__':
  start_time = time.time()
  for w in soup.find_all('a'):
    fun(w)
  end_time = time.time()
  elapsed_time = end_time - start_time
  print("Elapsed time1  :", elapsed_time, "seconds")


  start_time = time.time()
  with ProcessPoolExecutor(24) as ex:
    futures = [ex.submit(fun(w)) for w in soup.find_all('a')]
    for f in as_completed(futures): 
      pass
  end_time = time.time()
  elapsed_time = end_time - start_time
  print("Elapsed time2  :", elapsed_time, "seconds")
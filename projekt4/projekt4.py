import requests
from bs4 import BeautifulSoup
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("file_name",type = str)
args = parser.parse_args()
file_name=args.file_name

req = requests.get('https://oboznaukowy.edu.pl/#turnusy')
print(req.status_code)
#print(req.text)
#print(req.request.headers)
soup = BeautifulSoup(req.text, 'html.parser')
workshops = soup.find('section', {'id' : 'turnusy'})
#print(workshops.text)

workshop_names =[]
for w in workshops.find_all('p', {'class' : 'workshops__workshop__title'}):
    #print(w.text)
    titles=w.find('a')
    print(f'{titles.text.strip()}')

with open(file_name, 'w') as f:
    json.dump(titles, f)

#& C:/Users/Litka/AppData/Local/Programs/Python/Python39/python.exe "c:/Users/Litka/Desktop/python_projects/projekt 4/projekt4.py" warsztaty.json
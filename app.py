import csv
import requests

BASE_URL:str =''
URL:str = ''

candidate_numbers:list[str]=[]

def get_items(candidate_number:list[str])->:
    res = requests.get(f'{BASE_URL}')

with open('candidate.csv', 'rb') as candidate_csv:
    reader = csv.reader(candidate_csv)
    reader.next() # skips header row
    for row in reader:
        candidate_numbers.append(row[0])
    

get_items(candidate_numbers)
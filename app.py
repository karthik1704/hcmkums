import csv
from typing import Any
import requests

BASE_URL: str = ''
URL: str = ''

candidate_numbers: list[str] = []

AUTH = ('99999', 'pass')


def download_attachment(items: list[Any]):
    for item in items:
        file_path = item['FilePath']
        res = requests.get(f'{BASE_URL}{file_path}', auth=AUTH)
        ext = item['filename'].split('.')[-1]
        print(ext)
        open(f'test.{ext}', 'wb').write(res.content)


def get_items(candidate_numbers: list[str]) -> None:
    for number in candidate_numbers:
        res = requests.get(f'{BASE_URL}{number}{URL}', auth=AUTH)
        data = res.json()
        items: list[Any] = data.get('items')
        download_attachment(items)


with open('candidate.csv', 'rb') as candidate_csv:
    reader = csv.reader(candidate_csv)
    reader.next()  # skips header row
    for row in reader:
        candidate_numbers.append(row[0])


get_items(candidate_numbers)

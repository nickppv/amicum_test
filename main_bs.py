from bs4 import BeautifulSoup
import requests
import pandas

response = requests.get(url="https://www.python.org/downloads/")
soup = BeautifulSoup(response.text, 'lxml')

# ищем основной блок с данными
base_block = soup.find('div', class_='row download-list-widget')

# получаем весь блок с основной информацией
base_info = base_block.find('ol', class_='list-row-container menu')
# в следующих строчка получаем данные версии, даты релиза и ссылки
release_version = [i.text for i in base_info.find_all(
    'span', class_='release-number')]
release_date = [i.text for i in base_info.find_all(
    'span', class_='release-date')]
release_download = ['https://www.python.org' + i.find('a', href=True).get(
    'href') for i in base_info.find_all('span', class_='release-download')]
release_notes = [i.find('a', href=True).get(
    'href') for i in base_info.find_all('span', class_='release-enhancements')]

# создаем датафрейм и сохраняем его в файл xlsx
df = pandas.DataFrame({
    'Release version': release_version,
    'Release date': release_date,
    'Download': release_download,
    'Release Notes': release_notes
    })
df.to_excel('./python_releases_bs.xlsx', sheet_name="Releases", index=False)

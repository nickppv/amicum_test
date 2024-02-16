import pandas
from playwright.sync_api import sync_playwright

with sync_playwright() as pw:
    browser = pw.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://www.python.org/downloads/', timeout=0)

    # получаем основной блок с данными
    base_block = page.query_selector('.download-list-widget')

    # получаем всю основную информацию о релизах
    base_info = base_block.query_selector('.list-row-container')
    release_version = [
        i.inner_text() for i in base_info.query_selector_all('.release-number')
        ]
    release_date = [
        i.inner_text() for i in base_info.query_selector_all('.release-date')
        ]
    release_download = [
        'https://www.python.org' + i.query_selector('a').get_attribute(
            'href') for i in base_info.query_selector_all('.release-download')
        ]
    release_notes = [
        i.query_selector('a').get_attribute(
            'href') for i in base_info.query_selector_all(
                '.release-enhancements')
        ]

# создаем датафрейм и сохраняем его в файл xlsx
df = pandas.DataFrame({
    'Release version': release_version,
    'Release date': release_date,
    'Download': release_download,
    'Release Notes': release_notes
    })
df.to_excel('./python_releases_PW.xlsx', sheet_name="Releases", index=False)

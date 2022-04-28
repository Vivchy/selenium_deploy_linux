from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By

s = Service(r'driver/chromedriver.exe')


def main():
    """
    Основной цикл программы
    """
    # options
    options = webdriver.ChromeOptions()

    headers = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    options.add_argument(f'user-agent={headers}')

    # off webdriver
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--window-size=1550,1000")
    options.headless = True
    driver = webdriver.Chrome(
        service=s,
        options=options
    )


    try:
        driver.get(
            "https://www.youtube.com/")

        driver.implicitly_wait(10)
        search = driver.find_elements(By.XPATH, '//ytd-rich-item-renderer[@class = "style-scope ytd-rich-grid-row"]')
        time.sleep(2)
        print(search)
        for item in search:
            title = item.find_element(By.XPATH, './/a[@id = "video-title-link"]').text
            print(title)
        time.sleep(3)
    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    main()

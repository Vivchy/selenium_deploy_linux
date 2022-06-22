from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.mouse_button import MouseButton
import time

from source import path

s = Service(path) #путь до веб драйвера

def main():
    """
    Основной цикл программы
    """

    headers = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"

    options = webdriver.ChromeOptions()
    options.add_argument(f'user-agent={headers}')
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--window-size=1550,1000")

    # options.headless = True
    options.add_argument("--no-sandbox")


    driver = webdriver.Chrome(
        service=s,
        options=options
    )

    try:
        driver.get('https://market.yandex.ru/product--krossovki-reebok/1696969396?glfilter=14474402%3A14583828_101739014259&glfilter=14871214%3A27649830_101739014259&cpc=yjq_ZgI1NJOtvK96lZzW4Uk3ejvnYuMIXjGlsVXKDehwsJ6CkKa3pxlPaRsZl37_sULP2wyd1S5Ll00O7HTYOJYGxPDQ35-BNq2ukl0Nz5kw7UOGU_vWJJpzDVZiKGhx8rT2BIacNce9k8thtFuuD6wIZv0gyj7Y8njWrXoJ1hmz1Mt9q_ABx5CObYQFZQbX&sku=101739014259&offerid=gdsG2OIFbb9pxHUuX3oB_g&cpa=1')


        time.sleep(40)
    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    main()

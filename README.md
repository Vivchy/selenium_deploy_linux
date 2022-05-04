# Deploy selenium driver python on linux 

***

## Установка python 

https://github.com/Vivchy/example-python-requirements-deploy

## Установка google chrome и зависимостей

<pre>sudo apt update && sudo apt upgrade</pre>
<pre>sudo apt install -y libxss1 libappindicator1 libindicator7</pre>

скачать google chrome

<pre>wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb</pre>

установить пакет

<pre>sudo apt install ./google-chrome-stable_current_amd64.deb
</pre>

приверить версию 

<pre>google-chrome --version</pre>

***

## Для запуска скрипта с помощью баш скрипта 

<pre>
#!/bin/bash
/home/linux/selenium_deploy_linux/venv/bin/python main.py
</pre>

## Ошибки

#### selenium.common.exceptions.webdriverexception: message: 'chromedriver' executable may have wrong permissions

дать права на выполнение файла драйвера

<pre>chmod +x "/home/vivchy/selenium_deploy_linux/driver/chromedriver_linux"</pre>
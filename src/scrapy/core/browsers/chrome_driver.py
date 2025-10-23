import logging

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class ChromeBrowser:
    def __init__(self, logger, headless: bool = False):
        self.headless = headless
        self._logger = logger

    def create_driver(self) -> webdriver.Chrome:
        options = webdriver.ChromeOptions()
        if self.headless:
            options.add_argument('--headless=new')
        options.add_argument('--start-maximized')
        options.add_argument('--disable-infobars')
        options.add_argument('--disable-extensions')

        self._logger.logger.debug('Criando instância do Chrome WebDriver...')

        service = ChromeService(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=options)

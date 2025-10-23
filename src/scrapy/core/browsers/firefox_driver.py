import logging

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


class FirefoxBrowser:
    def __init__(self, logger, headless: bool = False):
        self.headless = headless
        self._logger = logger

    def create_driver(self) -> webdriver.Firefox:
        options = webdriver.FirefoxOptions()
        if self.headless:
            options.add_argument('--headless')

        self._logger.logger.debug('Criando instância do Firefox WebDriver...')

        service = FirefoxService(GeckoDriverManager().install())
        return webdriver.Firefox(service=service, options=options)

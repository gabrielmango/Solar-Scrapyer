import logging

from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class EdgeBrowser:
    def __init__(self, logger, headless: bool = False):
        self.headless = headless
        self._logger = logger

    def create_driver(self) -> webdriver.Edge:
        options = webdriver.EdgeOptions()
        if self.headless:
            options.add_argument('--headless=new')
        options.add_argument('--start-maximized')

        self._logger.logger.debug('Criando instância do Edge WebDriver...')

        service = EdgeService(EdgeChromiumDriverManager().install())
        return webdriver.Edge(service=service, options=options)

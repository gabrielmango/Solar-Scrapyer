import logging

from src.scrapy.core.base_driver import BaseDriverManager
from src.scrapy.core.browsers.chrome_driver import ChromeBrowser
from src.scrapy.core.browsers.edge_driver import EdgeBrowser
from src.scrapy.core.browsers.firefox_driver import FirefoxBrowser


class SeleniumDriverFactory(BaseDriverManager):
    SUPPORTED_BROWSERS = {
        'chrome': ChromeBrowser,
        'firefox': FirefoxBrowser,
        'edge': EdgeBrowser,
    }

    def __init__(self, logger, browser: str = 'chrome', headless: bool = False):
        self.browser_name = browser.lower()
        self.headless = headless
        self._logger = logger
        self.driver = None

    def start(self):
        if self.browser_name not in self.SUPPORTED_BROWSERS:
            raise ValueError(
                f"Navegador '{self.browser_name}' não suportado. Opções: {list(self.SUPPORTED_BROWSERS.keys())}"
            )

        browser_class = self.SUPPORTED_BROWSERS[self.browser_name]
        browser_instance = browser_class(headless=self.headless, logger=self._logger)

        self.driver = browser_instance.create_driver()
        self._logger.logger.info(f'Driver iniciado com sucesso: {self.browser_name.capitalize()}')
        self.driver.implicitly_wait(2)
        return self.driver

    def quit(self):
        if self.driver:
            self._logger.logger.info('Encerrando o WebDriver.')
            self.driver.quit()
            self.driver = None

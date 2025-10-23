from src.scrapy.actions.selenium_actions import SeleniumActions
from src.scrapy.core.selenium_factory import SeleniumDriverFactory


class SeleniumManager:
    def __init__(self, logger, browser: str = 'chrome', headless: bool = False):
        self.logger = logger
        self.driver_factory = SeleniumDriverFactory(browser=browser, headless=headless, logger=logger)
        self.driver = self.driver_factory.start()
        self.actions = SeleniumActions(self.driver, logger)

    def __enter__(self):
        return self.actions

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver_factory.quit()

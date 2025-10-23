import logging
from typing import Tuple

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SeleniumActions:
    def __init__(self, logger, driver: webdriver.ChromeService):
        self.driver = driver
        self._logger = logger

    def abrir_pagina(self, url: str):
        self._logger.logger.info(f'Abrindo página: {url}')
        self.driver.get(url)
        self.espera_carregar_pagina()

    def espera_carregar_pagina(self, timeout: int = 10):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    def espera_carregar_elemento(self, locator: Tuple[By, str], timeout: int = 30) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def clicar(self, locator: Tuple[By, str], usar_js: bool = False, timeout: int = 30):
        self._logger.logger.debug(f'Clicando no elemento {locator}')
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        if usar_js:
            self.driver.execute_script('arguments[0].click();', element)
        else:
            element.click()
        self.espera_carregar_pagina()

    def escrever(self, locator: Tuple[By, str], texto: str, timeout: int = 10, enter: bool = False):
        element = self.espera_carregar_elemento(locator, timeout)
        element.clear()
        element.send_keys(texto)
        if enter:
            element.send_keys(Keys.ENTER)

    def criar_locator(self, tipo: str, valor: str) -> Tuple[By, str]:
        mapping = {
            'id': By.ID,
            'class': By.CLASS_NAME,
            'xpath': By.XPATH,
            'link_text': By.LINK_TEXT,
            'name': By.NAME,
            'tag': By.TAG_NAME,
            'css': By.CSS_SELECTOR,
        }
        return (mapping[tipo], valor)

from abc import ABC, abstractmethod


class BaseDriverManager(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def quit(self):
        pass

from typing import Dict

class HttpRequest:
    def __init__(self, header: Dict = None, body: Dict = None, querry_params: Dict = None) -> None:
        self.header = header
        self.body = body
        self.querry_params = querry_params

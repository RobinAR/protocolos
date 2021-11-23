# Rojas Alvarez Robin Agustin
# Protocol   python -m unittest discover tests

from pathlib import Path
from datetime import datetime

class Protocol:
    def __init__(self, email, password, port, resource):
        self.email = email
        self.password = password
        self.port = port
        self.resource = resource


class Http (Protocol):
    def conection(self):
        diccionario = {"protocol": "http", "state": "conection is succesful", "url": f"http:// {self.resource}"}
        return diccionario

    def get_response(self):
        return "<h1> http conecyion <h1>"

    def get_detail_conection(self, password):
        if password == self.password:
            return {"email": self.email, "port": 80, "resource": self.resource}
        return "incorrect data"


class Ftp(Protocol):
    def conection(self):
        diccionario = {"protocol": "ftp", "state": "conection is succesful", "url": f"ftp://{self.resource}"}
        return diccionario

    def get_response(self):
        ruta_actual = Path('.')
        return [str(ruta) for ruta in ruta_actual.iterdir()]

    def get_detail_conection(self, password):
        if password == self.password:
            return {
                "email": self.email,
                "port": 21,
                "resource": self.resource
            }
        return "incorrect data"


class Smb (Protocol):
    def conection(self):
        diccionario = {"protocol": "Smb", "state": "conection is succesful", "url": f"smb://{self.resource}"}
        return diccionario

    def get_response(self):
        ruta_actual = Path('.')
        return [str(ruta) for ruta in ruta_actual.iterdir() if ruta.is_dir()]

    def get_detail_conection(self, password):
        if password == self.password:
            return {
                "email": self.email,
                "port": 445,
                "resource": self.resource
            }
        return "incorrect data"


class FactoryProtocol:
    def __init__(self, email, password, resource):
        self.__email = email
        self.__password = password
        self.__resource = resource
        self.historial = []

    def buil_conection(self, protocol):
        if protocol == "http":
            conexion = Http(self, self.__email, self.__password, self.__resource)
            hora = datetime.now().strftime("%H: %M%: %S")
            self.historial.append(f"{protocol}{hora}")
            return conexion
        if protocol == "ftp":
            conexion = Ftp(self, self.__email, self.__password, self.__resource)
            hora = datetime.now().strftime("%H: %M%: %S")
            self.historial.append(f"{protocol}{hora}")
            return conexion
        if protocol == "smb":
            conexion = Smb(self, self.__email, self.__password, self.__resource)
            hora = datetime.now().strftime("%H: %M%: %S")
            self.historial.append(f"{protocol}{hora}")
            return conexion

    def get_history_conections(self):
        return self.historial

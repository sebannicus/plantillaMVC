# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 22:53:53 2024

@author: Carlos Luco Montofré
"""

from .gestor_usuarios import Gestor_Usuarios
from .gestor_datos import Gestor_Datos
from .gestor_cajas import Gestor_Cajas
from .gestor_transacciones import Gestor_Transacciones
from .gestor_tasa_conversion import Gestor_Tasa_Conversion


class Model:
    def __init__(self):
        self.gestor_usuarios = Gestor_Usuarios()
        self.gestor_datos = Gestor_Datos()
        self.gestor_cajas = Gestor_Cajas()
        self.gestor_transacciones = Gestor_Transacciones()
        self.gestor_tasa_conversion = Gestor_Tasa_Conversion()

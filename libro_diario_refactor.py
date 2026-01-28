"""
Este archivo nos va a permitir mejorar los calsulos
"""

# Importamos tipos para mejorar la claridad del código
from typing import Dict, List


class LibroDiario:
    """
    Clase que representa un libro diario contable.
    Se encarga de almacenar y procesar transacciones financieras.
    """

    def __init__(self) -> None:
        """
        Constructor de la clase.
        Inicializa una lista vacía donde se guardarán las transacciones.
        """
        # Lista que almacena cada transacción como un diccionario
        self.transacciones: List[Dict[str, object]] = []

    def agregar_transaccion(
        self,
        fecha: str,
        descripcion: str,
        monto: float,
        tipo: str
    ) -> None:
        """
        Agrega una transacción al libro diario después de validar los datos.

        :param fecha: Fecha en la que se realiza la transacción
        :param descripcion: Detalle o concepto de la transacción
        :param monto: Valor monetario de la transacción (debe ser positivo)
        :param tipo: Tipo de transacción ('ingreso' o 'egreso')
        """

        # Validación del tipo de transacción
        if tipo not in ("ingreso", "egreso"):
            raise ValueError(
                "El tipo de transacción debe ser 'ingreso' o 'egreso'."
            )

        # Validación del monto para evitar valores incorrectos
        if not isinstance(monto, (int, float)) or monto <= 0:
            raise ValueError(
                "El monto debe ser un número positivo."
            )

        # Se agrega la transacción válida a la lista
        self.transacciones.append(
            {
                "fecha": fecha,              
                "descripcion": descripcion,  
                "monto": monto,              
                "tipo": tipo,                
            }
        )

    def calcular_resumen(self) -> Dict[str, float]:
        """
        Calcula el total de ingresos y egresos registrados.

        :return: Diccionario con los totales calculados
        """

        # Inicialización de acumuladores
        ingresos: float = 0.0
        egresos: float = 0.0

        # Recorremos todas las transacciones registradas
        for transaccion in self.transacciones:
            # Si la transacción es un ingreso, se suma al total de ingresos
            if transaccion["tipo"] == "ingreso":
                ingresos += float(transaccion["monto"])
            # Caso contrario, se considera un egreso
            else:
                egresos += float(transaccion["monto"])

        # Se retorna un diccionario con los resultados
        return {
            "ingresos": ingresos,
            "egresos": egresos,
        }

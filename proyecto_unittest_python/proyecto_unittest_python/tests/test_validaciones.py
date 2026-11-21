import unittest
from decimal import Decimal
from app.auxiliares.validaciones import (
    validar_rut,
    validar_correo,
    validar_fecha_nacimiento,
    validar_sku_producto,
    validar_nombre_producto,
    validar_descripcion_producto,
    validar_precio_producto,
)


class TestValidaciones(unittest.TestCase):

    def test_rut_valido(self):
        rut, mensaje = validar_rut("12.345.678-5")
        self.assertEqual(rut, "12.345.678-5")
        self.assertEqual(mensaje, "RUT válido")

    def test_rut_invalido(self):
        rut_malo, msg_malo = validar_rut("12.345.678-9")
        self.assertEqual(rut_malo, "")
        self.assertEqual(msg_malo, "RUT inválido")

        rut_sin_guion, msg_formato = validar_rut("12345678")
        self.assertEqual(rut_sin_guion, "")
        self.assertEqual(msg_formato, "Formato de RUT incorrecto")

    def test_sku_producto_obligatorio_y_maximo(self):
        valor_vacio, msg_vacio = validar_sku_producto("   ")
        self.assertIsNone(valor_vacio)
        self.assertEqual(msg_vacio, "El SKU es obligatorio.")

        valor_largo, msg_largo = validar_sku_producto("A" * 51)
        self.assertIsNone(valor_largo)
        self.assertEqual(msg_largo, "El SKU no puede exceder 50 caracteres.")

        valor_ok, msg_ok = validar_sku_producto("SKU-001")
        self.assertEqual(valor_ok, "SKU-001")
        self.assertEqual(msg_ok, "Sku válido.")

    def test_nombre_producto_obligatorio_y_maximo(self):
        valor_vacio, msg_vacio = validar_nombre_producto("")
        self.assertIsNone(valor_vacio)
        self.assertEqual(msg_vacio, "El nombre es obligatorio.")

        valor_largo, msg_largo = validar_nombre_producto("N" * 256)
        self.assertIsNone(valor_largo)
        self.assertEqual(msg_largo, "El nombre no puede exceder 255 caracteres.")

        valor_ok, msg_ok = validar_nombre_producto("Monitor Gamer")
        self.assertEqual(valor_ok, "Monitor Gamer")
        self.assertEqual(msg_ok, "Nombre válido.")

    def test_descripcion_producto_obligatoria(self):
        valor_ok, msg_ok = validar_descripcion_producto("Monitor 27 pulgadas 144Hz")
        self.assertEqual(valor_ok, "Monitor 27 pulgadas 144Hz")
        self.assertEqual(msg_ok, "Descripción válido.")

        valor_vacio, msg_vacio = validar_descripcion_producto("   ")
        self.assertIsNone(valor_vacio)
        self.assertEqual(msg_vacio, "El descripción es obligatorio.")

    def test_precio_producto_debe_ser_decimal_valido(self):
        precio_ok, msg_ok = validar_precio_producto("19990.50")
        self.assertEqual(precio_ok, Decimal("19990.50"))
        self.assertEqual(msg_ok, "Precio válido.")

        casos_invalidos = ["", "-1", "1.234", "NaN", "100000000", "texto"]
        for precio in casos_invalidos:
            with self.subTest(precio=precio):
                valor, _ = validar_precio_producto(precio)
                self.assertIsNone(valor)

    def test_correo_valido_e_invalido(self):
        correo_ok, msg_ok = validar_correo("juan.perez@gmail.com")
        self.assertEqual(correo_ok, "juan.perez@gmail.com")
        self.assertEqual(msg_ok, "Formato de correo correcto")

        correo_malo, msg_malo = validar_correo("juan.perez.gmail.com")
        self.assertEqual(correo_malo, "")
        self.assertEqual(msg_malo, "Formato de correo incorrecto")

    def test_fecha_nacimiento_valida_e_invalida(self):
        fecha_ok, msg_ok = validar_fecha_nacimiento("25/12/2000")
        self.assertEqual(fecha_ok, "25/12/2000")
        self.assertEqual(msg_ok, "Formato de fecha correcto")

        fecha_mala, msg_malo = validar_fecha_nacimiento("2000-12-25")
        self.assertEqual(fecha_mala, "")
        self.assertEqual(msg_malo, "Formato de fecha NO corresponde, ingrese nuevamente...")


if __name__ == "__main__":
    unittest.main()
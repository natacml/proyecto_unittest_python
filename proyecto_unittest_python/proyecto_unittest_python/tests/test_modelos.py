import unittest
from decimal import Decimal
from app.modelos.cliente import Cliente
from app.modelos.producto import Producto
from app.modelos.pedido import Pedido, EstadoPedido
from app.modelos.detalle_pedido import DetallePedido


class TestCliente(unittest.TestCase):

    def test_creacion_cliente(self):
        cliente = Cliente(
            id_cliente=1,
            rut_cliente="12.345.678-5",
            nombre_cliente="Juan",
            apellido_cliente="Perez",
            correo_cliente="juan@gmail.com",
            fecha_nacimiento_cliente="2000-12-25",
        )

        self.assertEqual(cliente.rut_cliente, "12.345.678-5")
        self.assertNotEqual(cliente.rut_cliente, "12.345.678-9")
        self.assertEqual(cliente.nombre_cliente, "Juan")
        self.assertNotEqual(cliente.nombre_cliente, "Hola")
        self.assertEqual(cliente.correo_cliente, "juan@gmail.com")
        self.assertEqual(cliente.fecha_nacimiento_cliente, "2000-12-25")


class TestProducto(unittest.TestCase):

    def test_creacion_producto(self):
        producto = Producto(
            id_producto=1,
            sku_producto="SKU-001",
            nombre_producto="Teclado Mecánico",
            descripcion_producto="Teclado RGB switch red",
            precio_producto=Decimal("45990.00"),
            producto_habilitado=True,
        )

        self.assertEqual(producto.sku_producto, "SKU-001")
        self.assertNotEqual(producto.sku_producto, "SKU-999")
        self.assertEqual(producto.nombre_producto, "Teclado Mecánico")
        self.assertNotEqual(producto.nombre_producto, "Mouse")
        self.assertEqual(producto.descripcion_producto, "Teclado RGB switch red")
        self.assertNotEqual(producto.descripcion_producto, "Sin descripción")
        self.assertEqual(producto.precio_producto, Decimal("45990.00"))
        self.assertNotEqual(producto.precio_producto, Decimal("1000.00"))
        self.assertTrue(producto.producto_habilitado)


class TestPedido(unittest.TestCase):

    def test_creacion_pedido(self):
        cliente = Cliente(
            id_cliente=1,
            rut_cliente="12.345.678-5",
            nombre_cliente="Juan",
            apellido_cliente="Perez",
        )
        pedido = Pedido(
            id_pedido=10,
            cliente_pedido=cliente,
            total_pedido=Decimal("25000.00"),
            estado_pedido=EstadoPedido.PEND,
            pedido_habilitado=True,
        )

        self.assertEqual(pedido.id_pedido, 10)
        self.assertNotEqual(pedido.id_pedido, 99)
        self.assertEqual(pedido.cliente_pedido.rut_cliente, "12.345.678-5")
        self.assertEqual(pedido.total_pedido, Decimal("25000.00"))
        self.assertNotEqual(pedido.total_pedido, Decimal("0.00"))
        self.assertEqual(pedido.estado_pedido, EstadoPedido.PEND)
        self.assertNotEqual(pedido.estado_pedido, EstadoPedido.CANC)


class TestDetallePedido(unittest.TestCase):

    def test_creacion_detalle_pedido(self):
        pedido = Pedido(id_pedido=10)
        producto = Producto(id_producto=1, sku_producto="SKU-001", nombre_producto="Mouse")
        detalle = DetallePedido(
            id_detalle_pedido=1,
            id_pedido=pedido,
            id_producto=producto,
            cantidad=3,
            precio_unitario=Decimal("15000.00"),
            habilitado=True,
        )

        self.assertEqual(detalle.id_detalle_pedido, 1)
        self.assertNotEqual(detalle.id_detalle_pedido, 2)
        self.assertEqual(detalle.cantidad, 3)
        self.assertNotEqual(detalle.cantidad, 1)
        self.assertEqual(detalle.precio_unitario, Decimal("15000.00"))
        self.assertNotEqual(detalle.precio_unitario, Decimal("0.00"))


if __name__ == "__main__":
    unittest.main()
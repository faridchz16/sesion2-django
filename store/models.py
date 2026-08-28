from dataclasses import dataclass
from typing import List


@dataclass
class Producto:
    id: int
    nombre: str
    descripcion: str
    precio: float
    stock: int
    categoria: str


PRODUCTOS: List[Producto] = [
    Producto(
        id=1,
        nombre="Arroz 1kg",
        descripcion="Arroz blanco grano largo, paquete de 1kg",
        precio=2.50,
        stock=50,
        categoria="Alimentos"
    ),
    Producto(
        id=2,
        nombre="Aceite de girasol 1L",
        descripcion="Aceite vegetal de girasol, botella de 1 litro",
        precio=3.80,
        stock=30,
        categoria="Alimentos"
    ),
    Producto(
        id=3,
        nombre="Jabón en polvo 2kg",
        descripcion="Detergente en polvo para ropa, bolsa de 2kg",
        precio=5.20,
        stock=25,
        categoria="Limpieza"
    ),
    Producto(
        id=4,
        nombre="Papel higiénico 4 rollos",
        descripcion="Papel higiénico suave, paquete de 4 rollos",
        precio=2.90,
        stock=40,
        categoria="Higiene"
    ),
    Producto(
        id=5,
        nombre="Leche entera 1L",
        descripcion="Leche pasteurizada entera, caja de 1 litro",
        precio=1.80,
        stock=60,
        categoria="Lácteos"
    ),
]


def get_next_id() -> int:
    return max(p.id for p in PRODUCTOS) + 1 if PRODUCTOS else 1


def add_producto(producto: Producto) -> None:
    PRODUCTOS.append(producto)
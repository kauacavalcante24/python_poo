from category import Category
from dataclasses import dataclass


@dataclass
class Transaction:
    detail: str
    value: float
    category: Category
    date: str
    time: str


    def __str__(self):
        return (
            f"Detalhes: {self.detail}\n"
            f"Valor: R$ {self.value:.2f}\n"
            f"Categoria: {self.category}\n"
            f"Data: {self.date}\n"
            f"Hora: {self.time}"
        )

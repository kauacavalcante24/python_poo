from dataclasses import dataclass


@dataclass
class Category:
    name: str


    def __str__(self):
        return self.name

from dataclasses import dataclass


@dataclass
class Automobilis:
    marke: str
    modelis: str
    metai: int

# class Automobilis:
#     def __init__(self, marke, modelis, metai):
#         self.marke = marke
#         self.modelis = modelis
#         self.metai = metai
#
#     def __repr__(self):
#         return f"{self.marke} {self.modelis} ({self.metai})"

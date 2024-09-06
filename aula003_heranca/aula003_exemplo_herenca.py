# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Colyana Magalhães da Silva Nascimento
# Data: 05/09/2024
# Aula 003 - Herança

import os


class Animal:
    def __init__(self, nome):
        self.nome = nome
        
    def latir(self):
        return 'Isto está no método latir()'
    
    def miar(self):
        return 'Isto está no método miar()'
    
class Cachorro(Animal):
    def latir(self):
        return f'{self.nome} está latindo!'
    
class Gato(Animal):
    def miar(self):
        return f'{self.nome} está miando.'
    
os.system('cls')

cao = Cachorro('Rex')
gato = Gato('Tobias')
print(cao.latir())
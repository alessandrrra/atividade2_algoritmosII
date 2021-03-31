# AlunoEnsinoMedio
# ano: int
# imprimir():void

from aluno import Aluno

class AlunoEnsinoMedio:
    def __init__(self, codigo, nome, matricula, ano):
        Aluno.__init__(self, codigo, nome, matricula)
        self.ano = ano
    
    def imprimir(self):
        Aluno.imprimir(self)
        print("Ano: ", self.ano)
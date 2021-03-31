# AlunoGraduação
# semestre: int
# imprimir():void

from aluno import Aluno

class AlunoGraduacao:
    def __init__(self, codigo, nome, matricula, semestre):
        Aluno.__init__(self, codigo, nome, matricula)
        self.semestre = semestre
    
    def imprimir(self):
        Aluno.imprimir(self)
        print("Semestre: ", self.semestre)
'''
Construa um algoritmo para implementar a classe Aluno(código, nome, matrícula).
A classe Aluno possui duas subclasses, a classe AluEnsinoMedio(ano) e AlunoGraduacao(semestre).
As 3 classes possuem o método construtor e também o método imprimir(), que imprimi na tela
os valores de todos os atributos da sua classe
'''

# Aluno
# codigo: int
# nome: string
# matricula:string
# imprimir():void

# AlunoEnsinoMedio
# ano: int
# imprimir():void

# AlunoGraduação
# semestre: int
# imprimir():void

class Aluno:
    def __init__(self, codigo, nome, matricula):
        self.codigo = codigo
        self.nome = nome
        self.matricula = matricula
    
    def imprimir(self):
        print("Código: ", self.codigo)
        print("Nome: ", self.nome)
        print("Matrícula: ", self.matricula)


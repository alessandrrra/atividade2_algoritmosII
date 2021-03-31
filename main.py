from aluno import Aluno
from aluno_ensinomedio import AlunoEnsinoMedio
from aluno_graduacao import AlunoGraduacao

a = Aluno(1, "Alessandra", "MAT048")
a.imprimir()

aem = AlunoEnsinoMedio(2, "Moisés", "MAT182", 3)
aem.imprimir()

ag = AlunoGraduacao(3, "Nycolle", "MAT558", 6)
ag.imprimir()
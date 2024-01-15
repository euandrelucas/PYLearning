# 4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
# Informações da escola
nomeEscola = 'Instituto Padre Miguelinho'
mediaAnual = 6
# Pegando as informações do Aluno
nomeAluno = input('Digite o nome completo do Aluno:')
bimestre1 = input('Qual foi a nota do 1º bimestre?')
bimestre2 = input('Qual foi a nota do 2º bimestre?')
bimestre3 = input('Qual foi a nota do 3º bimestre?')
bimestre4 = input('Qual foi a nota do 4º bimestre?')
# Calculando a média
notaTotal = int(float(bimestre1)) + int(float(bimestre2)) + int(float(bimestre3)) + int(float(bimestre4))
media = int(float(notaTotal)) / 4
if media >= mediaAnual:
    print('{} - BOLETIM ANUAL\nA média do aluno {} foi: {}, sendo considerado APROVADO!'.format(nomeEscola, nomeAluno, media))
else:
    print('{} - BOLETIM ANUAL\nA média do aluno {} foi: {}, sendo considerado REPROVADO!'.format(nomeEscola, nomeAluno, media))
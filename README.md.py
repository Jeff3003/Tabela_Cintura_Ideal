# Tabela_Cintura_Ideal
#Desenvolvido em Python. Tabela RCQ ( Relação Cintura Quadril )

print ('=' * 75)
print ('{:^25}Tabela de Cintura Ideal'.format(''))
print ('=' * 75)

print (''' QUAL É O SEU SEXO ?
[1] Masculino
[2] Feminino ''')
masc = 1
fem = 2
sexo = int(input('Digite sua opção : '))
cintura = float(input('Qual é a circunferência (dois dedos acima do umbigo) da sua cintura ? : '))
quadril = float(input('Qual é a circunferência (a parte mais larga) do seu quadril ? : '))
rcq = (cintura / quadril) * 100
print('Seu RCQ (Relação Cintura Quadril) é {:.0f}'.format(rcq))
if sexo == masc:
    if rcq <= 90:
        print ('\033[1;32mCintura Ideal. Parabéns !')
    elif rcq >= 90.5 and rcq <= 95:
        print ('\033[1;33mRisco Médio. Fique Atento !')
    elif rcq >= 95.5 and rcq <= 100:
        print ('\033[1;91mRisco Alto. Mude seus hábitos alimentares e pratique exercícios físicos !')
    else:
        print ('\033[1;31mVocê tem risco alto de desenvolver doenças cardiovasculares')
        print ('\033[1;31mCUIDE-SE !!!')
elif sexo == fem:
    if rcq <= 80:
        print('\033[1;32mCintura ideal. Parabéns !')
    elif rcq >= 80.5 and rcq <= 85:
        print('\033[1;33mRisco Médio. Fique Atento !')
    elif rcq >= 85.5 and rcq <= 90:
        print('\033[1;91mRisco Alto. Mude seus hábitos alimentares e pratique exercícios físicos!')
    else:
        print('\033[1;31mVocê tem risco alto de desenvolver doenças cardiovasculares')
        print('\033[1;31mCUIDE-SE !!!')

print ('\033[1;94m=' * 75)
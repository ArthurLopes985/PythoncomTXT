# Empresa= Atlantic
# Programadores:
# Arthur Lopes de Oliveira - RGM: 11241102534
# Bruno da Silva Negy - RGM: 11241102531
# João Vitor da Silva Martins Vaz - RGM: 11241103064
# Data= 16/04/2024
# Programa de RH dos funcionários da empresa Atlantic.
#---------------------------------------------------------------------------------------------------
import locale
import os
from datetime import date
data_atual = date.today( )
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
lista=[]
dic={}
def carregar():
    with open("trabalhoRH_TXT_Dados.txt","r") as Registro:
        for i in Registro:
            lista.append(i.rstrip().split(","))
    for i in lista:
        dic[i[0]]=[i[1],i[2],i[3]]
    return dic
def salvar(dict):
    with open("trabalhoRH_TXT_Dados.txt","w") as Registro:
        for chave,dados in dict.items(dic):
            Registro.write(f"{chave},{dados[0]},{dados[1]},{dados[2]}\n")
def pre():
    print('\033[1mInformações pré-existentes:\033[0m')
    for i in dic[alter]:
        print(i)
def logo():
    os.system('cls')
    cor='\033[0;30;44m'
    fim='\033[0m'
    imp='''
╔═╗╔╦╗╦  ╔═╗╔╗╔╔╦╗╦╔═╗  
╠═╣ ║ ║  ╠═╣║║║ ║ ║║    
╩ ╩ ╩ ╩═╝╩ ╩╝╚╝ ╩ ╩╚═╝ 
'''
    print(f'{cor}{imp}{fim}')
def retornar():
    input('\033[1mPressione \'ENTER\' para retornar ao menu anterior.\033[0m')
#---------------------------------------------------------------------------------------------------
info = ('\033[1mNumero ou caractere invalido. Tente  Novamente.\033[0m',
        '\033[1mValor invalido, precisa ser um numero.\033[0m',
        '\033[1mDigite o registro a ser alterado: \033[0m',
        '\033[1mRegistro alterado com sucesso!\033[0m',
        '\033[1mRegistro inexistente.\033[0m',
        '\033[1mPrecisa ter apenas letras. Tente novamente.\033[0m')
carregar()
while True:
    logo()
    print('\033[1mSeja bem vindo(a) à plataforma de RH da Atlantic!\nAbaixo estão as opções disponiveis\033[0m')
    menu = input('''\033[1m
[ 1 ] Consultar funcionários
[ 2 ] Pesquisar funcionário por nome ou número de registro
[ 3 ] Deletar algum registro, nome de funcionário ou salário
[ 4 ] Alterar algum registro, nome de funcionário ou salário
[ 5 ] Adicionar registro, nome de funcionário ou salário
[ 6 ] Para encerrar o programa
Insira a opção desejada: \033[0m''')
    if menu not in ['1', '2', '3', '4', '5', '6']:    
        logo()
        print(info[0])
    elif menu == '1':
        logo()
        for chave,dados in dic.items():
            print(f'\033[1m{chave:^10} {dados[0]:^20} {dados[2]:^10}\033[0m')
        retornar()
    elif menu == '2':
        logo()
        while True:
            logo()
            menu1=input('''\033[1m
[1] Pesquisa pelo ID 
[2] Pesquisa pelo nome
[3] Voltar ao menu principal 
Insira a opção desejada: \033[0m''')
            if menu1 == '1':
                logo()
                val=input('\033[1mEntre com o registro a ser pesquisado: \033[0m')
                if val in dic:
                    print(f'''\033[1mFuncionário pesquisado: {val}
Nome do funcionário: {dic[val][0]}
Salário: R${dic[val][1]}
Profissão: {dic[val][2]}\033[0m''')
                    retornar()
                else:
                    print('\033[1mRegistro não encontrado.\033[0m')
                    retornar()
            elif menu1 == '2':
                logo()
                valn=input('\033[1mEntre com o nome a ser pesquisado: \033[0m')
                for chave, dados in dic.items():
                    if valn in dados[0]:
                        print(f'\033[1m{chave:^10} {dados[0]:^20} R${dados[1]:^10} {dados[2]:^10}\033[0m')
                retornar()
            else:
                break
    elif menu == '3':
        logo()
        delet=input('\033[1mDigite o registro a ser deletado: \033[0m')
        if delet in dic.keys():
            print(f'''\033[1mFuncionário a ser apagado: {delet}
Nome do funcionário: {dic[delet][0]}
Salário: R${dic[delet][1]}
Profissão: {dic[delet][2]}\033[0m''')
            resp=input('\033[1mDigite S ou s se deseja apagar esses dados: \033[0m')
            if resp =='S' or resp =='s':
                del dic[delet]
                logo()
                print('\033[1mRegistro deletado com sucesso!\033[0m')
                retornar()
            else:
                logo()
                print('\033[1mDados não apagados\033[0m')
                retornar()
        else:
            print(info[4])
            retornar()
    elif menu == '4':
        while True:
            logo()
            menu2=input('''\033[1m
[1] Alterar nome
[2] Alterar Salário
[3] Alterar Profissão 
[4] Voltar ao menu principal
Insira a opção desejada: \033[0m''')
            if menu2 not in ['1', '2', '3', '4']:
                logo()
                print(info[0])
            elif menu2 == '1':
                logo()
                try:
                    alter=input(info[2])
                except ValueError as error:
                    logo()
                    print(info[1])
                if alter in dic:
                    while True:
                        pre()
                        nome_alt=input('\033[1mDigite o novo nome: \033[0m')
                        if nome_alt.isalpha():
                            dic[alter][0]=nome_alt
                            logo()
                            print(info[3])
                            retornar()
                            break
                        else:
                            logo()
                            print(info[5])
                else:
                    print(info[4])
                    retornar()
            elif menu2 == '2':
                logo()
                try:
                    alter=input(info[2])
                except ValueError as error:
                    logo()
                    print(info[1])
                if alter in dic:
                    while True:
                        pre()
                        mud_sal=input('\033[1mDigite o novo salário: \033[0m')
                        if mud_sal.isdigit():
                            dic[alter][1]=mud_sal
                            logo()
                            print(info[3])
                            retornar()
                            break
                        else:
                            logo()
                            print(info[5])
                else:
                    print(info[4])
                    retornar()
            elif menu2 == '3':
                logo()
                try:
                    alter=input(info[2])
                except ValueError as error:
                    logo()
                    print(info[1])
                if alter in dic:
                    while True:
                        pre()
                        prof_alt=input('\033[1mDigite a nova profissão: \033[0m')
                        if prof_alt.isalpha():
                            dic[alter][2]=prof_alt
                            logo()
                            print(info[3])
                            retornar()
                            break
                        else:
                            logo()
                            print(info[5])
                else:
                    print(info[4])
                    retornar()
            else:
                break
    elif menu == '5':
        logo()
        adic=input('\033[1mDigite o registro a ser adicionado: \033[0m')
        if adic in dic.keys():
            print('\033[1mRegistro ja existente.\033[0m')
            retornar()
        else:
            while True:
                nome_add=input('\033[1mDigite o novo nome: \033[0m')
                if nome_add.isalpha():
                    break
                else:
                    print(info[5])
            while True:
                sal_add=input('\033[1mDigite o novo salário: \033[0m')
                if sal_add.isdigit():
                    break
                else:
                    print('\033[1mPrecisa ter apenas números. Tente novamente.\033[0m')
            while True:
                prof_add=input('\033[1mDigite a nova profissão: \033[0m')
                if prof_add.isalpha():
                    break
                else:
                    print(info[5])
            dic[adic]=[nome_add, sal_add, prof_add]
            salvar(dict)
            print('\033[1mRegistro adicionado com sucesso!\033[0m')
            retornar()
    else:
        logo()
        print('\033[1mPrograma encerrado.\033[0m')
        print(f'\033[1m{data_atual.strftime("%d/%m/%Y")}\033[0m')
        break
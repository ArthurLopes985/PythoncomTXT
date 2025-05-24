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
import sqlite3
conexão=sqlite3.connect("trabalhoRH_SQL_Dados.db")
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
def pre():
    print('\033[1mInformações pré-existentes:\033[0m')
    for i in row[alter]:
        print(i)
def retornar():
    input('\033[1mPressione \'ENTER\' para retornar ao menu anterior.\033[0m')
def procurar_fun(nomval):
    with conexão:
        a=conexão.execute('SELECT * FROM Registro WHERE Primeiro_nome LIKE ? OR Segundo_nome LIKE ?', (f'%{nomval}%', f'%{nomval}%'))
        rows=a.fetchone()
        return rows
#---------------------------------------------------------------------------------------------------
while True:
    logo()
    print('Seja bem vindo(a) à plataforma de RH da Atlantic!\nAbaixo estão as opções disponiveis')
    menu = input('''
[ 1 ] Consultar funcionários
[ 2 ] Pesquisar funcionário por nome ou número de registro
[ 3 ] Deletar algum registro, nome de funcionário ou salário
[ 4 ] Alterar algum registro, nome de funcionário ou salário
[ 5 ] Adicionar registro, nome de funcionário ou salário
[ 6 ] para encerrar o programa
Insira a opção desejada: ''')
    if menu not in ['1', '2', '3', '4', '5', '6']:
        logo()
        print('\033[1mNumero ou caractere invalido. Tente  Novamente.\033[0m')
    elif menu == '1':
        logo()
        with conexão:
            cursor=conexão.execute('SELECT * FROM Registro')
            for row in cursor:
                print(f'{row[0]:^10} {row[1]:^10} {row[2]:^10} {row[3]:^10}')
        retornar()
    elif menu == '2':
        while True:
            logo()
            menu1=input('''\033[1m
[1] Pesquisa pelo ID 
[2] Pesquisa pelo nome
[3] Voltar ao menu principal 
Insira a opção desejada: \033[0m''')
            if menu1 == '1':
                while True:
                    try:
                        val=int(input("\033[1mEntre com o registro a ser pesquisado: \033[0m"))
                    except ValueError as error:
                        logo()
                        print('\033[1mValor invalido, precisa ser um numero.\033[0m')
                    else:
                        break
                with conexão:
                    cursor=conexão.execute("SELECT*FROM Registro WHERE ID=?", (val,))
                    row=cursor.fetchone()
                    if row:
                        print(f'''\033[1mFuncionário pesquisado: {val}
Nome do funcionário: {row[1]} {row[2]}
Salário: R${row[3]}
Profissão: {row[4]}\033[0m''')
                        retornar()
                    else:
                        print("\033[1mRegistro não encontrado.\033[0m")
                        retornar()
            if menu1 == '2':
                while True:
                    nomval=input("\033[1mDigite o nome a ser pesquisado: \033[0m")
                    if nomval.isalpha():
                        break
                    else:
                        logo()
                        print('\033[1mValor invalido, precisa ser letras.\033[0m')
                funcionarios= procurar_fun(nomval)
                for emp in funcionarios:
                    print(f'\033[1m{emp}\033[0m')
                retornar()
            else:
                break
    elif menu == '3':
        logo()
        while True:
            try: 
                delet=int(input("\033[1mDigite o registro a ser deletado: \033[0m"))
            except ValueError as error:
                logo()
                print('\033[1mValor invalido, precisa ser um numero.\033[0m')
            with conexão:
                cursor=conexão.execute("SELECT*FROM Registro WHERE ID=?", (delet,))
                row=cursor.fetchone()
                if row:
                    with conexão:
                        print(f'''\033[1mFuncionário a ser apagado: {delet}
Nome do funcionário: {row[1]} {row[2]}
Salário: R${row[3]}
Profissão: {row[4]}\033[0m''')
                        resp=input('\033[1mDigite S ou s se deseja apagar esses dados: \033[0m')
                        if resp =='S' or resp =='s':
                            conexão.execute('DELETE FROM Registro WHERE ID=?',(delet,))
                            print("\033[1mRegistro deletado com sucesso!\033[0m")
                            retornar()
                            break
                        else:
                            print("\033[1mDados não apagados.\033[0m")
                            retornar()
                            break
                else:
                    print('\033[1mRegistro inexistente.\033[0m')
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
                print('\033[1mNumero ou caractere invalido. Tente  Novamente.\033[0m')
            elif menu2 == '1':
                logo()
                while True:
                    try:
                        alter=int(input("Digite o registro a ser alterado: "))
                    except ValueError as error:
                        logo()
                        print('Valor invalido, precisa ser um numero.')
                    else:
                        break
                while True:
                    with conexão:
                        cursor=conexão.execute("SELECT*FROM Registro WHERE ID=?", (alter,))
                        row=cursor.fetchone()
                        if row is None:
                            logo()
                            input('\033[1mRegistro Inexistente. Pressione ENTER para retornar.\033[0m')
                            break
                        else:
                            print(f'''\033[1mFuncionário a ser alterado: {alter}
    Nome do funcionário: {row[1]} {row[2]}
    Salário: R${row[3]}
    Profissão: {row[4]}\033[0m''')
                            resp=input('\033[1mDigite S ou s se deseja alterar esses dados: \033[0m')
                            if resp =='S' or resp =='s':
                                if row:
                                    while True:
                                        prim_nome=input("\033[1mDigite o novo nome: \033[0m")
                                        if prim_nome.isalpha():
                                            break
                                        else:
                                            logo()
                                            print('\033[1mPrecisa ter apenas letras. Tente novamente.\033[0m')
                                    while True:
                                        seg_nome=input('\033[1mDigite o novo segundo nome: \033[0m')
                                        if seg_nome.isalpha():
                                            break
                                with conexão:
                                    conexão.execute('UPDATE Registro SET Primeiro_nome=?, Segundo_nome=? WHERE ID=?', (prim_nome, seg_nome, alter))
                                    logo()
                                    print("\033[1mRegistro alterado com sucesso!\033[0m")
                                    retornar()
                                    break
                            else:
                                logo()
                                print('\033[1mRegistro não alterado.\033[0m')
                                retornar()
                                break
            elif menu2 == '2':
                logo()
                while True:
                    try:
                        alter=int(input("\033[1mDigite o registro a ser alterado: \033[0m"))
                    except ValueError as error:
                        logo()
                        print('\033[1mValor invalido, precisa ser um numero.\033[0m')
                    else:
                        break
                while True:
                    with conexão:
                        cursor=conexão.execute("SELECT*FROM Registro WHERE ID=?", (alter,))
                        row=cursor.fetchone()
                        if row is None:
                            logo()
                            input('\033[1mRegistro Inexistente. Pressione ENTER para voltar ao menu anterior.\033[0m')
                            break
                        else:
                            print(f'''\033[1mFuncionário a ser alterado: {alter}
    Nome do funcionário: {row[1]} {row[2]}
    Salário: R${row[3]}
    Profissão: {row[4]}\033[0m''')
                            resp=input('\033[1mDigite S ou s se deseja alterar esses dados: \033[0m')
                            if resp =='S' or resp =='s':
                                if row:
                                    while True:                       
                                        try:
                                            salario=int(input("\033[1mDigite o novo salário: \033[0m"))
                                        except ValueError as error:
                                            logo()
                                            print('\033[1mValor invalido, precisa ser um numero.\033[0m')
                                        else:
                                            break
                                    with conexão:
                                        conexão.execute('UPDATE Registro SET Salario=? WHERE ID=?',(salario, alter))
                                        logo()
                                        print("\033[1mRegistro alterado com sucesso!\033[0m")
                                        retornar()
                                        break 
                            else:
                                logo()
                                print('\033[1mRegistro não alterado.\033[0m')
                                retornar()
                                break 
            elif menu2 == '3':
                logo()
                while True:
                    try:
                        alter=int(input("\033[1mDigite o registro a ser alterado: \033[0m"))
                    except ValueError as error:
                        logo()
                        print('\033[1mValor invalido, precisa ser um numero.\033[0m')
                    else:
                        break
                while True:
                    with conexão:
                        cursor=conexão.execute("SELECT*FROM Registro WHERE ID=?", (alter,))
                        row=cursor.fetchone()
                        if row is None:
                            logo()
                            input('\033[1mRegistro Inexistente. Pressione ENTER para voltar ao menu anterior\033[0m')
                            break
                        else:
                            print(f'''\033[1mFuncionário a ser alterado: {alter}
    Nome do funcionário: {row[1]} {row[2]}
    Salário: R${row[3]}
    Profissão: {row[4]}\033[0m''')
                        resp=input('\033[1mDigite S ou s se deseja alterar esses dados: \033[0m')
                        if resp =='S' or resp =='s':
                            if row:
                                while True:    
                                    prof_alt=str(input("\033[1mDigite a nova profissão: \033[0m"))
                                    if prof_alt.isalpha():
                                        break
                                    else:
                                        logo()
                                        print('\033[1mPrecisa ter apenas letras. Tente novamente.\033[0m')
                                with conexão:
                                    conexão.execute('UPDATE Registro SET Profissão=? WHERE ID=?', (prof_alt, alter))
                                    logo()
                                    print("\033[1mRegistro alterado com sucesso!\033[0m")
                                    retornar()
                                    break
                        else:
                            logo()
                            print('\033[1mRegistro não alterado.\033[0m')
                            retornar()
                            break
            else:
                break
    elif menu == '5':
        logo()
        while True:
            nome_add=input("\033[1mDigite o novo nome: \033[0m")
            if nome_add.isalpha():
                break
            else:
                logo()
                print('\033[1mPrecisa ter apenas letras. Tente novamente.\033[0m')
        while True:
            segnome_add=input("\033[1mDigite o novo segundo nome: \033[0m")
            if segnome_add.isalpha():
                break
            else:
                logo()
                print('\033[1mPrecisa ter apenas letras. Tente novamente.\033[0m')
        while True:
                sal_add=input("\033[1mDigite o novo salário: \033[0m")
                if sal_add.isdigit():
                    break
                else:
                    logo()
                    print('\033[1mPrecisa ter apenas números. Tente novamente.\033[0m')
        while True:
            prof_add=input("\033[1mDigite a nova profissão: \033[0m")
            if prof_add.isalpha():
                break
            else:
                logo()
                print('\033[1mPrecisa ter apenas letras. Tente novamente.\033[0m')
        with conexão:
            conexão.execute("INSERT INTO Registro(Primeiro_nome, Segundo_nome, Salario, Profissão) VALUES(?,?,?,?)", (nome_add, segnome_add, sal_add, prof_add))
            print("\033[1mRegistro incluido com sucesso.\033[0m")
            retornar()
    else:
        logo()
        logo()
        print("\033[1mPrograma encerrado.\033[0m")
        print(f'\033[1m{data_atual.strftime("%d/%m/%Y")}\033[0m')
        break
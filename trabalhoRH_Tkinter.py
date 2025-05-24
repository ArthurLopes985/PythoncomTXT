# Empresa= Atlantic
# Programadores:
# Arthur Lopes de Oliveira - RGM: 11241102534
# Bruno da Silva Negy - RGM: 11241102531
# João Vitor da Silva Martins Vaz - RGM: 11241103064
# Data= 04/06/2024
# Programa de RH dos funcionários da empresa Atlantic.
#---------------------------------------------------------------------------------------------------
import sqlite3
from contextlib import closing
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.messagebox import askyesno
from PIL import Image, ImageTk
#--------------------------------------------------------------------------------------------------
def My_Select():
    tree.delete(*tree.get_children())
    tree.place(x=220,y=0) 
    label1.place_forget()
    label2.place_forget()
    label3.place_forget()
    label4.place_forget()
    pesq.place_forget()
    Nome.place_forget()
    Sal.place_forget()
    Prof.place_forget()
    lbl_NN.place_forget()
    lbl_S.place_forget()
    lbl_PR.place_forget()
    Botao_Save.place_forget()
    Botao_Pesquisar.place_forget()
    Botao_Retornar.place_forget()
    Botao_Alterar.place_forget()
    Botao_Exc['state'] = NORMAL
    Botao_Inc['state'] = NORMAL
    Botao_Alt['state'] = NORMAL
    Botao_Pes['state'] = NORMAL
    tree.place(x=220,y=0) 
    label5.place(x=220,y=235)
    label6.place(x=220,y=258)
    with sqlite3.connect("trabalhoRH_TKT_Dados.db") as conexão:
            with closing(conexão.cursor()) as cursor:
                cursor.execute('''select * from Registro''')
                resultado=cursor.fetchall()
                for i in resultado:
                    tree.insert('', END, values=i)
#--------------------------------------------------------------------------------------------------
def My_Inc():
     Nome.delete(0, END)
     tree.place_forget()
     label5.place_forget()
     label6.place_forget()
     Botao_Exc['state'] = DISABLED
     Botao_Alt['state'] = DISABLED
     Botao_Pes['state'] = DISABLED
     label1.place(x=170,y=25)
     label2.place(x=170,y=50)
     label3.place(x=170,y=75)
     Nome.place(x=300,y=25)
     Sal.place(x=300,y=50) 
     Prof.place(x=300,y=75) 
     Botao_Save.place(x=180,y=125)
     Botao_Retornar.place(x=300,y=125)
#----------------------------------------------------------------------------------------------
def Salvar():
    my_name=Nome.get()
    sal=Sal.get()
    prof=Prof.get()
    try: 
        with sqlite3.connect("trabalhoRH_TKT_Dados.db") as conexão:        
            with closing(conexão.cursor()) as cursor:
                flag=False
                for i in my_name:
                    if i.isdigit():
                        flag=True
                for i in sal:
                    if i.isalpha():
                        flag=True
                for i in prof:
                    if i.isdigit():
                        flag=True
                if flag:
                    showinfo(title='Atenção', message='Dados não validos.')
                else:
                    cursor.execute('''insert into Registro (Nome,Salario,Profissao) values (?,?,?)''',(my_name,sal,prof))
                    conexão.commit()
                    showinfo(title='Atenção', message='Registro Incluído!')
    except sqlite3.IntegrityError:
        showinfo(title='Atenção', message='Matrícula Já Existente!')
#------------------------------------------------------------------------------------------------
def My_Exc():
    Botao_Inc['state'] = DISABLED
    Botao_Alt['state'] = DISABLED
    Botao_Pes['state'] = DISABLED
    if not tree.focus():
        showinfo(title='ERRO', message='Selecione um item para Exclusão')
        My_Select()
    else:
        item_selecionado = tree.focus()
        rowid = tree.item(item_selecionado)
        Matr_Exc = (rowid["values"][0])
        with sqlite3.connect("trabalhoRH_TKT_Dados.db") as conexão:
            with closing(conexão.cursor()) as cursor:
                cursor.execute(f'delete from Registro where ID = "{Matr_Exc}"')
                answer = askyesno(title='confirmation', message='Tem certeza que quer apagar esse funcionário?')
                if answer:
                    conexão.commit()
                    tree.delete(item_selecionado)
                    My_Select()
                else:
                    conexão.rollback()
                    My_Select()
#--------------------------------------------------------------------------------------------------
def My_Alt():
     Botao_Exc['state'] = DISABLED
     Botao_Inc['state'] = DISABLED
     Botao_Pes['state'] = DISABLED
     global Matr_Alt
     global Nome_Alt
     global sal_Alt
     global prof_Alt
     Nome.delete(0, END)
     Sal.delete(0, END)
     Prof.delete(0, END)
     if not tree.focus():
        showinfo(title='ERRO', message='Selecione um item para Alteração')
        My_Select()
     else:
        label5.place_forget()
        label6.place_forget()
        item_selecionado = tree.focus()
        rowid = tree.item(item_selecionado)
        Matr_Alt = (rowid["values"][0])
        Nome_Alt = (rowid["values"][1])
        sal_Alt = (rowid["values"][2])
        prof_Alt = (rowid["values"][3])
        lbl_NN.place(x=220,y=230)
        Nome.insert(0, Nome_Alt) 
        Nome.place(x=220,y=255)
        lbl_S.place(x=220,y=280)
        Sal.insert(0, sal_Alt) 
        Sal.place(x=220,y=305)
        lbl_PR.place(x=220,y=330)
        Prof.insert(0, prof_Alt) 
        Prof.place(x=220,y=355)
        Botao_Alterar.place(x=220,y=390)
        Botao_Retornar.place(x=220,y=425)
#---------------------------------------------------------------------------------------
def Alterar():
    Nome_Alt=Nome.get()
    sal_Alt=Sal.get()
    prof_Alt=Prof.get()
    with sqlite3.connect("trabalhoRH_TKT_Dados.db") as conexão:
        with closing(conexão.cursor()) as cursor:
            flag=False
            for i in Nome_Alt:
                if i.isdigit():
                    flag=True
            for i in sal_Alt:
                if i.isalpha():
                    flag=True
            for i in prof_Alt:
                if i.isdigit():
                    flag=True
            if flag:
                showinfo(title='Atenção', message='Dados não validos.')
            else:
                cursor.execute(f'update Registro set Nome = "{Nome_Alt}", Salario = "{sal_Alt}",Profissao = "{prof_Alt}" where ID = "{Matr_Alt}"')
                conexão.commit()
                selected_item = tree.selection()[0]
                tree.item(selected_item, text="blub", values=(Matr_Alt,Nome_Alt, sal_Alt, prof_Alt))
                showinfo(title='Atenção', message='Registro Alterado')
#-----------------------------------------------------------------------------------------------------
def My_Pes():
    tree.delete(*tree.get_children())
    tree.place(x=220,y=0) 
    Botao_Exc['state'] = DISABLED
    Botao_Inc['state'] = DISABLED
    Botao_Alt['state'] = DISABLED
    label4.place(x=220,y=240)
    pesq.place(x=220,y=265) 
    label5.place(x=220,y=350)
    label6.place(x=220,y=370)
    Botao_Pesquisar.place(x=220,y=290)
    Botao_Retornar.place(x=220,y=315)
#------------------------------------------------------------------------------------------------------------
def Pesquisar():
    nompes=pesq.get()
    tree.delete(*tree.get_children())
    with sqlite3.connect("trabalhoRH_TKT_Dados.db") as conexão:
            with closing(conexão.cursor()) as cursor:
                cursor.execute('select * from Registro WHERE Nome LIKE ?', ('%'+ nompes + '%',))
                resultado=cursor.fetchall()
                for i in resultado:
                    tree.insert('', END, values=i)
#-------------------------------------------------------------------------------------------------
Janela = Tk()
Janela.title("Sistema de RH dos funcionários - Atlantic") 
Janela.geometry('1600x900') 
Tit = Label(Janela, text="Selecione uma das opções abaixo", borderwidth=1, relief='solid')
Tit.place(x=1125,y=0)
Tit["font"] = ("Times New Roman", "12", "bold")
Tit["fg"]=("blue")
Tit["bg"]=("white")
Botao_Sel = Button(Janela, text="Relatório Geral",width=15, borderwidth=1, relief='solid')
Botao_Sel["font"] = ("Times New Roman", "10", "bold")
Botao_Sel["bg"]=("white")
Botao_Sel.place(x=1230,y=25)
Botao_Sel['command']=My_Select
#--------------------------------------------------------------------------------------------------
Botao_Inc = Button(Janela, text="Incluir funcionário",width=15, borderwidth=1, relief='solid')
Botao_Inc["bg"]=("white")
Botao_Inc["font"] = ("Times New Roman", "10", "bold")
Botao_Inc.place(x=1230,y=50)
Botao_Inc['command']=My_Inc
label1 = Label (Janela, text = "Entre com o Nome")
label1["font"] = ("Times New Roman", "10", "bold")
Nome = Entry(Janela,width=30, borderwidth=1, relief='solid')
label2 = Label (Janela, text = "Entre com o Salario")
label2["font"] = ("Times New Roman", "10", "bold")
Sal = Entry(Janela,width=30, borderwidth=1, relief='solid')
label3 = Label (Janela, text = "Entre com o Profissão")
label3["font"] = ("Times New Roman", "10", "bold")
Prof = Entry(Janela,width=30, borderwidth=1, relief='solid')
Botao_Save = Button(Janela, text="Incluir funcionário",width=15, borderwidth=1, relief='solid')
Botao_Save["bg"]=("white")
Botao_Save["font"] = ("Times New Roman", "10", "bold")
Botao_Save['command']=Salvar
Botao_Retornar = Button(Janela, text="Retornar",width=15,command=My_Select, borderwidth=1, relief='solid')
Botao_Retornar["font"] = ("Times New Roman", "10", "bold")
#--------------------------------------------------------------------------------------------------
Botao_Exc = Button(Janela, text="Excluir Funcionário",width=15, borderwidth=1, relief='solid')
Botao_Exc["font"] = ("Times New Roman", "10", "bold")
Botao_Exc["bg"]=("white")
Botao_Exc.place(x=1230,y=75)
Botao_Exc['command']=My_Exc
#--------------------------------------------------------------------------------------------------
Botao_Alt = Button(Janela, text="Alterar Informações",width=15, borderwidth=1, relief='solid')
Botao_Alt["font"] = ("Times New Roman", "10", "bold")
Botao_Alt["bg"]=("white")
Botao_Alt.place(x=1230,y=100)
lbl_NN = Label (Janela, text = "Entre com o novo nome")
lbl_S = Label (Janela, text = "Entre com o novo salário")
lbl_PR = Label (Janela, text = "Entre com a nova profissão")
Botao_Alt['command']=My_Alt
Botao_Alterar = Button(Janela, text="Salvar Alterações",width=15, borderwidth=1, relief='solid')
Botao_Alterar["bg"]=("white")
Botao_Alterar['command']=Alterar
Botao_Retornar = Button(Janela, text="Retornar",width=15, borderwidth=1, relief='solid')
Botao_Retornar["bg"]=("white")
Botao_Retornar['command']=My_Select
#-------------------------------------------------------------------------------------------------
Botao_Pes = Button(Janela, text="Pesquisa por nome",width=15, borderwidth=1, relief='solid')
Botao_Pes["font"] = ("Times New Roman", "10", "bold")
Botao_Pes["bg"]=("white")
Botao_Pes.place(x=1230,y=125)
Botao_Pes['command']=My_Pes
label4 = Label (Janela, text = "Entre com o nome a ser pesquisado")
pesq = Entry(Janela,width=30, borderwidth=1, relief='solid')
Botao_Pesquisar = Button(Janela, text="Pesquisar",width=15, borderwidth=1, relief='solid')
Botao_Pesquisar["bg"]=("white")
Botao_Pesquisar['command']=Pesquisar
Botao_Retornar = Button(Janela, text="Retornar",width=15, borderwidth=1, relief='solid')
Botao_Retornar["bg"]=("white")
Botao_Retornar['command']=My_Select
#---------------------------------------------------------------------------------------------------------
Sair= Button(Janela, text="Sair da Aplicação", command=Janela.destroy,width=15, borderwidth=1, relief='solid')
Sair["font"] = ("Times New Roman", "10", "bold")
Sair["bg"]=("white")
Sair.place(x=1230,y=150)
image = Image.open("Logo.png")
resize_image = image.resize((156, 100))
img = ImageTk.PhotoImage(resize_image)
Logo = Label(image=img, borderwidth=1, relief='solid')
Logo.image = img
Logo.place(x=0,y=0)
columns = ('ID', 'Nome', 'Salario', 'Profissao')
tree = ttk.Treeview(Janela, columns=columns, show='headings')
tree.heading('ID', text='ID')
tree.heading('Nome', text='Nome do Funcionário')
tree.heading('Salario', text='Salário')
tree.heading('Profissao', text='Profissão')
label5 = Label (Janela, text = "Role a tela para baixo com o Mouse", borderwidth=1, relief='solid') 
label5["font"] = ("Times New Roman","10","bold",)
label5["fg"]=("blue")
label5["bg"]=("white")
label6 = Label (Janela, text = "Selecione o registro para Alterar/Excluir", borderwidth=1, relief='solid')
label6["font"] = ("Times New Roman","10","bold",)
label6["fg"]=("red")
label6["bg"]=("white")
Janela.mainloop()
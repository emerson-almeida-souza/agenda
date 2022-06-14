import sqlite3
from sqlite3 import Error
import os

#CRIANDO CONEXÃO
def conexaoBanco():
    caminho = "C:\\Python\\Banco\\agenda.db"
    con=None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon=conexaoBanco()

def query(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    
    finally:
        print("Operacao realizada comn sucesso")
        os.system("pause")

def consultar(conexao, sql):
        c = conexao.cursor()
        c.execute(sql)
        res = c.fetchall()
        return res

def MenuInserir():
    os.system("cls")
    vnome = input("Digite o nome: ")
    vtelefone = input("Digite o telefone: ")
    vemail = input("Digite o email: ")
    vsql="INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO) VALUES('"+vnome+"', '"+vtelefone+"', '"+vemail+"')"
    query(vcon, vsql)

def MenuDeletar():
    os.system("cls")
    vid = input("Digite o ID do registro a ser deletado: ")
    vsql="DELETE FROM tb_contatos WHERE N_IDCONTATO = '"+vid+"'"
    query(vcon, vsql)

def MenuAtualizar():
    os.system("cls")
    vid = input("Digite o ID do registro a ser atualizado: ")

    r = consultar(vcon, "SELECT * FROM tb_contatos WHERE N_IDCONTATO = '"+vid+"'")
    rnome = r[0][1] #nome
    rtelefone = r[0][2] #telefone
    remail = r[0][3] #email

    vnome = input("Digite o nome: ")
    vtelefone = input("Digite o telefone: ")
    vemail = input("Digite o email: ")

    #Se não for digitado nada, ele recebe o mesmo nome que ele tinha antes
    if(len(vnome) == 0):
        vnome = rnome

    if(len(vtelefone) == 0):
        vtelefone = rtelefone

    if(len(vemail) == 0):
        vemail = remail
    
    vsql = "UPDATE tb_contatos SET T_NOMECONTATO='"+vnome+"', T_TELEFONECONTATO = '"+vtelefone+"', T_EMAILCONTATO = '"+vemail+"' WHERE N_IDCONTATO = '"+vid+"'"
    query(vcon, vsql)

def MenuConsultar():
    vsql = "SELECT * FROM tb_contatos"
    res = consultar(vcon, vsql)

    for r in res:
        print("ID: {}\n Nome: {}\n Telefone: {}\n E-mail: {}\n".format(r[0], r[1], r[2], r[3]))
    os.system("pause")
    print("Fim da lista")

def MenuConsultarNomes():
    vnome=input("Digite o nome: ")
    vsql = "SELECT * FROM tb_contatos WHERE T_NOMECONTATO LIKE '%"+vnome+"%'"
    res = consultar(vcon, vsql)

    for r in res:
        print("ID: {}\n Nome: {}\n Telefone: {}\n E-mail: {}\n".format(r[0], r[1], r[2], r[3]))
    os.system("pause")
    print("Fim da lista")

def menuPrincipal():
    os.system("cls")
    print("1 - Inserir novo registro")
    print("2 - Deletar registro")
    print("3 - Atualizar registro")
    print("4 - Consultar registros")
    print("5 - Consultar registro por Nome")
    print("6 - Sair")

opc = 0
while opc != 6:
    menuPrincipal()
    opc = int(input("Digite uma opcao: "))

    if opc == 1:
        MenuInserir()
    elif opc == 2:
        MenuDeletar()
    elif opc == 3:
        MenuAtualizar()
    elif opc == 4:
        MenuConsultar()
    elif opc == 5:
        MenuConsultarNomes()
    elif opc == 6:
        os.system("cls")
        print("Programa finalizado")
    else:
        os.system("cls")
        print("Opção invalida")
        os.system("pause")

vcon.close()
os.system("pause")


        
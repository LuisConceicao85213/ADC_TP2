import pickle
""""
Importa o Ficheiro Pickle

e importa também variaveis
"""

from clientes import nome_ficheiro_lista_de_clientes
from faturas import nome_ficheiro_lista_de_faturas

from veiculos import nome_ficheiro_lista_de_veiculos

def carrega_as_listas_dos_ficheiros():
    """
    Carrega as litas do ficheiro para as variaveis
    
    :return: os valores de cada ficheiro
    :rtype: list
    """

    lista_de_veiculos = le_de_ficheiro(nome_ficheiro_lista_de_veiculos)
    lista_de_clientes = le_de_ficheiro(nome_ficheiro_lista_de_clientes)
    lista_de_faturas = le_de_ficheiro(nome_ficheiro_lista_de_faturas)
    
    return  lista_de_veiculos, lista_de_clientes, lista_de_faturas

def guarda_as_listas_em_ficheiros(lista_de_veiculos, lista_de_clientes, lista_de_faturas):
    """Guarda as listas no ficheiro

    :param lista_de_clientes: lista com todos os clientes
    :param type: list
    :param lista_de_veiculos: lista com todos os veiculos
    :param type: list
    :param lista_de_faturas: lista com todos as faturas
    :param type: list
    """

    op = input("Os dados nos ficheiros serão sobrepostos. Continuar (s/N)?")
    if op in ['s', 'S']:
        guarda_em_ficheiro(nome_ficheiro_lista_de_veiculos, lista_de_veiculos)
        guarda_em_ficheiro(nome_ficheiro_lista_de_clientes, lista_de_clientes)
        guarda_em_ficheiro(nome_ficheiro_lista_de_faturas, lista_de_faturas)
    else:
        print("Gravação cancelada...")
        
def guarda_em_ficheiro(nome_do_ficheiro, dados):
    """Guarda os dados recebidos num ficheiro

    :param nome_do_ficheiro: nome do ficheiro onde vai guardar os dados
    :param type: list
    :param dados: dados a serem guardados
    :param type: list
    """

    with open(nome_do_ficheiro, "wb") as f:
        pickle.dump(dados, f)
        
def le_de_ficheiro(nome_ficheiro):
    """Lê os dados de um ficheiro

    :param nome_ficheiro: nome do ficheiro onde estao os dados
    :para type: list
    :return: o que leu do ficheiro (depende dos dados guardados)
    """

    with open(nome_ficheiro, "rb") as f:
        return pickle.load(f)

# TODO: Copie para aqui o código de cada uma das funções nos
# ficheiros com o nome io_ficheiros*.py e faça um commit de cada vez
# Quando este ficheiro estiver completo com todas as suas funções,
# deve ser o unico ficheiro io_ficheiros.py existente, deve apagar
# todos os outros ficheiros io_ficheiros-*.py, e inclusive estes comentários

# ...

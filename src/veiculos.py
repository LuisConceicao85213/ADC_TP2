from io_terminal import imprime_lista

nome_ficheiro_lista_de_veiculos = "lista_de_veiculos.pk"


def cria_novo_veiculo():
    """Pede ao utilizador para introduzir um novo veiculo

    :return: dicionario com um veiculo na forma
        {"marca": <<marca>>, "matricula": <<matricula>>, ...}
    """

    marca = input("marca? ")
    matricula = input("matricula? ").upper()
    # TODO: Pedir o resto dos dados do veiculo, e não esquecer de os guardar no dicionario
    # ...

    veiculo = {"marca": marca,
               "matricula": matricula}

    return veiculo

def imprime_lista_de_veiculos(lista_de_veiculos):
    """Faz uma tabela com a lista de veiculos
    
    :param lista_de_veiculos: lista com todos os veiculos
    :param type: list
    """

    imprime_lista(cabecalho="Lista de Veiculos", lista=lista_de_veiculos)

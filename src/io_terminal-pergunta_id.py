def pergunta_id(questao, lista, mostra_lista=False):
    """
    :param questao: Pergunta
    :ParaType:Str
    :param lista: É uma lista com um cabeçalho
    :ParaType:Int
    :param mostra_lista: Serve para imprimir lista na interface
    :ParaType:Bool
    :return: id filtrado
    """

    if mostra_lista:
        imprime_lista(cabecalho="", lista=lista)

    while True:
        id = int(input(questao))
        if 0 <= id < len(lista):
            return id
        else:
            print(f"id inexistente. Tente de novo. Valores admitidos {0} - {len(lista)}")


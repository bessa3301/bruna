import json

# Dados de exemplo -- sem conexao com database
with open("contatos.json") as contatos_arquivo:
    contatos = json.load(contatos_arquivo)


# Contatos dentro do arquivo .json
# print(contatos)


def saveToJson(data):
    """
    Recebe os dados de addContact.
    Mantem as convencoes SOLID para qualidade de codigo.
    Salva os dados no arquivo.
    """

    # Lendo informacoes
    with open("contatos.json", "r+") as arquivo:
        dic = json.load(arquivo)
        dic.append(data)
        arquivo.seek(0)
        json.dump(dic, arquivo)

    # limpando infos nao necessarias para proxima operacao
    with open("contatos.json", "w") as arquivo:
        json.dump("", arquivo)

    # adicionando novos dados
    with open("contatos.json", "r+") as arquivo:
        json.dump(dic, arquivo)

    pass


"""
adicionar contatos.
nome nao estar vazio.
telefones devem ser contidos em um array.
"""


def addContact(name, phones, email, instagram):

    # checando se nome esta vazio
    if name == "":
        print(f"nome nao pode estar vazio dumass")
        pass
    else:

        # objeto sendo tratado
        data = []

        # adicionando nome
        data.append(name)

        # adicionando telefone para cada telefone passado dentro do array
        data_telefone = []

        for phone in phones:
            data_telefone.append(phone)
            pass

        # adicionando telefone ao objeto data
        data.append(data_telefone)

        # adicionando email e usuario do instagram
        data.append(email)
        data.append(instagram)

        saveToJson(data)

        print(data)
        pass

    pass


addContact("testing", [123, 123], "email@something.ru", "@someUser")

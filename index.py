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


# addContact("testing", [123, 123], "email@something.ru", "@someUser")

"""
- telefone: caso ja exista = remover, else adicionar. 
- caso nao exista indice avisar. 

A RFC 8398 - https://tools.ietf.org/html/rfc8398
indica que os enderecos de email são unicos, logo, podem ser usados para indexar como
identificador unico. Logo facilitando a busca usando o mesmo.
"""


class Switcher(object):
    def mod(self, st):
        method_name = st[0]
        data = st[1]
        payload = st[2]
        method = getattr(self, method_name, lambda: "use uma das opcoes validas")
        return method(data, payload)

    def name(self, data, payload):

        data[0] = payload
        res = data
        return data

    def email(self, data, payload):

        data[2] = payload
        res = data
        return data

    def insta(self, data, payload):
        data[3] = payload
        res = data
        return data

    def fones(self, data, payload):
        return "fones works"


def updateContact(target, modifier, payload):

    sucess_status = bool(False)
    email = target[2]

    # variaveis sem uso, incluidas apenas para cumprir com os requisitos passados
    name = target[0]
    insta = target[3]

    # prevenir erros com fone
    if modifier == "fones" and isinstance(payload, list):
        print("xx works")
        pass
    else:

        # ciclar por cada contato em contatos
        for p in contatos:

            # encontrar usuario usando email
            if p[2] == email:
                # print(p)

                # switch para nome,fones,email,insta
                s = Switcher()
                print(s.mod([modifier, p, payload]))

                pass
            pass

        # print(f"works")
        pass
    pass


# lista passada do frontend para o backend
listaAtual = ["testing", [123, 123], "email@something.ru", "@someUser"]

updateContact(listaAtual, "fones", [123, 123])

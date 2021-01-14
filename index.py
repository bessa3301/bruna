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
Como adicionar contatos?

- Escolha um nome, array de telefones, email e instagram
- chame a funcao addContact com os parametros nessa ordem
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


# exemplo adicionar contato:
# addContact("testing", [123, 123], "email@something.ru", "@someUser")

"""
A RFC 8398 - https://tools.ietf.org/html/rfc8398
indica que os enderecos de email são unicos, logo, podem ser usados para indexar como
identificador unico. Logo facilitando a busca usando o mesmo.

Alterações no documento podem ser encontradas no arquivo contatos.json
"""

# classe switcher que recebe argumentos para seus metodos
class Switcher(object):
    def mod(self, st):
        method_name = st[0]
        data = st[1]
        payload = st[2]
        method = getattr(self, method_name, lambda: "use uma das opcoes validas")
        return method(data, payload)

    # nome
    def name(self, data, payload):

        data[0] = payload
        res = data
        return data

    # email
    def email(self, data, payload):

        data[2] = payload
        res = data
        return data

    # instagram
    def insta(self, data, payload):
        data[3] = payload
        res = data
        return data

    # telefones
    def fones(self, data, payload):

        if isinstance(payload, list):

            # esta parte e mais complexa, aqui estou comparando simetricamente a diferenca entre
            # dois SETS e retornando os valores que nao são iguais.
            data[1] = list(set(payload).symmetric_difference(set(data[1])))
            return data

        else:
            return "Telefone espera uma lista como argumento (array)"

    pass


# atualizar json
def updateJson(data, p):

    """
    Recebe os dados de updateContact.
    Mantem as convencoes SOLID para qualidade de codigo.
    !! Remove o registro existente.
    Salva os dados novos no arquivo.
    """

    # Lendo informacoes
    with open("contatos.json", "r+") as arquivo:
        dic = json.load(arquivo)
        # @!
        dic.pop(p)
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


# atualizar contato
def updateContact(target, modifier, payload):

    sucess_status = bool(False)
    email = target[2]

    # variaveis sem uso, incluidas apenas para cumprir com os requisitos passados
    name = target[0]
    insta = target[3]

    foundState = False
    positionInArray = 0

    # ciclar por cada contato em contatos
    for p in contatos:

        # encontrar usuario usando email
        if p[2] == email:
            # print(p)
            foundState = True

            # switch para nome,fones,email,insta
            s = Switcher()
            # retornando para o usuario o que a funcao retornou
            data = s.mod([modifier, p, payload])
            updateJson(data, positionInArray)
            print(data)
        pass
        positionInArray = positionInArray + 1
    pass

    # chamando statement fora do loop para economizar memoria
    if foundState != True:
        print(f"Usuario Não Encontrado")


pass


"""
Como atualizar dados?

- popule o objeto suaLista com os dados do cliente que gostaria de editar
- use as funcoes abaixo, removendo o comentario, ja que elas ja comtem os parametros.
"""


# lista passada do frontend para o backend
# EXEMPLO:
# listaAtual = ["testing", [123, 123], "t@t.com", "@someUser"]
suaLista = ["nome", [12, 34], "a@b.ru", "@algo"]

# atualizar nome
# updateContact(listaAtual, "name", "escolha um nome")

# atualizar email
# updateContact(listaAtual, "email", "email@exemplo.com")

# atualizar fones
# updateContact(listaAtual, "fones", [123, 456])

# atualizar insta
# updateContact(listaAtual, "insta", "@exemplo")

import json

# Dados de exemplo -- sem conexao com database
with open("contatos.json") as contatos_arquivo:
    contatos = json.load(contatos_arquivo)


# Contatos dentro do arquivo .json
# print(contatos)

"""
> sua funcao deve criar um novo contato, e retornar o mesmo. 

| 0 | nome |
| 1 | lista de telefones |
| 2 | email |
| 3 | instagram |

x deve receber os 4 parametros acima. 
> telefones devem estar dentro de um array. 
> nome nao pode ser vazio.
"""


def addContact(name, phones, email, instagram):

    # checando se nome esta vazio
    if name == "" or name == null or name == undefined:
        print(f"nome nao pode estar vazio dumass")
        pass
    else:

        # telefones dentro de uma lista
        data_telefone = []

        for phone in phones:
            data_telefone.append()
            pass

        print("works")
        pass

    pass


addContact("", [123, 123], "", "")

<img src="./kodsystemi.png" height="200" width="200" />

### kod#13265
|Категория|Содержание|
|---------|----------|
|Идиома|португальский - Бразилия|
|Чтобы|Бруна|

<br>
<br>

# Objetivo:

Voce e um dos desenvolvedores do "contatinhosAPP" que desenvolvera funcoes que interagem com o frontend proposto;
Estrutura existente:

- informações de cada contato sao armazenadas em uma lista
- unica info obrigatoria é nome. outros = [fone1,fone-n (nao especifica quantos e o limite),email,instagram]
- telefones sao armazenados em outra lista
- a lista para cada contato segue o padrao abaixo:
#### ['nome',['fone1','fone-n'],'email','usuario instagram']

## Tarefas:

| indice na lista | informacao |
| --------------- | ---------- |
| 0 | nome |
| 1 | lista de telefones |
| 2 | email |
| 3 | instagram |

- [ ] criar novo contato; 
> sua funcao deve criar um novo contato, e retornar o mesmo. deve receber os 4 parametros acima. telefones devem estar dentro de um array. nome nao pode ser vazio.

- [ ] atualizar informações de um contato; 
> Só e permitido atualizar uma informação por function call. è passado a lista atual para busca, e a informação nova. salvar na memoria informacoes [ nome , email , instagram ]. telefone: caso ja exista = remover, else adicionar. caso nao exista indice avisar. funcao deve retornar boolean se a operação foi bem sucedida ou não

### Python version 3.8x
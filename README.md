# Atividade Prática: Manipulação de Listas e Investigação de Identidade em Python

Este repositório contém a resolução da atividade prática de manipulação de estruturas de dados (listas) desenvolvida em ambiente Google Colab para a disciplina de Estrutura de Dados / Algoritmos.

## 👥 Integrantes da Dupla
* **Integrante 1:** [Seu Nome Completo] - [Seu RGM/Matrícula]
* **Integrante 2:** [Nome do seu Colega] - [RGM/Matrícula do Colega]

## 🎯 Objetivo da Atividade
O objetivo principal é criar uma lista inicial em Python e realizar uma série de operações sequenciais de manipulação, utilizando a função nativa `id()` para investigar a identidade e o comportamento dos objetos na memória, compreendendo os conceitos de **mutabilidade** e **referência**.

As operações executadas foram:
1. Exibir a lista inicial e seu `id()`;
2. Adicionar um elemento ao final com `append()`;
3. Inserir um elemento em uma posição específica com `insert()`;
4. Remover um elemento pelo valor utilizando `remove()`;
5. Remover um elemento pela posição utilizando `pop()`;
6. Alterar o valor de um elemento existente;
7. Limpar todos os elementos utilizando `clear()`.

---

## 💻 Código Desenvolvido

```python
def mostrar_estado(nome_operacao, lst):
    print(f'=== {nome_operacao} ===')
    print(f'Conteúdo atual da lista: {lst}')
    print(f'id() da lista: {id(lst)}')
    print('Detalhes dos elementos (Índice | Valor | id()):')
    for i, val in enumerate(lst):
        print(f'  [{i}] -> Valor: {val} | id(): {id(val)}')
    print('-' * 40 + '\n')

# Ponto de partida
lista = [10, 20, 30]
mostrar_estado('1. Lista Inicial', lista)

# Operações
lista.append(40)
mostrar_estado('2. Operação append(40)', lista)

lista.insert(1, 15)  
mostrar_estado('3. Operação insert(1, 15)', lista)

lista.remove(20)  
mostrar_estado('4. Operação remove(20)', lista)

lista.pop(2)  
mostrar_estado('5. Operação pop(2)', lista)

lista[0] = 99  
mostrar_estado('6. Alteração de valor lista[0] = 99', lista)

lista.clear()
mostrar_estado('7. Operação clear()', lista)
```

---

## 📊 Análise dos Resultados

### a) O id() da lista mudou durante as operações? O que isso indica?
**Resposta:** Não, o `id()` da lista permaneceu exatamente o mesmo em todas as etapas. Isso indica que a lista é o mesmo objeto na memória do início ao fim; suas propriedades mudaram, mas sua identidade como contêiner continuou a mesma.

### b) O que aconteceu com os elementos quando novos valores foram adicionados?
**Resposta:** Quando novos elementos foram adicionados (`append` e `insert`), a lista expandiu sua estrutura interna para guardar os `id()` desses novos objetos. Os elementos que já estavam na lista e ficaram depois do local de inserção tiveram seus índices deslocados, mas mantiveram seus `id()` originais.

### c) O que acontece com a referência de um elemento quando ele é removido da lista?
**Resposta:** A referência (o ponteiro de memória) deixa de existir dentro da lista. Se esse objeto não estiver guardado em nenhuma outra variável fora da lista, o coletor de lixo do Python (*Garbage Collector*) apaga o valor da memória para liberar espaço.

### d) Ao alterar um elemento da lista, o id() desse elemento permaneceu igual? Explique o resultado observado.
**Resposta:** Não, o `id()` mudou. Isso acontece porque números inteiros (`int`) são **imutáveis** em Python. Não é possível alterar o valor de um inteiro "por dentro". Ao fazer `lista[0] = 99`, o Python descarta a referência ao número antigo e faz o índice `0` apontar para o `id()` do novo objeto criado (o número `99`).

### e) Por que dizemos que uma lista em Python é um objeto mutável?
**Resposta:** Porque o seu conteúdo, tamanho e ordem podem ser alterados diretamente no mesmo endereço de memória, permitindo modificar o objeto sem a necessidade de criar uma nova lista (mantendo o mesmo `id()`).

### f) Qual é a diferença entre alterar o conteúdo de uma lista e criar uma nova lista?
**Resposta:** Alterar o conteúdo atualiza a lista existente no mesmo espaço de memória (mantém o `id()`), afetando todas as variáveis que apontam para ela. Criar uma nova lista (ex: `lista = [...]`) aloca um espaço inédito na memória, gerando um `id()` completamente novo e rompendo o vínculo com os dados antigos.

---

## 🛠️ Tecnologias Utilizadas
* **Python 3**
* **Google Colab**


def mostrar_estado(nome_operacao, lst):
  print(f'=== {nome_operacao} ===')
  print(f'Conteúdo atual da lista: {lst}')
  print(f'id() da lista: {id(lst)}')
  print('Detalhes dos elementos (Índice | Valor | id()):')
  for i, val in enumerate(lst):
    print(f'  [{i}] -> Valor: {val} | id(): {id(val)}')
  print('-' * 40 + '\n')



lista = [10, 20, 30]
mostrar_estado('1. Lista Inicial', lista)


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



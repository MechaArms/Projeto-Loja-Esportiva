listaProdutos = []
codigoProdutos = []
listaPreços = []

from leitoraListaProdutos import setProdutos, setCodigos, setPrecos

listaProdutos = setProdutos()
codigoProdutos = setCodigos()
listaPreços = setPrecos()

n_cupom = []
lista = []
pedido = []
und = []
qt = []
prod = []
total_fecha_caixa = []


def getDados():
    cont = 1
    n_cupom.append(0)
    print('\n' * 2)
    print('--Lista de Compras--')
    print('\nDigite o codigo do produto para inserir na nota de compra \nou digite "0" [Zero] para fechar a lista de compras\n')
    print('Cupom fiscal nº ',len(n_cupom))
    while True:
        print(f'Produto {cont}',end='')
        produto = int(input(': '))
        while produto not in codigoProdutos:
            if produto == 0:
                break
            else:
                print('[Numero Inválido]')
                print(f'Produto {cont}',end='')
                produto = int(input(': '))
        if produto == 0:
            break
        else:
            lista.append(produto) #codigo produto
            indice = codigoProdutos.index(produto)
            quantidade = int(input('Quantidade: '))
            if quantidade <= 0:
                print('[Numero Inválido]')
                print(f'O produto {cont} foi cancelado!')
                lista.pop()
            else:
                valor_unitario = listaPreços[indice]
                valor_pedido = listaPreços[indice] * quantidade
                und.append(valor_unitario)
                pedido.append(valor_pedido) #valor total
                qt.append(quantidade) #quantidade
                prod.append(listaProdutos[indice]) #descrição produto
        print('')
        cont += 1
    setDados(lista,prod,qt,und,pedido)


def setDados(lista,prod,qt,und,pedido): #impressão tela
    print('\n' * 2)
    print('{:^50}'.format('CAIXA LIVRE - VENDA'))
    print('{:<5}{:>7}{:>15}{:>6}{:>10}{:>13}'.format('Item','Codigo','Nome','Qt','Val Unit','Val Item'))
    print('{:<5}{:>7}{:>15}{:>6}{:>10}{:>13}'.format('-'*4,'-'*6,'-'*13,'-'*2,'-'*8,'-'*8))

    for i in range(len(lista)):
        print('{:>4}{:>8}{:>15}{:>6}{:>10.2f}{:>13.2f}'.format(i+1,lista[i],prod[i],qt[i],und[i],pedido[i]))

    total = sum(pedido)
    print('{:<10}{:>13}'.format('-'*43,'-'*8,))
    print('{:>43}{:>13.2f}'.format('Total R$',total))
    total_fecha_caixa.append(total) #adicionando o valor total da nota para fechar o caixa
    print('\n'*2)

    #confirma compra
    confirmaLista(total) 
        

def confirmaLista(total):
    confirmarListaCompra = int(input('\nDeseja finalizar a lista ou cancelar um item da lista? \n [finalizar = 0, cancelar item = 1, cancelar nota = 9]: '))
    if confirmarListaCompra == 0:
        print('\nLista de compras concluida!\n')
        #troco
        troco = pagamento(total)
        print(f'\nO valor do troco é de: R$ {troco:.2f}')
        #limpeza da lista de compra e abertura de uma nova
        deleteCupom()
        checkNovoCupom() 
    elif confirmarListaCompra == 1:
        cancelamentoItem()
    elif confirmarListaCompra == 9:
        print('O cupom nº ',len(n_cupom),' foi cancelado!')
        total_fecha_caixa[-1] = 0 #zera a nota atual
        deleteCupom()
        checkNovoCupom()
    else:
        print('[Numero Inválido]')
        confirmaLista()


def pagamento(total):
    valorPago = float(input('Digite o valor a pagar: R$ '))
    print(f'\nO Valor pago é de: R$ {valorPago:.2f}')
    troco = valorPago - total
    return troco


def checkNovoCupom(): #pergunta novo cupom ou fechamento
    perg = int(input('\nDeseja fechar o caixa? \n[sim = 1 , não = 2]: '))
    if perg == 1:
        fechamento(total_fecha_caixa)
    elif perg == 2:
        getDados()
    else:
        print('[Numero Inválido]')
        while perg < 1 or perg > 2:
            perg = int(input('\nDeseja fechar o caixa? \n[sim = 1 , não = 2]: '))
            if perg == 1:
                fechamento(total_fecha_caixa)
            elif perg == 2:
                getDados()
            else:
                continue

                
def deleteCupom():
    lista.clear()
    prod.clear()
    qt.clear()
    und.clear()
    pedido.clear()


def cancelamentoItem():
    checkLista = int(input('Digite o numero do item na lista que deseja excluir: '))
    checkLista -= 1
    if checkLista > len(lista) or checkLista < 0:
        print('[Numero Inválido]')
        cancelamentoItem()
    else:
        lista.pop(checkLista)
        prod.pop(checkLista)
        qt.pop(checkLista)
        und.pop(checkLista)
        pedido.pop(checkLista)
    setDados(lista,prod,qt,und,pedido)


def fechamento(total_fecha_caixa): #fechamento caixa
    print('\n' * 2)
    print('--Fechamento de Caixa--')
    print('\nQuantidade de cupons emitidos: ', len(total_fecha_caixa))
    for i in range(len(total_fecha_caixa)):
        if total_fecha_caixa[i] == 0:
            print(f'Cupom nº {i+1} foi cancelado')
        else:
            print(f'Cupom nº {i+1} R$ {total_fecha_caixa[i]:.2f}')
    print('Total R$ {:<10.2f}'.format(sum(total_fecha_caixa)))

getDados() #executando o codigo


codigoProdutos = []
listaProdutos = []
listaPrecos = []

def getListaProdutos():
    with open("C:/Users/Informatica/Desktop/python/ListagemDeMercadorias.txt", 'r',encoding ="utf-8") as arquivo: # abrindo o arquivo txt do exercicio é necessario criar o arquivo do enunciado
        for i in range(10):
            produto = arquivo.readline() # lê a linha do texto
            produto = produto.replace(' ','') #remove os espaços em branco
            produto = produto.replace('\t','') #remove os espaços em branco por tabulação [TAB]
            produto = produto.replace('\n','') #remove os espaços em paragrafo [ENTER]
            
            cd = int(produto[0:3]) # busca apenas os 3 primeiros numeros e os transforma em inteiro
                        
            pr = float(produto[-6:]) # busca apenas os 6 ultimos numeros e os transforma em inteiro
            
            np = produto[-22:-6] # busca do inicio ao meio dos itens
            realNp = np[3:] # remove os 3 primeiros (os codigos)

            codigoProdutos.append(cd)
            listaPrecos.append(pr)
            listaProdutos.append(realNp)
            
getListaProdutos() # roda o codigo

#teste      
#print(codigoProdutos)
#print(listaPrecos)
#print(listaProdutos)

def setCodigos():
    return codigoProdutos

def setPrecos():
    return listaPrecos

def setProdutos():
    return listaProdutos
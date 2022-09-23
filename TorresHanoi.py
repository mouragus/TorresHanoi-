from stack import Pilha

def pega_pilha(nome, a, b, c) -> Pilha:
    if nome == 'a':
        return a 
    elif nome == 'b':
        return b
    else: 
        return c

def move(orig, dest, a ,b, c):
    pilha_o = pega_pilha(orig, a, b, c)
    pilha_d = pega_pilha(dest, a, b, c)
    
    #Possiveis Erros 
    if orig == dest:
        print("Movimento Inválido!")
        return False
    elif pilha_o.isEmpty():
        print("Movimento Inválido!")
        return False
    elif not pilha_d.isEmpty and pilha_o.peek() > pilha_d.peek():
        print("Movimento Inválido!")
        return False

    #Movimentação 
    info = pilha_o.pop()
    pilha_d.put(info)
    print(orig, "->", dest, "disco:", info)
    return True 

#Hastes
a = Pilha ()
b = Pilha ()
c = Pilha ()

#Discos
a.put(3)
a.put(2)
a.put(1)

contador = 0

while contador < 3: 
    origem = input("Pilha Origem: ")
    destino = input("Pilha Destino: ")

    if move(origem, destino,a ,b, c) == True:
        if destino == 'c':
            contador = contador + 1
        elif origem ==  'c':
            contador = contador - 1
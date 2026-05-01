#ex 1
import random

def rolar_dados(qtd):
    lista = []
    
    for i in range(qtd):
        dado = random.randint(1, 6)
        lista.append(dado)
    
    return lista
    
#ex 2

def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    valor = dados_rolados[dado_para_guardar]
    
    nova_rolados = []
    for i in range(len(dados_rolados)):
        if i != dado_para_guardar:
            nova_rolados.append(dados_rolados[i])
    
    novo_estoque = dados_no_estoque + [valor]
    
    return [nova_rolados, novo_estoque]

#ex 3

def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    valor = dados_no_estoque[dado_para_remover]
    
    novo_estoque = []
    for i in range(len(dados_no_estoque)):
        if i != dado_para_remover:
            novo_estoque.append(dados_no_estoque[i])
    
    novo_rolados = dados_rolados + [valor]
    
    return [novo_rolados, novo_estoque]

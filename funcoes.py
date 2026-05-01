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

#ex 4

def calcula_pontos_regra_simples(faces):
    dicionario = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for numero in faces:
        if numero == 1:
            dicionario[1] += 1
        elif numero == 2:
            dicionario[2] += 2
        elif numero == 3:
            dicionario[3] += 3
        elif numero == 4:
            dicionario[4] += 4
        elif numero == 5:
            dicionario[5] += 5
        elif numero == 6:
            dicionario[6] += 6
    return dicionario

#ex 5

def calcula_pontos_soma(faces):
    soma = 0
    for i in faces:
        soma += i
    return soma

#ex 6

def calcula_pontos_sequencia_baixa(faces):
    for i in faces:
        if 1 in faces and 2 in faces and 3 in faces and 4 in faces:
            return 15
        elif 2 in faces and 3 in faces and 4 in faces and 5 in faces:
            return 15
        elif 3 in faces and 4 in faces and 5 in faces and 6 in faces:
            return 15
        else:
            return 0

#ex 7

def calcula_pontos_sequencia_alta(faces):
    for i in faces:
        if 1 in faces and 2 in faces and 3 in faces and 4 in faces and 5 in faces:
            return 30
        elif 2 in faces and 3 in faces and 4 in faces and 5 in faces and 6 in faces:
            return 30
        else:
            return 0
#ex 8

def calcula_pontos_full_house(faces):
    contagem = {}
    for numero in faces:
        if numero in contagem:
            contagem[numero] += 1
        else:
            contagem[numero] = 1
    valores = contagem.values()
    soma = 0
    for i in faces:
        soma += i
    if 3 in valores and 2 in valores:
        return soma
    else:
        return 0

#ex 9

def calcula_pontos_quadra(faces):
    contagem = {}
    for numero in faces:
        if numero in contagem:
            contagem[numero] += 1
        else:
            contagem[numero] = 1
    valores = contagem.values()
    soma = 0
    for i in faces:
        soma += i
    for quantidade in contagem.values():
        if quantidade >= 4:
            return soma
    
    return 0

#ex 10

def calcula_pontos_quina(faces):
    contagem = {}
    for numero in faces:
        if numero in contagem:
            contagem[numero] += 1
        else:
            contagem[numero] = 1
    valores = contagem.values()
    for quantidade in contagem.values():
        if quantidade >= 5:
            return 50
        
    return 0

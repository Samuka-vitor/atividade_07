# criando lista
nome = []

# primeira parte
# criando o cód. para acrescentar novos nomes na lista
while True: 
    try: 
        novo_nome = input("Informe um nome que deseja adicionar na lista: ") # escreve o novo nome

        if novo_nome:                               # aqui será acrescentado um novo nome 
            nome.append(novo_nome)                  # função .append() é o que de fato acrescenta novos nomes na lista, observe a sintexe
            print(f"{novo_nome} cadastrado.")       # vai printar o novo nome cm a mensagem
            nome.sort()                             # ordena os nomes em ordem alfabetica
            continue                                
        else:
            break                                

    except Exception as e:                          # aqui será tratado as excessões
        print(f"Nâo foi possível cadastrar o nome. {e}.")

    finally:                                       # pra finalizar, aprenta a lista com novos nomes
        for i in range(len(nome)):
            print(f"Índice {i}: {nome[i]}.")

# altera o nome na lista
try:
    pesquisa_indice = int(input("Informe o índice que deseja alterar: "))
    confirmacao = input(f"Deseja alterar o nome {nome[pesquisa_indice]}? Digite 'sim' para confirmar.")

    if confirmacao == "sim":
        nome_novo = input("Informe o novo nome: ")
        nome[pesquisa_indice] = nome_novo

    else:
        ...
except Exception as e: 
        print(f"Não foi possível alterar o nome. {e}.")

finally: 
     # exibe a lista original
    for i in range(len(nome)):
        print (f"Índice {i}: {nome[i]}")

# tentativa de deletar um item
nome_excluir = input("Me diga, qual nome deseja excluir? ")
if nome_excluir in nome:
    nome.remove(nome_excluir)
    print(f"{nome_excluir} foi removido da lista.")
else:
    print(f"{nome_excluir} não está na lista ou não foi possível excluir.")
    
# exibe a nova lista
for i in range(len(nome)):
        print (f"Índice {i}: {nome[i]}")


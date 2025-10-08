def criar_pessoa(nome: str, idade: int, id: int):
    return dict(id=id, nome=nome, idade=idade)

if __name__ == "__main__":
    p1 = criar_pessoa("Marcos", 28, 1)
    p2 = criar_pessoa("Ana", 24, 2)
    p3 = criar_pessoa("Carlos", 30, 3)
    print(p1)
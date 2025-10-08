def ordenar_lista(numeros: list[int]):
    return sorted(numeros)

if __name__ == "__main__":
    lista = [42, 12, 9, 73, 51, 22]
    resultado = ordenar_lista(lista)
    print(resultado)
def top_tres_maiores(numeros: list[int]):
    return sorted(numeros, reverse=True)[:3]

if __name__ == "__main__":
    lista = [5, 42, 12, 9, 73, 51, 22]
    resultado = top_tres_maiores(lista)
    print(resultado)
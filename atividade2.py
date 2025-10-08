from atividade1 import criar_pessoa  

def adicionar_gostos(pessoas: list, gostos: list):
    id_para_gostos = {item["id"]: item["gostos"] for item in gostos}
    resultado = []
    for pessoa in pessoas[:5]:  
        nova = pessoa.copy()
        nova["gostos"] = id_para_gostos.get(nova["id"], [])
        resultado.append(nova)
    return resultado


if __name__ == "__main__":
    pessoas = [
        criar_pessoa("Marcos", 28, 1),
        criar_pessoa("Ana", 24, 2),
        criar_pessoa("Carlos", 30, 3),
        criar_pessoa("Julia", 22, 4),
        criar_pessoa("Pedro", 27, 5),
        criar_pessoa("Laura", 26, 6)
    ]
    gostos = [
        {"id": 1, "gostos": ["Música", "Futebol"]},
        {"id": 2, "gostos": ["Leitura", "Cinema"]},
        {"id": 3, "gostos": ["Viagem"]},
        {"id": 4, "gostos": ["Dança", "Esportes"]},
        {"id": 5, "gostos": ["Tecnologia", "Culinária"]},
        {"id": 6, "gostos": ["Moda"]}
    ]
    resultado = adicionar_gostos(pessoas, gostos)
    print(resultado)
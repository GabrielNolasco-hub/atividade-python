import pandas as pd

def exportar_csv(pessoas: list, nome_arquivo: str):
    df = pd.DataFrame(pessoas)
    df.to_csv(nome_arquivo, index=False)

# Teste
if __name__ == "__main__":
    from atividade2 import adicionar_gostos
    from atividade1 import criar_pessoa

    # Recriando dados (mesmo da questão 2)
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

    # Adiciona gostos às pessoas
    pessoas_com_gostos = adicionar_gostos(pessoas, gostos)

    # Exporta para CSV
    exportar_csv(pessoas_com_gostos, "pessoas.csv")
    print("Arquivo 'pessoas.csv' gerado com sucesso!")

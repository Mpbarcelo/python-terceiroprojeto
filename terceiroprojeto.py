#%%
# Criando uma lista heterogênea com diferentes tipos de dados

dados_pessoa = ["João", 25, 1.75, True]

# Acessando elementos da lista

nome = dados_pessoa[0]

idade = dados_pessoa[1]

altura = dados_pessoa[2] * 2

e_maior = dados_pessoa[0]

# Exibindo informações

print("Nome:", nome)

print("Idade:", idade)

print("Altura:", altura)

print("É maior de idade?", e_maior)




#%%
idades = []

alturas = []

for i in range(5):

    print(f"Pessoa {i + 1}:")

    idade = int(input("Digite a idade: "))

    altura = float(input("Digite a altura (em metros): "))

    idades.append(idade)

    alturas.append(altura)

print("\nIdades:")

for idade in reversed(idades):

    print(idade)

print("\nAlturas:")

for altura in reversed(alturas):

    print(f"{altura:.2f} metros")
    
    
    
# %%

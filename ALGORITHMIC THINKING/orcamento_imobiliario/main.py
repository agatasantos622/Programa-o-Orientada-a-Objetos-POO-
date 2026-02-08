from imovel import Apartamento, Casa, Estudio
from contrato import Contrato
from gerador_csv import gerar_csv

print("=== ORÇAMENTO IMOBILIÁRIA R.M ===")

print("1 - Apartamento")
print("2 - Casa")
print("3 - Estudio")

opcao = int(input("Escolha o tipo de imóvel: "))

if opcao == 1:
    quartos = int(input("Quantidade de quartos (1 ou 2): "))
    garagem = input("Possui garagem? (s/n): ").lower() == "s"
    crianca = input("Possui crianças? (s/n): ").lower() == "s"
    imovel = Apartamento(quartos, garagem, crianca)

elif opcao == 2:
    quartos = int(input("Quantidade de quartos (1 ou 2): "))
    garagem = input("Possui garagem? (s/n): ").lower() == "s"
    imovel = Casa(quartos, garagem)

elif opcao == 3:
    vagas = int(input("Quantidade de vagas: "))
    imovel = Estudio(vagas)

else:
    print("Opção inválida")
    exit()

contrato = Contrato()
parcelas = int(input("Contrato em quantas parcelas? (até 5): "))
valor_parcela = contrato.parcelar(parcelas)

print("\n--- RESULTADO ---")
print(f"Tipo do imóvel: {imovel.tipo}")
print(f"Valor do aluguel mensal: R$ {imovel.calcular_valor():.2f}")
print(f"Contrato: R$ 2.000,00 em {parcelas}x de R$ {valor_parcela:.2f}")

gerar_csv(imovel.calcular_valor())
print("Arquivo parcelas_orcamento.csv gerado com sucesso!")

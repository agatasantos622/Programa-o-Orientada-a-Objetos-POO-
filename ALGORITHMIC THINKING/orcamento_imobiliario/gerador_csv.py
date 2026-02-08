import csv

def gerar_csv(valor_mensal):
    with open("parcelas_orcamento.csv", mode="w", newline="", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(["Parcela", "Valor (R$)"])

        for i in range(1, 13):
            writer.writerow([i, f"{valor_mensal:.2f}"])

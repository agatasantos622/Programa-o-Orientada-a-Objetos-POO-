class Contrato:
    def __init__(self):
        self.valor = 2000

    def parcelar(self, parcelas):
        if parcelas > 5:
            parcelas = 5
        return self.valor / parcelas
class Imovel:
    def __init__(self, tipo, valor_base):
        self.tipo = tipo
        self.valor_base = valor_base
        self.valor_final = valor_base

    def calcular_valor(self):
        return self.valor_final


class Apartamento(Imovel):
    def __init__(self, quartos, garagem, tem_crianca):
        super().__init__("Apartamento", 700)
        self.quartos = quartos
        self.garagem = garagem
        self.tem_crianca = tem_crianca
        self.calcular_valor()

    def calcular_valor(self):
        self.valor_final = self.valor_base

        if self.quartos == 2:
            self.valor_final += 200

        if self.garagem:
            self.valor_final += 300

        if not self.tem_crianca:
            self.valor_final *= 0.95

        return self.valor_final


class Casa(Imovel):
    def __init__(self, quartos, garagem):
        super().__init__("Casa", 900)
        self.quartos = quartos
        self.garagem = garagem
        self.calcular_valor()

    def calcular_valor(self):
        self.valor_final = self.valor_base

        if self.quartos == 2:
            self.valor_final += 250

        if self.garagem:
            self.valor_final += 300

        return self.valor_final


class Estudio(Imovel):
    def __init__(self, vagas):
        super().__init__("Estudio", 1200)
        self.vagas = vagas
        self.calcular_valor()

    def calcular_valor(self):
        self.valor_final = self.valor_base

        if self.vagas >= 2:
            self.valor_final += 250
            extras = self.vagas - 2
            if extras > 0:
                self.valor_final += extras * 60

        return self.valor_final

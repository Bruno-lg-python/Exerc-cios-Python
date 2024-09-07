class Tipos:
    def __init__(self, nome, raça, cor, espécies,tipo_som):
        self.nome = nome
        self.raça = raça
        self.cor = cor
        self.espécies = espécies
        self.tipo_som = tipo_som


class Animal(Tipos):

    def som(self):
        print(f"O som que o cachorro {self.nome} faz e {self.tipo_som}")
    
    def especies(self):
        print(f'O {self.nome} e um {self.raça} que é {self.espécies}')

    def cores(self):
        print(f'A cor dos pelos de {self.nome} e {self.cor}')

espe = Animal('rex', 'vira_lata', 'preto', 'domesticado', 'auau')
espe.som()
espe.especies()
espe.cores()

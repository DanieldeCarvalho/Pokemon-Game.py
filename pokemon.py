class Pokemon:
    def __init__(self, especie, level=1, nome=None): #<argumento>=None = argumento nao obrigatorio
        self.especie = especie
        self.level = level
        if nome:
            self.nome = nome
        else:
            self.nome = especie

    def __str__(self):
        return (f'{self.nome} ({self.level})')

    def atacar(self, pokemon):
        print(f'{self.especie} atacou {pokemon.especie}')#esse self vai retornar o que eu botei no metodo str.

    pass

class PokemonEletrico(Pokemon):
    tipo = 'eletrico'

    def atacar(self, pokemon):
        print(f'{self} lançou um raio do trovão em {pokemon}')

class PokemonFogo(Pokemon):
    tipo = 'fogo'

    def atacar(self, pokemon):
        print(f'{self} jogou uma bola de fogo em {pokemon}')

class PokemonAgua(Pokemon):
    tipo = 'agua'

    def atacar(self, pokemon):
        print(f'{self} lançou uma bola de fogo em {pokemon}')


# 20:06
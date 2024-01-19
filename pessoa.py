import datetime


class Pessoa:

    @staticmethod
    def converte_data(data):
        try:
            return datetime.datetime.strptime(data, "%d-%m-%Y")
        except ValueError:
            return 'Digite a data corretamente: (d-m-y)'

    def __init__(
            self, 
            nome_completo, 
            nome_social, 
            tipo, 
            cpf_cnpj, 
            endereco, 
            data_nascimento, 
            cidade_natal
            ):
        self.__nome_completo = nome_completo
        self.__nome_social = nome_social
        self.__tipo = tipo
        self.__cpf = cpf_cnpj
        self.__endereco = endereco
        self.__data_nascimento = self.converte_data(data_nascimento)
        self.__cidade_natal = cidade_natal

    @property
    def nome(self):
        return self.__nome_completo
        
    @property
    def idade(self):
        return self.__idade
    
    @property
    def cidade(self):
        return self.__cidade_natal
    
    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @property
    def idade(self):
        try:
            ano_atual = datetime.date.today()
            nascimeto = ano_atual.year - self.__data_nascimento.year

            lista_condicional = [
                ano_atual.month >= self.__data_nascimento.month,
                ano_atual.day >= self.__data_nascimento.day
            ]

            if all(lista_condicional):
                return nascimeto
            return nascimeto - 1         
        except AttributeError:
            return 'Digite a data corretamente: (d-m-y)'

    def __str__(self):
        return (
            f'Meu nome é {self.nome}, tenho {self.idade} anos de idade e sou '
            f'natural de {self.cidade}'
            )

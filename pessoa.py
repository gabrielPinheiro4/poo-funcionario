import datetime

class Pessoa:

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
        self.__data_nascimento = data_nascimento.split('/')
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
        ano_atual = datetime.date.today()
        nascimento_convertido = datetime.date(
            int(self.__data_nascimento[2]), 
            int(self.__data_nascimento[1]), 
            int(self.__data_nascimento[0])
            )

        if ano_atual.month >= nascimento_convertido.month:

            if ano_atual.day >= nascimento_convertido.day:
                return ano_atual.year - nascimento_convertido.year
            return (ano_atual.year - nascimento_convertido.year) - 1
        
        return (ano_atual.year - nascimento_convertido.year) - 1
    

    def __str__(self):
        return (
            f'Meu nome é {self.nome}, tenho {self.idade} anos de idade e sou '
            f'natural de {self.cidade}'
            )

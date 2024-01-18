import datetime, uuid

class Pessoa:
    ano_atual = datetime.date.today()

    def __init__(self, nome_completo, tipo, cpf_cnpj, endereco, data_nascimento, cidade_natal):
        self.__nome_completo = nome_completo
        self.__tipo = tipo
        self.__cpf = cpf_cnpj
        self.__endereco = endereco
        self.__data_nascimento = data_nascimento
        self.__cidade_natal = cidade_natal
        self.__idade = Pessoa.ano_atual.year - self.__data_nascimento.year

    @property
    def get_nome(self):
        return self.__nome_completo
        
    @property
    def get_idade(self):
        return self.__idade
    
    @property
    def get_cidade(self):
        return self.__cidade_natal

    def __str__(self):
        return f'Meu nome é {self.get_nome}, tenho {self.get_idade} anos de idade e sou natural de {self.get_cidade}'


class Funcionario(Pessoa):
    def __init__(self, nome_completo, tipo, cpf_cnpj, endereco, data_nascimento, cidade_natal, empresa, filial, funcao, setor, departamaneto):
        super().__init__(nome_completo, tipo, cpf_cnpj, endereco, data_nascimento, cidade_natal)
        self.__matricula = uuid.uuid4()
        self.__empresa = empresa
        self.__filial = filial
        self.__funcao = funcao
        self.__setor = setor
        self.__departamento = departamaneto

    @property
    def get_filial(self):
        return self.__filial
    
    @property
    def get_setor(self):
        return self.__setor
    
    @property
    def get_funcao(self):
        return self.__funcao

    def __str__(self):
        return f'{self.get_nome}: funcionário da filial {self.get_filial}, setor {self.get_setor}, desempenhando função de {self.get_funcao}'

    
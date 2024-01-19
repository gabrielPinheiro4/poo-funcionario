from pessoa import Pessoa
import uuid


class Funcionario(Pessoa):
    def __init__(
            self, 
            nome_completo, 
            nome_social, 
            tipo, 
            cpf_cnpj, 
            endereco, 
            data_nascimento, 
            cidade_natal, 
            empresa, 
            filial, 
            funcao, 
            setor, 
            departamaneto
            ):
        super().__init__(
            nome_completo, 
            nome_social, 
            tipo, 
            cpf_cnpj, 
            endereco, 
            data_nascimento, 
            cidade_natal
            )
        self.__matricula = str(uuid.uuid4())
        self.__empresa = empresa
        self.__filial = filial
        self.__funcao = funcao
        self.__setor = setor
        self.__departamento = departamaneto

    @property
    def filial(self):
        return self.__filial
    
    @property
    def setor(self):
        return self.__setor
    
    @property
    def funcao(self):
        return self.__funcao

    def __str__(self):
        return (f'{self.nome}: funcionário da filial {self.filial}, '
                f'setor {self.setor}, desempenhando '
                f'função de {self.funcao}')

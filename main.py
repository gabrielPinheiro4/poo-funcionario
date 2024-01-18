from classes import (
    Funcionario, 
    datetime
    )

def main():
    nome_completo = input('Digise seu nome completo: ')
    tipo = input('Pessoa fisica ou juridica ?: ') 
    cpf_cnpj = input('Digite seu cpf ou cnpj: ')
    endereco = input('Digite seu endereço: ')
    data_nascimento = input('Digite sua data de nascimento: ')
    cidade_natal = input('Digite sua cidade natal: ')
    empresa = input('Digite o nome da empresa onde você trabalha: ')
    filial = input('Digite sua filial: ')
    funcao = input('Digite sua função: ') 
    setor = input('Digite seu setor: ')
    departamaneto = input('Digite seu departamento: ')

    data_nascimento = data_nascimento.split('/')
    nova_data = datetime.date(int(data_nascimento[2]), int(data_nascimento[1]), int(data_nascimento[0]))

    funcionario = Funcionario(nome_completo, tipo, cpf_cnpj, endereco, data_nascimento, cidade_natal, empresa, filial, funcao, setor, departamaneto)
    print(funcionario)


if __name__ == '__main__':
    main()
    
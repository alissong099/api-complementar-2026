def main():
    funcionarios = qtd_funcionarios()

    folhas_pagamento = extrato_individual(funcionarios)


def qtd_funcionarios():
    try:
        qtd_funcionarios = int(input('Informe a quantia de funcionários: '))
        return qtd_funcionarios
    except ValueError:
        print('Erro! Por favor insira uma quantia valida!')
        return qtd_funcionarios()

def extrato_individual(qtd_func):
    if qtd_func <= 0:
        return 'Não há nenhum funcionário para exibir a folha de pagamento.'
    
    sal_liquido = 0
    desconto_inss = 0
    vale_refeicao = 0
    bonus_horas_extras = 0
    total_folha = 0
    maior_salario = 0
    menor_salario = 999999

    for i in range(qtd_func):
        nome_funcionario = input('Informe o nome do funcionário -> ')
        sal_bruto = float(input('Informe o salário do funcionário -> '))
        qtd_horas_extras = int(input('Informe as horas extras trabalhadas do funcionário no mês vigente -> '))

        if sal_bruto > 2000:
            vale_refeicao = 150
        
        bonus_horas_extras = ((sal_bruto / 220) * 1.5) * qtd_horas_extras
        desconto_inss = sal_bruto * 0.11
        sal_liquido = ((sal_bruto + bonus_horas_extras) - desconto_inss) - vale_refeicao
        total_folha += sal_liquido
        
        if sal_liquido > maior_salario:
            maior_salario = sal_liquido
        
        if sal_liquido < menor_salario:
            menor_salario = sal_liquido

        extrato = f'''--- EXTRATO: {nome_funcionario.upper()} ---
        Salário Bruto:   R$ {sal_bruto:.2f}
        Horas Extras:    R$ {bonus_horas_extras:.2f}  ({qtd_horas_extras}h)
        INSS:            R$ {desconto_inss:.2f}
        Vale Refeição:   R$ {vale_refeicao:.2f}
        Salário Líquido: R$ {sal_liquido:.2f}
        ---'''
        print(' ')
        print(extrato)
    print(' ')
    adicionais = f'''Maior Salário Líquido: R$ {maior_salario:.2f}
    Menor Salário Líquido: R$ {menor_salario:.2f}
    Total Folha: R$ {total_folha:.2f}'''
    
    print(adicionais)
        


main()
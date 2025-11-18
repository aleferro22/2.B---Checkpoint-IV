# Classe para calcular o desconto do INSS
class CalculadoraINSS:
    def calcular_desconto(self, salario_bruto):
        desconto = 0.0
        
        if salario_bruto <= 1100.00:
            desconto = salario_bruto * 0.075
        elif salario_bruto <= 2203.48:
            desconto = 1100.00 * 0.075 + (salario_bruto - 1100.00) * 0.09
        elif salario_bruto <= 3305.22:
            desconto = 1100.00 * 0.075 + (2203.48 - 1100.00) * 0.09 + (salario_bruto - 2203.48) * 0.12
        else:
            # Acima do teto, desconto máximo aproximado
            desconto = 1100.00 * 0.075 + (2203.48 - 1100.00) * 0.09 + (3305.22 - 2203.48) * 0.12 + (salario_bruto - 3305.22) * 0.14
            # Limite máximo de desconto (teto aproximado)
            if desconto > 3305.22 * 0.14:
                desconto = 3305.22 * 0.14  # Aproximadamente 462.73
        
        return desconto

# Classe para calcular o IRRF
class CalculadoraIRRF:
    def calcular_irrf(self, salario_base):
        irrf = 0.0
        
        if salario_base <= 1903.98:
            irrf = 0.0  # Isento
        elif salario_base <= 2826.65:
            irrf = (salario_base * 0.075) - 169.44
        elif salario_base <= 3751.05:
            irrf = (salario_base * 0.15) - 354.80
        elif salario_base <= 4664.68:
            irrf = (salario_base * 0.225) - 636.13
        else:
            irrf = (salario_base * 0.275) - 869.36
        
        # IRRF não pode ser negativo
        return max(irrf, 0.0)

# Função principal para orquestrar os cálculos
def main():
    try:
        salario_bruto = float(input("Digite o salário bruto: "))
        
        # Instanciar as classes
        calc_inss = CalculadoraINSS()
        calc_irrf = CalculadoraIRRF()
        
        # Calcular desconto INSS
        desconto_inss = calc_inss.calcular_desconto(salario_bruto)
        
        # Calcular salário base
        salario_base = salario_bruto - desconto_inss
        
        # Calcular IRRF
        irrf = calc_irrf.calcular_irrf(salario_base)
        
        # Exibir resultados
        print(f"Salário Bruto: {salario_bruto:.2f}")
        print(f"Desconto INSS: {desconto_inss:.2f}")
        print(f"Salário Base: {salario_base:.2f}")
        print(f"IRRF: {irrf:.2f}")
    
    except ValueError:
        print("Por favor, digite um valor numérico válido para o salário bruto.")

if __name__ == "__main__":
    main()

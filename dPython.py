import sys

# Função para equilibrar o saldo bancário
def equilibrar_saldo(saldo_atual, valor_deposito, valor_retirada):
    # Atualiza o saldo com base nas transações
    saldo_atual += valor_deposito
    saldo_atual -= valor_retirada
    # Arredonda o saldo para uma casa decimal
    saldo_atual = round(saldo_atual, 1)
    return saldo_atual

# Lê o saldo atual da conta bancária
saldo_atual = float(sys.stdin.readline())

# Lê o valor do depósito
valor_deposito = float(sys.stdin.readline())

# Lê o valor da retirada
valor_retirada = float(sys.stdin.readline())

# Chama a função para equilibrar o saldo
novo_saldo = equilibrar_saldo(saldo_atual, valor_deposito, valor_retirada)

# Exibe o saldo atualizado
print("Saldo atualizado na conta:", novo_saldo)

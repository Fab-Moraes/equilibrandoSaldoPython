# equilibrandoSaldoPython

# Descrição

Para esse desafio, considere que você foi contratado por uma empresa bancária para auxiliar nas implementações e melhorias do sistema empresarial. Em uma análise inicial, foi identificado pela equipe financeira a necessidade de desenvolver uma solução que permita ao cliente equilibrar seu saldo bancário. Dessa forma, o programa deve solicitar uma entrada que representa o saldo atual do funcionário, e após, seja informado o valor de duas transações, sendo elas: um depósito e um saque. O programa deve atualizar o saldo com base nas transações e exibir o saldo final.

Informação: As transações de depósito e retirada devem ser tratadas como valores positivos e negativos, respectivamente, para garantir que o cálculo do saldo final seja realizado corretamente.
 

# Entrada
saldoAtual: um número decimal representando o saldo atual da conta bancária.
valorDeposito: um número decimal representando o valor a ser depositado na conta.
valorRetirada: um número decimal representando o valor a ser retirado da conta.

# Regra de Formatação:
Considere apenas uma casa decimal para esse desafio.

# Saída

 Um número decimal que representa o saldo atualizado na conta bancária após o processamento das transações.


# Código modificado
Estou substituindo as chamadas input() pelo sys.stdin.readline() para obter entradas do usuário. Aqui está como cada parte do código funciona:

import sys: Importa o módulo sys, que fornece acesso a funcionalidades relacionadas ao sistema, incluindo a entrada padrão (stdin) e a saída padrão (stdout).

saldo_atual = float(sys.stdin.readline()): Lê uma linha da entrada padrão e a armazena na variável saldo_atual. Como o sys.stdin.readline() retorna uma string, usamos float() para converter essa string em um número decimal.

valor_deposito = float(sys.stdin.readline()): Lê a próxima linha da entrada padrão e a armazena na variável valor_deposito.

valor_retirada = float(sys.stdin.readline()): Lê a próxima linha da entrada padrão e a armazena na variável valor_retirada.

O restante do código é o mesmo que o original, onde chamamos a função equilibrar_saldo com as entradas fornecidas pelo usuário, calculamos o novo saldo e o exibimos na saída padrão com print().

Basicamente, estamos substituindo a função input() padrão, que lê entradas do usuário a partir do teclado, pelo sys.stdin.readline(), que lê as entradas diretamente da entrada padrão. Isso permite que você forneça várias entradas em linhas separadas, como em um arquivo de texto, em vez de uma única entrada por vez.






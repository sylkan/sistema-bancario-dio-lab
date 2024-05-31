def menu():
  """
  Exibe o menu principal do sistema bancário.
  """
  print("\nSistema Bancário DIO")
  print("----------------------")
  print("1. Depositar")
  print("2. Sacar")
  print("3. Extrato")
  print("4. Sair")

  opcao = input("Digite a opção desejada: ")
  return opcao

def depositar(saldo):
  """
  Realiza a operação de depósito em conta.
  """
  valor = float(input("Digite o valor a ser depositado (máximo R$ 1000): R$ "))
  if valor > 1000:
    print("Valor máximo de depósito por operação é de R$ 1000.")
    return saldo
  else:
    saldo += valor
    print(f"Depósito realizado com sucesso! Seu novo saldo é: R$ {saldo:.2f}")
    return saldo

def sacar(saldo, saques_hoje):
  """
  Realiza a operação de saque em conta.
  """
  if saques_hoje >= 3:
    print("Limite diário de saques atingido (3 saques).")
    return saldo, saques_hoje
  else:
    valor = float(input("Digite o valor a ser sacado (máximo R$ 500): R$ "))
    if valor > 500:
      print("Valor máximo de saque por operação é de R$ 500.")
      return saldo, saques_hoje
    elif valor > saldo:
      print("Saldo insuficiente para saque.")
      return saldo, saques_hoje
    else:
      saldo -= valor
      saques_hoje += 1
      print(f"Saque realizado com sucesso! Seu novo saldo é: R$ {saldo:.2f}")
      return saldo, saques_hoje

def extrato(saldo):
  """
  Exibe o extrato da conta.
  """
  print(f"Seu saldo atual é: R$ {saldo:.2f}")

saldo = 0
saques_hoje = 0

while True:
  opcao = menu()

  if opcao == "1":
    saldo = depositar(saldo)
  elif opcao == "2":
    saldo, saques_hoje = sacar(saldo, saques_hoje)
  elif opcao == "3":
    extrato(saldo)
  elif opcao == "4":
    print("Obrigado por usar o Sistema Bancário DIO!")
    break
  else:
   print("Opção inválida. Tente novamente.")
   
   
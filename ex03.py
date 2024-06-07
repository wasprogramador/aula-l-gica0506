taxa_brl_para_usd = 5.29 # USD = 5.29 BRL
taxa_usd_para_brl = 1 / taxa_brl_para_usd # BRL = 0.20 USD

while True:
    #Exibe o menu de opções
    print("\n Escolha uma opção")
    print("1. BRL para US$")
    print("2. US$ para BRL")
    print("3. sair")

    opção = input("Digite o númer da opção desejada")

    if opção == '1':
        valor_brl = float(input("DIgite o valor em (R$:) "))
        valor_usd = valor_brl / taxa_brl_para_usd
        print(f"R$ {valor_brl:.2f} é equivalente a US$ {valor_usd:.2f}")
    elif opção =='2':
        valoe_usd = float(input("Digite o valor em dólares (US$)"))
        valor_brl = valor_usd * taxa_brl_para_usd
        print(f"US$ {valor_usd:.2f} é equivalente a R$ {valor_brl:.2f}")
    elif opção == '3':
        print("Saindo...")
        break
    else:
        print("Opção inválida.. tente novamente")

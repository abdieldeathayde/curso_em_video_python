def questoes():
	dia = int(input("Digite o dia que você nasceu: \n"))
	mes = str(input("Digite o mes de nascimento: \n"))
	ano = int(input("Digite o ano de nascimento: \n"))

	print("=============== Desafio 02 ===============")
	
	info = input(f"Você nasceu no dia {dia} de {mes} de {ano} . Correto? \n")

	if "sim" in info.lower():
		quit()
	else:
		questoes()

questoes()

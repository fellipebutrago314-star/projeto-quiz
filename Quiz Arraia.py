print(" BEM-VINDO AO QUIZ ARRAIÁ DO SABER ")
print("=" * 50)

pontos = 0

# Pergunta 1
print("Pergunta 1: Qual dia do mês de junho é comemorado o Dia de São João?")
print("a) 12 de junho")
print("b) 20 de junho")
print("c) 24 de junho")
print("d) 18 de junho")

per1 = input("Digite o item correto: ")

if per1.lower() == "c":
    print(" Correto!")
    print("São João é comemorado em 24 de junho, data que celebra o nascimento de São João Batista.")
    pontos += 1
else:
    print(" Incorreto!")
    print("A resposta correta era: c) 24 de junho.")
    print("São João Batista é um dos santos mais homenageados nas festas juninas.")

# Pergunta 2
print("Pergunta 2: Qual é o alimento mais típico das festas juninas?")
print("a) Milho")
print("b) Lasanha")
print("c) Feijoada")
print("d) Panelada")

per2 = input("Digite o item correto: ")

if per2.lower() == "a":
    print(" Correto!")
    print("O milho é a base de diversas comidas juninas, como pamonha, canjica e bolo de milho.")
    pontos += 1
else:
    print(" Incorreto!")
    print("A resposta correta era: a) Milho.")
    print("O milho é um dos principais símbolos da culinária junina.")

# Pergunta 3
print("Pergunta 3: Qual a principal dança das festas juninas?")
print("a) Forró")
print("b) Quadrilha")
print("c) Salsa")
print("d) Samba")

per3 = input("Digite o item correto: ")

if per3.lower() == "b":
    print(" Correto!")
    print("A quadrilha é uma dança folclórica tradicional que representa um casamento caipira.")
    pontos += 1
else:
    print(" Incorreto!")
    print("A resposta correta era: b) Quadrilha.")
    print("A quadrilha é considerada a dança mais tradicional das festas juninas.")

# Pergunta 4
print("Pergunta 4: Qual a principal região do Brasil onde os festejos juninos são mais famosos?")
print("a) Norte")
print("b) Sudeste")
print("c) Nordeste")
print("d) Sul")

per4 = input("Digite o item correto: ")

if per4.lower() == "c":
    print(" Correto!")
    print("O Nordeste realiza algumas das maiores festas juninas do mundo.")
    pontos += 1
else:
    print(" Incorreto!")
    print("A resposta correta era: c) Nordeste.")
    print("Cidades como Campina Grande e Caruaru são referências nas festas juninas.")

# Pergunta 5
print("Pergunta 5: Qual destes santos é homenageado nas festas juninas?")
print("a) São Pedro")
print("b) São Jorge")
print("c) Santo Expedito")
print("d) São Bento")

per5 = input("Digite o item correto: ")

if per5.lower() == "a":
    print("Correto!")
    print("São Pedro é um dos três santos celebrados durante o período junino.")
    pontos += 1
else:
    print("Incorreto!")
    print("A resposta correta era: a) São Pedro.")
    print("Os três principais santos juninos são Santo Antônio, São João e São Pedro.")

# Pergunta 6
print("Pergunta 6: Qual destas comidas é tradicionalmente feita com milho?")
print("a) Sushi")
print("b) Pamonha")
print("c) Pizza")
print("d) Hambúrguer")

per6 = input("Digite o item correto: ")

if per6.lower() == "b":
    print("Correto!")
    print("A pamonha é preparada com milho verde e muito apreciada nas festas juninas.")
    pontos += 1
else:
    print("Incorreto!")
    print("A resposta correta era: b) Pamonha.")
    print("A pamonha é uma das comidas típicas mais populares do período junino.")

# Resultado final
print("\n" + "=" * 50)
print("RESULTADO FINAL ")
print("=" * 50)

print(f"Você acertou {pontos} de 6 perguntas!")

if pontos == 6:
    print(" Excelente! Você é um especialista em cultura junina!")
elif pontos >= 4:
    print(" Muito bem! Você conhece bastante sobre as festas juninas!")
elif pontos >= 2:
    print(" Bom trabalho! Continue aprendendo sobre a cultura junina.")
else:
    print("Que tal estudar mais sobre as festas juninas e tentar novamente?")

print("Obrigado por participar do Quiz Arraiá do Saber! ")

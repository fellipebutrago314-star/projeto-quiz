import tkinter as tk
from tkinter import messagebox

# Lista de perguntas
perguntas = [
    {
        "pergunta": "1. Qual dia de junho é comemorado o Dia de São João?",
        "opcoes": ["a) 12 de junho", "b) 20 de junho", "c) 24 de junho", "d) 18 de junho"],
        "resposta": "c",
        "explicacao": "São João é comemorado em 24 de junho."
    },
    {
        "pergunta": "2. Qual é o alimento mais típico das festas juninas?",
        "opcoes": ["a) Milho", "b) Lasanha", "c) Feijoada", "d) Panelada"],
        "resposta": "a",
        "explicacao": "O milho é a base de várias comidas típicas juninas."
    },
    {
        "pergunta": "3. Qual a principal dança das festas juninas?",
        "opcoes": ["a) Forró", "b) Quadrilha", "c) Salsa", "d) Samba"],
        "resposta": "b",
        "explicacao": "A quadrilha é a dança tradicional das festas juninas."
    },
    {
        "pergunta": "4. Qual região do Brasil possui os festejos juninos mais famosos?",
        "opcoes": ["a) Norte", "b) Sudeste", "c) Nordeste", "d) Sul"],
        "resposta": "c",
        "explicacao": "O Nordeste possui algumas das maiores festas juninas do mundo."
    },
    {
        "pergunta": "5. Qual santo também é homenageado nas festas juninas?",
        "opcoes": ["a) São Pedro", "b) São Jorge", "c) São Bento", "d) Santo Expedito"],
        "resposta": "a",
        "explicacao": "São Pedro é um dos três principais santos juninos."
    },
    {
        "pergunta": "6. Qual comida típica é feita com milho verde?",
        "opcoes": ["a) Pizza", "b) Hambúrguer", "c) Pamonha", "d) Sushi"],
        "resposta": "c",
        "explicacao": "A pamonha é preparada a partir do milho verde."
    }
]

indice = 0
pontos = 0

# Função para mostrar a pergunta
def mostrar_pergunta():
    global indice

    if indice < len(perguntas):
        pergunta.config(text=perguntas[indice]["pergunta"])
        resposta.set("")

        for i in range(4):
            botoes[i].config(
                text=perguntas[indice]["opcoes"][i],
                value=chr(97 + i)  # a, b, c, d
            )
    else:
        finalizar()

# Função para verificar resposta
def verificar():
    global indice, pontos

    if resposta.get() == "":
        messagebox.showwarning("Aviso", "Escolha uma alternativa!")
        return

    if resposta.get() == perguntas[indice]["resposta"]:
        pontos += 1
        messagebox.showinfo(
            "Resposta",
            "✅ Correto!\n\n" + perguntas[indice]["explicacao"]
        )
    else:
        correta = perguntas[indice]["resposta"]
        messagebox.showinfo(
            "Resposta",
            f"❌ Incorreto!\n\nResposta correta: {correta}\n\n"
            + perguntas[indice]["explicacao"]
        )

    indice += 1
    mostrar_pergunta()

# Resultado final
def finalizar():
    pergunta.config(text=f"Fim do quiz!\n\nVocê acertou {pontos} de {len(perguntas)} perguntas.")

    for botao in botoes:
        botao.destroy()

    botao_proximo.destroy()

    if pontos == 6:
        resultado.config(text="🌟 Excelente! Você é especialista em São João!")
    elif pontos >= 4:
        resultado.config(text="🎉 Muito bem! Você conhece bastante a cultura junina!")
    else:
        resultado.config(text="📚 Continue estudando e tente novamente!")

# Janela principal
janela = tk.Tk()
janela.title("Quiz Arraiá do Saber")
janela.geometry("600x400")

titulo = tk.Label(
    janela,
    text="🌽 QUIZ ARRAIÁ DO SABER 🌽",
    font=("Arial", 16, "bold")
)
titulo.pack(pady=10)

pergunta = tk.Label(
    janela,
    text="",
    font=("Arial", 12),
    wraplength=500
)
pergunta.pack(pady=15)

resposta = tk.StringVar()

botoes = []
for i in range(4):
    rb = tk.Radiobutton(
        janela,
        text="",
        variable=resposta,
        value="",
        font=("Arial", 11)
    )
    rb.pack(anchor="w", padx=100)
    botoes.append(rb)

botao_proximo = tk.Button(
    janela,
    text="Próxima Pergunta",
    command=verificar,
    font=("Arial", 11)
)
botao_proximo.pack(pady=20)

resultado = tk.Label(janela, font=("Arial", 12, "bold"))
resultado.pack()

mostrar_pergunta()

janela.mainloop()
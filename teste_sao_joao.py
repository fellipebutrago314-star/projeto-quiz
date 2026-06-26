import tkinter as tk
from tkinter import messagebox

# ==========================================================
# Quiz Arraiá do Saber - Tema São João (Tkinter)
# ==========================================================

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

# ==========================================================
# Estado do jogo
# ==========================================================

indice = 0
pontos = 0
respondido = False

# ==========================================================
# Estilo/tema
# ==========================================================

CORES = {
    "bg": "#FFF1C7",          # palha
    "painel": "#FFDD75",     # dourado
    "painel2": "#FFE9A8",   # amarelinho
    "texto": "#3B2F1A",     # marrom
    "verde": "#2E7D32",
    "vermelho": "#D32F2F",
    "azul": "#1565C0",
    "laranja": "#EF6C00",
    "roxo": "#6A1B9A",
    "cinza": "#6B5B4A",
    "branco": "#FFFFFF",
}

FONTS = {
    "titulo": ("Arial", 18, "bold"),
    "sub": ("Arial", 11, "bold"),
    "pergunta": ("Arial", 16, "bold"),
    "opcao": ("Arial", 11, "bold"),
    "exp": ("Arial", 11),
}

# ==========================================================
# Funções auxiliares
# ==========================================================


def set_status(msg, cor="#1565C0", icone=""):
    status.config(text=f"{icone} {msg}".strip(), fg=cor)


def marcar_opcoes(estou_correto: bool):
    """Marca as alternativas com cores e desabilita após responder."""
    global botoes

    correta_val = perguntas[indice]["resposta"]

    for i, rb in enumerate(botoes):
        rb.config(state="disabled")

        valor = chr(97 + i)  # a,b,c,d
        if valor == correta_val:
            rb.config(bg=CORES["verde"], fg=CORES["branco"],
                      activebackground=CORES["verde"], activeforeground=CORES["branco"])
        else:
            if not estou_correto and rb.cget("value") == resposta.get():
                rb.config(bg=CORES["vermelho"], fg=CORES["branco"],
                          activebackground=CORES["vermelho"], activeforeground=CORES["branco"])
            else:
                rb.config(bg=CORES["painel2"], fg=CORES["texto"],
                          activebackground=CORES["painel2"], activeforeground=CORES["texto"])


# ==========================================================
# Lógica do quiz
# ==========================================================

def mostrar_pergunta():
    global indice, respondido

    respondido = False
    botao_proximo.config(text="Responder", state="normal", command=verificar)

    if indice >= len(perguntas):
        finalizar()
        return

    # reset visual
    for rb in botoes:
        rb.config(state="normal", bg=CORES["painel2"], fg=CORES["texto"],
                  activebackground=CORES["painel2"], activeforeground=CORES["texto"])

    resposta.set("")
    info.config(text=f"Pergunta {indice + 1} de {len(perguntas)}")

    pergunta_label.config(text=perguntas[indice]["pergunta"])
    explicacao.config(text="")
    set_status("Escolha uma alternativa e responda!",
               cor=CORES["azul"], icone="🎯")

    for i in range(4):
        botoes[i].config(text=perguntas[indice]["opcoes"]
                         [i], value=chr(97 + i))


def proxima():
    global indice
    indice += 1
    mostrar_pergunta()


def verificar():
    global indice, pontos, respondido

    if respondido:
        return

    if resposta.get() == "":
        messagebox.showwarning("Aviso", "Escolha uma alternativa!")
        return

    correta = perguntas[indice]["resposta"]
    escolhida = resposta.get()

    respondido = True

    if escolhida == correta:
        pontos += 1
        explicacao.config(text=perguntas[indice]["explicacao"])
        set_status("Acertou!", cor=CORES["verde"], icone="✅")
        marcar_opcoes(estou_correto=True)
    else:
        explicacao.config(text=perguntas[indice]["explicacao"])
        set_status("Ops! Quase!", cor=CORES["vermelho"], icone="❌")
        marcar_opcoes(estou_correto=False)

    botao_proximo.config(text="Próxima Pergunta",
                         state="normal", command=proxima)


def finalizar():
    global pontos

    for rb in botoes:
        rb.destroy()

    botao_proximo.destroy()

    info.config(text="Fim do quiz! 🎉")
    pergunta_label.config(
        text=f"Você acertou {pontos} de {len(perguntas)} perguntas.")
    explicacao.config(text="")

    if pontos == len(perguntas):
        set_status("🌟 Excelente! Você é especialista em São João!",
                   cor=CORES["roxo"], icone="🏆")
    elif pontos >= 4:
        set_status("🎉 Muito bem! Você conhece a cultura junina!",
                   cor=CORES["verde"], icone="👏")
    else:
        set_status("📚 Continue estudando e tente novamente!",
                   cor=CORES["laranja"], icone="🌽")


# ==========================================================
# Janela principal (responsiva)
# ==========================================================

janela = tk.Tk()
janela.title("Quiz Arraiá do Saber (São João)")
janela.geometry("1920x1080")
janela.minsize(1920, 1080)
janela.configure(bg=CORES["bg"])

janela.grid_rowconfigure(0, weight=0)
janela.grid_rowconfigure(1, weight=1)
janela.grid_columnconfigure(0, weight=1)

# Header com Canvas (bandeirinhas)
header = tk.Frame(janela, bg=CORES["bg"])
header.grid(row=0, column=0, sticky="nsew")
header.grid_columnconfigure(0, weight=1)

canvas = tk.Canvas(header, bg=CORES["bg"], highlightthickness=0, height=120)
canvas.grid(row=0, column=0, sticky="nsew")

# Título no header
titulo = tk.Label(
    header,
    text="🌽 QUIZ ARRAIÁ DO SABER 🌽\nTema: São João",
    bg=CORES["bg"],
    fg=CORES["texto"],
    font=FONTS["titulo"],
)
# posiciona no topo central
titulo.place(relx=0.5, rely=0.1, anchor="n")

# Desenho simples de bandeirinhas
colors = [CORES["laranja"], CORES["verde"],
          CORES["roxo"], CORES["vermelho"], CORES["azul"]]
w = 900
h = 120

# corda (aprox)
canvas.create_line(20, 35, w - 20, 35, fill="#7A5A3A", width=3)

# triângulos
for i in range(13):
    x1 = 30 + i * 68
    y1 = 25
    x2 = x1 + 52
    c = colors[i % len(colors)]
    canvas.create_polygon(x1, y1, x2, y1, (x1 + x2) / 2,
                          y1 + 20, fill=c, outline="white", width=1)

# Painel principal
main = tk.Frame(janela, bg=CORES["bg"], padx=18, pady=10)
main.grid(row=1, column=0, sticky="nsew")
main.grid_rowconfigure(0, weight=1)
main.grid_columnconfigure(0, weight=1)

card = tk.Frame(main, bg=CORES["painel"], bd=0, padx=16, pady=14)
card.grid(row=0, column=0, sticky="nsew")
card.grid_rowconfigure(0, weight=1)
card.grid_columnconfigure(0, weight=1)

info = tk.Label(card, text="Pergunta",
                bg=CORES["painel"], fg=CORES["cinza"], font=FONTS["sub"])
info.grid(row=0, column=0, sticky="w")

pergunta_label = tk.Label(
    card,
    text="",
    bg=CORES["painel"],
    fg=CORES["texto"],
    font=FONTS["pergunta"],
    wraplength=560,
    justify="center",
)
pergunta_label.grid(row=1, column=0, sticky="w", pady=(10, 12))

# Alternativas
resposta = tk.StringVar()

options_frame = tk.Frame(card, bg=CORES["painel"])
options_frame.grid(row=2, column=0, sticky="nsew")

botoes = []
for i in range(4):
    rb = tk.Radiobutton(
        options_frame,
        text="",
        variable=resposta,
        value="",
        bg=CORES["painel2"],
        fg=CORES["texto"],
        activebackground=CORES["painel2"],
        activeforeground=CORES["texto"],
        selectcolor=CORES["painel2"],
        font=FONTS["opcao"],
        indicatoron=False,
        padx=12,
        pady=8,
        borderwidth=0,
    )
    rb.grid(row=i, column=0, sticky="ew", pady=6)
    botoes.append(rb)

# Explicação inline
explicacao = tk.Label(
    card,
    text="",
    bg=CORES["painel"],
    fg=CORES["texto"],
    font=("Arial", 11),
    wraplength=560,
    justify="left",
)
explicacao.grid(row=3, column=0, sticky="w", pady=(10, 0))

# Status (feedback)
status = tk.Label(
    card, text="", bg=CORES["painel"], fg=CORES["azul"], font=("Arial", 12, "bold"))
status.grid(row=4, column=0, sticky="w", pady=(10, 0))

botao_proximo = tk.Button(
    card,
    text="Responder",
    command=verificar,
    bg=CORES["verde"],
    fg=CORES["branco"],
    activebackground="#1B5E20",
    activeforeground=CORES["branco"],
    font=("Arial", 12, "bold"),
    relief="raised",
    padx=16,
    pady=8,
)
botao_proximo.grid(row=5, column=0, sticky="e", pady=(14, 0))

mostrar_pergunta()

janela.mainloop()

import turtle

def avancar(distancia):
    turtle.forward(distancia)

def voltar(distancia):
    turtle.backward(distancia)

def girar_direita(angulo):
    turtle.right(angulo)

def girar_esquerda(angulo):
    turtle.left(angulo)

def elevar_caneta():
    turtle.penup()

def abaixar_caneta():
    turtle.pendown()

def mudar_cor(cor):
    turtle.color(cor)

def definir_posicao(x, y):
    turtle.goto(x, y)

def definir_titulo(titulo):
    turtle.title(titulo)

def iniciar():
    turtle.mainloop()
    
def mudar_cor():
    turtle.color()
    
def mudar_cor_fundo(cor):
    turtle.bgcolor(cor)
    
def mudar_velocidade(velocidade):
    turtle.speed(velocidade)
    
def mudar_icone(nome):
    icones = {
        "classico": "classic",
        "Classico": "classic",
        "tartaruga": "turtle",
        "Tartaruga": "turtle",
        "circulo": "circle",
        "Circulo": "circle",
        "quadrado": "square",
        "Quadrado": "square",
        "triangulo": "triangle",
        "Triangulo": "triangle",
        "seta": "arrow",
        "Seta": "arrow"
    }
    turtle.shape(icones.get(nome, "turtle"))
    

    

    
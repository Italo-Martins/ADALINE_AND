''''
Autor: Italo Martins Cordeiro

'''
import numpy as np
import matplotlib.pyplot as plt


# Fução para plotar reta de decisão.
def graph(W, B, cont, col):
    x_line = np.linspace(-1, 2)
    a = -(W[0]/W[1])
    c = B/W[1]
    y_line = a*x_line - c
    plt.figure(1)
    plt.plot(x_line, y_line, label = f'Reta de decisão interação {cont}', color = col, linewidth=3.0)
    plt.scatter([0,0,1], [0,1,0], color = 'g', s = 70)
    plt.scatter([1], [1], color = 'r', s = 70)
    plt.xlim(-1,2)
    plt.ylim(-1,2)
    plt.xlabel('X0', fontsize = 16)
    plt.ylabel('X1', fontsize = 16)
    plt.title('Plano de Serpação', fontsize = 18)
    plt.legend()
    plt.show()

#Função de ativação.
def active_linear(entrada):
    if entrada >= 1:
        return 1
    elif entrada <= 0:
        return 0
    return entrada
    

#Parâmetros Iniciais da Rede Neural.
n_epocha = 10 # Número máximo de epocha.
err = 0.01 # Erro mínimo para.
a = 0.8 #Taxa de aprendizado.

# Vetor de Entrada da Rede Neural.
x = np.array([[0,0],
              [0,1],
              [1,0],
              [1,1]])

#Vetor de Saída Esperado.
y = np.array([0,0,0,1])

#Incialização do vetor peso.
w = np.array([0,0])

#Inicialização da bias.
b = 0


# Contagem de epocha.
epocha = 0
# Vetores de erro
erro_epocha = np.array([])
erro_medio = np.array([])
numero_epocha = np.array([])
reta = 0

#Laço de interação
while epocha < n_epocha:
    ind = 0
    erro = 0

    for i in x:
        
        f = np.dot(i,w.T) #Produto dos pessoas pelas entradas
        y_out = f + b  #Soma com a bias
        y_out = active_linear(y_out) # Resposta encontrada
        e = y[ind] - y_out # Calculo do erro
        erro = abs(e) + erro # Soma dos erros por interação
        w = w + a * e * i # Atualização do pesos
        b = b + a * e #Atualização da bias
        ind += 1
        reta += 1
        if w[1] != 0:
            graph(w,b,reta, 'b') #Função para plotar a reta de descisão
    
   #Condicional para finalizar o laço caso o erro seja menor que o especificado    
    if e<= err:
        break    
    epocha += 1
    numero_epocha = np.append(numero_epocha, epocha)
    erro_epocha = np.append(erro_epocha, e) # Vetor de erro por epoca
    erro_medio = np.append(erro_medio, erro/4) # Vetor de erro por epoca
    
# Chamando a função para plotar as ultima reta de descisão        
graph(w,b,reta, 'r')

#Plote do grafico do erro por epoca
plt.figure(2)
plt.plot(numero_epocha, erro_epocha, label = 'Erro', linewidth=3.0)
plt.ylabel('Erro', fontsize = 16)
plt.xlabel('Época', fontsize = 16)
plt.title('Grafico do Erro por Época', fontsize = 18)
plt.legend()
plt.show()


#Geração dos pontos do plano entre 0 e 1
points = 50
x_test = np.random.rand(points)
y_test = np.random.rand(points)

# Laço para pintar os pontos do plano de acordo com a ADALINE
for k in range(len(y_test)):
    for l in range(len(x_test)):
        entrada = np.array([x_test[k], y_test[l]])
        f = np.dot(entrada,w.T) #Produto dos pessoas pelas entradas
        y_out = f + b #Soma com a bias

        plt.figure(3)
        if y_out > 0:
            plt.scatter(x_test[k], y_test[l], color = 'r',s = 90)
        else:
            plt.scatter(x_test[k], y_test[l], color = 'b', s = 90)
plt.xlabel('X',fontsize = 16)
plt.ylabel('Y',fontsize = 16)
plt.show()


x1 = np.linspace(-2,2.8,500)
y1 = np.array([])

for k in x1:
    y1 = np.append(y1,active_linear(k))

plt.figure(4)
plt.plot(x1,y1, label = 'Linear', linewidth = 3)
plt.ylabel('Y', fontsize = 16)
plt.xlabel('X', fontsize = 16)
plt.title('Função de Ativação', fontsize = 18)
plt.xlim(-2, 2.8)
plt.legend()
plt.show()

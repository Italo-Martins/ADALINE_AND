# ADALINE como porta AND
Algoritmo baseado no modelo ADALINE para funcionar como porta logica AND.

Esse algoritmo foi desenvolvido durante o aprendizado de Rede Neurais (RN) e consiste no desenvolvimento de um algoritmo baseado no modelo matemático de uma rede **ADALINE**. Após o desenvolvimento do modelo será treinado para funcionar conforme uma porta logica AND, para isso o conjunto de dados de treinamento sera a tabela verdade da porta logica.

**TABELA VERDADE PORTA LOGICA AND:**
| X1 | X2 | Y |
|----|----|---|
| 0  | 0  | 0 |
| 0  | 1  | 0 |
| 1  | 0  | 0 |
| 1  | 1  | 1 |

-A função de ativação utiliza é a linear o seu gráfico também é plotado:

 ![funcao de ativacao](https://user-images.githubusercontent.com/77513186/172415619-6b70eaf6-73dd-46ca-a99c-bd7bd0157d1c.png)

 
-Para verificar o andamento do treinamento são plotados os gráficos do erro por época e a reta de decisão por interação:

![erro por epoca](https://user-images.githubusercontent.com/77513186/172415938-40ea6efb-5426-454e-9ffd-e0344744376e.png)

![reta de separacao](https://user-images.githubusercontent.com/77513186/172415947-dd5b2c4d-49c6-49fe-bc89-ac435e8fcd15.png)

-Para verificar se o modelo foi corretamente trinado o conjunto de testes são pontos entre 0 e 1 do plano x e y, caso a resposta seja 1 o ponto será pintado de vermelho caso a respostas seja 0 o ponto será pintado de azul:

![plano de separação](https://user-images.githubusercontent.com/77513186/172418397-c294f1ec-4504-42eb-a48c-2c28028f5123.png)

# Grid

## `display: grid`

-   Utiliza-se dentro de um container para transformar seus itens em grid items podendo manipular o seu posicionamento

#

## `grid-template-columns:`

-   Serve para definir a quantidade de colunas e o tamanho delas

#

## `grid-template-rows:`

-   podemos definir a quantidade de linhas e tamanho delas.

-   E também podemos utilizar o `grid-auto-rows:` para definir o tamanho das novas linhas

#

## `gap: 20px`

-   para dar espaço entre os grid items

#

# Alinhamento do container

**obs: para obter o efeito é necessario ter espaço sobrando para o alinhamento**

## `align-content:`

-   Quando utilizado num container por exemeplo, alinha todos os contéudos dentro dele na vertical, complementando utilizando:

![](https://cdn.discordapp.com/attachments/371604240591749120/1083857154097811616/image.png)

#

## `justify-content:`

-   Basicamente a mesma coisa do align so que na horizontal:

![](https://cdn.discordapp.com/attachments/371604240591749120/1083857571322015744/image.png)
![](https://cdn.discordapp.com/attachments/371604240591749120/1083857499742015578/image.png)

#

## `place-content:`

-   É um atalho para usar o align e o justify utilizando apenas uma linha de comando, e a ordem é:

    align-content

    justify-content

![](https://cdn.discordapp.com/attachments/371604240591749120/1083857571322015744/image.png)
![](https://cdn.discordapp.com/attachments/371604240591749120/1083861347743318127/image.png)

#

# Alinhamento de grid items

## `grid-column:`

-   Utiliza-se para informar a posição do item nas colunas podendo definir um local fixo ou uma coluna de inicio e uma de fim

#

## `grid-row:`

-   Mesma coisa da coluna porém em linha

#

## `align-items:` e `justify-items:` e `place-items:`

-   Utiliza-se dentro do container que engloba todos os elementos do grid e ele realiza a alteração em todos os itens

#

## `align-items:`

![](https://cdn.discordapp.com/attachments/371604240591749120/1083938728717848657/image.png)
![](https://cdn.discordapp.com/attachments/371604240591749120/1083938846833647696/image.png)

#

## `jutify-items:`

![](https://cdn.discordapp.com/attachments/371604240591749120/1083938728717848657/image.png)
![](https://cdn.discordapp.com/attachments/371604240591749120/1083938959396192337/image.png)

#

## `place-items:`

**obs: aqui pode receber 2 argumentos a ordem é align, justify**

![](https://cdn.discordapp.com/attachments/371604240591749120/1083938728717848657/image.png)
![](https://cdn.discordapp.com/attachments/371604240591749120/1083939468219781201/image.png)

#

## `align-self:` e `justify-self:` e `place-self:`

-   Utiliza-se dentro do elemento que deseja alterar

#

## `align-self:`

![](https://cdn.discordapp.com/attachments/371604240591749120/1083940696878223390/image.png)

![](https://cdn.discordapp.com/attachments/371604240591749120/1083940334381318154/image.png)

#

## `justify-self:`

![](https://cdn.discordapp.com/attachments/371604240591749120/1083940696878223390/image.png)
![](https://cdn.discordapp.com/attachments/371604240591749120/1083940368275480676/image.png)

#

## `place-self:`

**obs: aqui pode receber 2 argumentos a ordem é align, justify**

![](https://cdn.discordapp.com/attachments/371604240591749120/1083940696878223390/image.png)
![](https://cdn.discordapp.com/attachments/371604240591749120/1083940387191799918/image.png)

# Modelo SIR

- Sucetiveis
- Infectados
- Removidos

      <-

  [S] -> [I] -> [R]

- t -> Time (dia)

St+1 = St - B _ St _ It
It+1 = It + B _ St _ It - G _ It
Rt+1 = Rt + G _ It

B equals to avg(contatos pessoa -> individuos infectados)
G equals to (remocao individuos infectados)
1/G = avg(dias passados ate remocao pessoa)

## Goal do programa

- Fracoes e quantidades de individuos sucetiveis, infectados, recuperados, e mortos teve em um dia especifico do periodo analisado

- Quando aconteceu o pico da epidemia (dia com numero maximo de infectados)

- Quando foi a primeira vez que o numero de infectados ficou menor que o seu valor inicial

- Fracao e quantidade de pessoas que morreram antes e depois do pico da epidemia durante o periodo analisado

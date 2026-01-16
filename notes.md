# Idea: Dividir para conquistar

Queremos posicionar la mayor cantidad de paneles (de dimensión i x j) en un techo de tamaño (n x m).

Por inducción:

Si suponemos que conocemos la mayor cantidad de paneles en un techo de tamaño (n - 1 x m - 1)
¿Cómo podemos obtener el resultado para el techo de n x m?

Veamos un ejemplo,

Sea este un rectangulo de tamaño n x m:

+-+-+-+..
|x|x| | .
|x|x| | .
|x|x| | .
+-+-+-+..

Si queremos expandirlo en una de sus dimensiones vamos a agregar un nuevo espacio de tamaño 1 x n.

Ese nuevo espacio lo podemos usar para colocar paneles.

Podemos elegir la orientación.

Hay tres posibilidades:

1. Los colocamos todos horizontales
2. Los colocames todos verticales
3. Una mezcla

En el primer caso, el área afectada va a ser de tamaño j x n,
y nos queda un rectangulo no afectado de tamaño n - j x n.
Si conocemos el máximo para esa área no afectada, el maximo correspondera a la suma de ese máximo con
los que nos caben horizontalmente.
Similarmnte ocurre para los casos 2 y 3.

Por lo tanto el máximo va a corresponder a el máximo entre estas 3 opciones.

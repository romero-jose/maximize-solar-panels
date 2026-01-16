# Idea: Dividir para conquistar

Queremos posicionar la mayor cantidad de paneles (de dimensión i x j) en un techo de tamaño (n x m).

### Intuición: Dividir para conquistar

Si suponemos que conocemos la mayor cantidad de paneles en un techo de tamaño (n - 1 x m - 1)
¿Cómo podemos obtener el resultado para el techo de n x m?

Veamos un ejemplo, sea este un rectangulo de tamaño n x m:

```
+-+-+-+..
|x|x| | .
|x|x| | .
|x|x| | .
+-+-+-+..
```

Si queremos expandirlo horizontalmente vamos a agregar un nuevo espacio al techo de tamaño 1 x n.

¿Cómo podemos usar este espacio para colocar más paneles?

Según la orientación hay tres posibilidades:

1. Los colocamos todos horizontales
2. Los colocames todos verticales
3. Una mezcla

En el primer caso, el área afectada va a ser de tamaño j x n,
y nos queda un rectangulo no afectado de tamaño n - j x n.
Es decir, hemos dividido el problema en dos partes: un techo de ancho j y otro de ancho n - j.
En el caso 2, el área afectada va a ser de ancho 1.
El caso 3 es análogo al caso 1.

Por lo tanto el máximo va a corresponder a el máximo entre estas 3 opciones que en realidad se pueden reducir a sólo dos.

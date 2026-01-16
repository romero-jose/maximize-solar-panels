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
De esta manera hemos logrado replantear el problema en base a versiones más pequeñas del mismo problema.

### Casos base

Respecto a los casos bases, el máximo para cualquier techo más pequeño que el panel es 0,
y el máximo para un techo justo del tamaño del panel es 1.

```
+-+
|x|
|x|
|x|
+-+
```

### Caso inductivo

Los subproblemas que nos interesan son:

1. n - ancho x m y ancho x m
2. n - largo x m y largo x m

Sin embargo, en realidad el problema es bidimensional y hasta ahora nos hemos concentrado en una sola dirección.
Afortunadamente, podemos aplicar el mismo razonamiento para la otra dirección y de esa manera llegamos a los siguientes casos:

1. n - ancho x m y ancho x m
2. n - largo x m y largo x m
3. n x m - largo y n x largo
4. n x m - ancho y n x ancho

Dado que estos subproblemas son estrictamente más pequeños que el problema original,
podemos solucionar el problema por induccion.

### Implementación

En términos de implementación, hay dos maneras naturales de hacerlo: top-down y bottom-up.
Primero partí implementando la solución bottom up,
pero después me di cuenta que en este caso era más elegante la solución top-down.

Procedemos tal cual la explicación de la solución. Aunque hay algunos detalles que explicar:

1. Utilizamos el decorador `@cache` de Python para implementar de forma sencilla la memoización.
2. Por un tema de eficiencia agregamos a los casos base todos los casos donde los paneles calzan perfecto.

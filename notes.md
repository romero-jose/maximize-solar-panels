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

### Implementación

En términos de implementación, hay dos maneras naturales de hacerlo, top-down y bottom-up.
Primero partí implementando la solución bottom up,
pero después me di cuenta que en este caso era más elegante la solución top-down.

Procedemos tal cual la explicación de la solución. Aunque hay algunos detalles que explicar.

En primer lugar, por un tema de eficiencia y no de correctitud, agregamos a los casos base todos los casos donde los paneles calzan perfecto.

En el caso inductivo, identificamos tres posibilidades, pero no hemos explicado en detalle como llegamos a los subproblemas.
Las tres posibilidades eran:

1. Colocar todos los paneles de forma horizontal
2. Colocar todos los paneles de forma vertical
3. Una mezcla

Además, existe una cuarta posiblidad que no mencionamos, no colocar ningún panel.
Este caso no lo consideramos porque lo que nos interesa es el máximo número de paneles que se pueden colocar, y no colocar ningún panel nunca nos va a ayudar a llegar a esta meta.

Si colocamos todos los paneles de forma vertical,
el ancho del área afectada por esta decisión va a ser del ancho del panel.

Si colamos todos los paneles de forma horizonal,
el ancho del área afectada va a ser el largo del panel.

En el caso 3 va a haber por lo menos un panel de forma horizontal y por lo tanto el ancho del área afectada va a ser el largo del panel nuevamente.

De esta manera, podemos dividir los tres casos anteriores en solamente dos:

1. ancho = ancho del panel
2. ancho = largo del panel

Entonces, como existen únicamente dos casos, basta con estudiar esos dos casos para encontrar el máximo que buscamos.

De esta manera, los dos subproblemas que nos interesan son:

1. n - ancho x m y ancho x m
2. n - largo x m y largo x m

Hasta ahora hemos explorado una dirección, pero en realidad, el problema es bidimensional.

Afortunadamente, el problema es simétrico y podemos utilizar el mismo razonamiento para la otra dirección.

De esta manera finalmente, dividimos el problema en los subproblemas:

1. n - ancho x m y ancho x m
2. n - largo x m y largo x m
3. n x m - largo y n x largo
4. n x m - ancho y n x ancho

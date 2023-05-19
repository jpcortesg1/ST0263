# Universidad EAFIT

# Laboratior 5.1

## Juan Pablo Cortes Gonzalez

## 19 de Mayo del 2033

## Documentación para manejo de MapReduce con MRJOB y Wordcount en Apache Spark EN AWS EMR

# 1 Documentación para manejo de MapReduce con MRJOB.

## Importante

Si quiere realizar las pruebas como en el documento es necesario que active el ambiente virtual donde estan las dependencias de python, para esto debe ejecutar el siguiente comando:

```bash
source venv/bin/activate
pip install -r requirements.txt
```

El archivo requirements.txt contiene las dependencias necesarias para ejecutar el programa.
Este se encuentra en la raiz del repositorio.

## 1.1 Se tiene un conjunto de datos, que representan el salario anual de los empleados formales en Colombia por sector económico, según la DIAN.

### Realizar un programa en Map/Reduce, con hadoop en Python o Java, que permita calcular:

1. El salario promedio por Sector Económico (SE)
2. El salario promedio por Empleado
3. Número de SE por Empleado que ha tenido a lo largo de la estadística

   El conjunto de datos se encuentra [aquí](https://github.com/jpcortesg1/ST0263/blob/main/Reto5/Reto%205.3/empleados/dataempleados.txt)

   El programa se encuentra [aquí](https://github.com/jpcortesg1/ST0263/blob/main/Reto5/Reto%205.3/empleados/main.py)

   Para ejecutar el archivo main.py se debe ejecutar el siguiente comando:

   ```bash
   python main.py dataempleados.txt > result.txt
   ```

   (En caso de que python no sea para ejecutar puede ser python3)

   Ahora en el archivo result.txt se encuentra el resultado de la ejecución del programa.

   En este caso pueden existir tres tipos de lines

   ```
   "Average Salary By SE 5434:"	36000.0
   "Average Salary By Emp 1115:"	62333.333333333336
   "SE number that had EMP 1115:"	2
   ```

   El primero indica el salario promedio por sector económico, el segundo el salario promedio por empleado y el tercero el número de sectores económicos que ha tenido el empleado. Para ver el resultado puede [visitar](https://github.com/jpcortesg1/ST0263/blob/main/Reto5/Reto%205.3/empleados/result.txt)

## 1.2 Se tiene un conjunto de acciones de la bolsa, en la cual se reporta a diario el valor promedio por acción.

### Realizar un programa en Map/Reduce, con hadoop en Python o Java, que permita calcular:

1. Por acción, dia-menor-valor, día-mayor-valor
2. Listado de acciones que siempre han subido o se mantienen estables.
3. DIA NEGRO: Saque el día en el que la mayor cantidad de acciones tienen el menor valor de acción (DESPLOME), suponga una inflación independiente del tiempo.

   El conjunto de datos se encuentra [aquí](https://github.com/jpcortesg1/ST0263/blob/main/Reto5/Reto%205.3/empresas/dataempresas.txt)

   El programa se encuentra [aquí](https://github.com/jpcortesg1/ST0263/blob/main/Reto5/Reto%205.3/empresas/main.py)

   Para ejecutar el archivo main.py se debe ejecutar el siguiente comando:

   ```bash
   python main.py dataempresas.txt > result.txt
   ```

   (En caso de que python no sea para ejecutar puede ser python3)

   Ahora en el archivo result.txt se encuentra el resultado de la ejecución del programa.

   En este caso pueden existir tres tipos de lines

   ```
   "EPM - Lowest Value Day:"	"2015-01-02"
   "EPM - Highest Value Day:"	"2015-01-01"
   "Black Day:"	"2015-01-02"
   "exito - Always Up or Stable:"	true
   ```

   El primero representa el día con menor valor, el segundo el día con mayor valor el tercero el día negro y el cuarto representa si la acción siempre ha estado subiendo. Para ver el resultado puede [visitar](https://github.com/jpcortesg1/ST0263/blob/main/Reto5/Reto%205.3/empresas/result.txt)

## 1.3 Sistema de evaluación de películas.

### Realizar un programa en Map/Reduce, con hadoop en Python o Java, que permita calcular:

1. Número de películas vista por un usuario, valor promedio de calificación
2. Día en que más películas se han visto
3. Día en que menos películas se han visto
4. Número de usuarios que ven una misma película y el rating promedio
5. Día en que peor evaluación en promedio han dado los usuarios
6. Día en que mejor evaluación han dado los usuarios
7. La mejor y peor película evaluada por genero

   El conjunto de datos se encuentra [aquí](https://github.com/jpcortesg1/ST0263/blob/main/Reto5/Reto%205.3/peliculas/datapeliculas.txt)

   El programa se encuentra [aquí](https://github.com/jpcortesg1/ST0263/blob/main/Reto5/Reto%205.3/peliculas/main.py)

   Para ejecutar el archivo main.py se debe ejecutar el siguiente comando:

   ```bash
   python main.py datapeliculas.txt > result.txt
   ```

   (En caso de que python no sea para ejecutar puede ser python3)

   Ahora en el archivo result.txt se encuentra el resultado de la ejecución del programa.

   En este caso pueden existir tres tipos de lines

   ```
   "276"	[2, 2.0, "N MOV SEE BY US, AVR RTG"]
   "Max Date"	["2014-03-20", 11]
   "Min Date"	["2014-03-21", 5]
   "387"	[1, 5.0, "N US that see a MV, AVR RTG"]
   "Min Rating Date"	["2014-03-20", 2.6363636363636362]
   "Max Rating Date"	["2014-03-21", 3.8]
   "accion"	3.1875
   ```

   El primero representa, numero de peliculas vista por usuario y valor promedio de calificación, el segundo representa el dia que más peliculas se ha visto, el tercero el día que menos peliculas se han visto, el cuarto el numero de usuarios que ven una misma pelicula y rating promedio, el quinto el día con peor evaluación, el sexto el día con mejor evaluación y el 7 el rating promedio por genero. Para ver el resultado puede [visitar](https://github.com/jpcortesg1/ST0263/blob/main/Reto5/Reto%205.3/peliculas/result.txt)

# Universidad EAFIT

# Laboratior 5.3

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

# 2 Documentación para Wordcount en Apache Spark EN AWS EMR

## Importante

Para poder hacer estos ejercicios es necesarios poder crear un cluster de EMR en aws y tener acceso a este para conectarse mediante ssh. Si quieres crear un cluster con estas carectiristicas puedes [ver](https://github.com/jpcortesg1/ST0263/tree/main/Reto5/Reto%205.1)

También es ncesario conocer sobre gestion de archivos HDFS y S3 vía HUE y SSH, para esto puedes ver [ver](https://github.com/jpcortesg1/ST0263/tree/main/Reto5/Reto%205.2)

Luego es necesario tener en HDFS y S3 los siguientes archivos [data1](https://github.com/jpcortesg1/ST0263/blob/main/Reto5/Reto%205.3/02-mapreduce/data1.txt), [data2](https://github.com/jpcortesg1/ST0263/blob/main/Reto5/Reto%205.3/02-mapreduce/data2.txt)

Esto se hace siguiendo los pasos del [repositorio](https://github.com/jpcortesg1/ST0263/tree/main/Reto5/Reto%205.2)

## 2.1 Ejecutar el wordcount por linea de comando 'pyspark' INTERACTIVO en EMR con datos en HDFS vía ssh en el nodo master.

Primero se hace una conexión ssh al nodo master. Debe tener algo así:

<img src="https://user-images.githubusercontent.com/60229777/239617770-d884c227-aa2d-4d80-9b42-2bdcf0e36c49.png">

Luego ejecutamos el comando pyspark para entrar al shell de pyspark:
<img src="https://user-images.githubusercontent.com/60229777/239618108-ff14fafe-89b9-410e-b8ae-0f1eb740c73f.png">

Luego corremos el siguiente código para hacer el wordcount:

```python
# Conéctate al nodo master del clúster EMR a través de ssh
# Inicia una sesión interactiva de PySpark ejecutando el comando `pyspark` en la línea de comandos

# Lee los datos desde HDFS
data = sc.textFile("hdfs:///input.txt")

# Realiza el wordcount
counts = data.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)

# Muestra los resultados
output = counts.collect()
for (word, count) in output:
    print("%s: %i" % (word, count))
```
La salida para data1:
<img src="https://user-images.githubusercontent.com/60229777/239619102-a8c29fd1-b8f3-4bce-9a22-21eb4620eee8.png">

La salida para data2:
<img src="https://user-images.githubusercontent.com/60229777/239619102-a8c29fd1-b8f3-4bce-9a22-21eb4620eee8.png">

## 2.2 Ejecutar el wordcount por linea de comando 'pyspark' INTERACTIVO en EMR con datos en S3 (tanto de entrada como de salida)  vía ssh en el nodo master.

Primero se hace una conexión ssh al nodo master. Debe tener algo así:

<img src="https://user-images.githubusercontent.com/60229777/239617770-d884c227-aa2d-4d80-9b42-2bdcf0e36c49.png">

Luego ejecutamos el comando pyspark para entrar al shell de pyspark:
<img src="https://user-images.githubusercontent.com/60229777/239618108-ff14fafe-89b9-410e-b8ae-0f1eb740c73f.png">

Luego corremos el siguiente código para hacer el wordcount:

```python
# Conéctate al nodo master del clúster EMR a través de ssh
# Inicia una sesión interactiva de PySpark ejecutando el comando `pyspark` en la línea de comandos

# Lee los datos desde S3
data = sc.textFile("s3a://my-bucket/input.txt")

# Realiza el wordcount
counts = data.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)

# Guarda los resultados en S3
counts.saveAsTextFile("s3a://my-bucket/output")
```

Debemos ver algo así:
### data 1
<img src="https://user-images.githubusercontent.com/60229777/239628421-fd30ad62-5759-4930-b708-7dcf1c41b73e.png">

### data 2
<img src="https://user-images.githubusercontent.com/60229777/239629142-739a06ea-1e59-4d9e-aa7d-c0fb83207e8a.png">

Para verificar que se guardo en s3, podemos ir a la interfaz de aws o hub y verificar que el output este, debemos ver algo así:
<img src="https://user-images.githubusercontent.com/60229777/239628473-3db1ecc1-4d67-4742-95f1-d8119ee3d323.png">
<img src="https://user-images.githubusercontent.com/60229777/239628519-2af3648a-98bb-4f12-91eb-92a1d377ed8b.png">

### data 2
<img src="https://user-images.githubusercontent.com/60229777/239629142-739a06ea-1e59-4d9e-aa7d-c0fb83207e8a.png">

Para verificar que se guardo en s3, podemos ir a la interfaz de aws o hub y verificar que el output este, debemos ver algo así:
<img src="https://user-images.githubusercontent.com/60229777/239629082-e693136f-d7b4-4128-898d-bd1b0d0769ce.png">
<img src="https://user-images.githubusercontent.com/60229777/239629116-4a06e8f7-eb69-4c3d-aea9-593deb912330.png">

(En las imagenes solo se enseña un archivo de los dos que salen al correr el código, para ver el otro pueden visitar el bucket y ver ambos archivos)

## 2.3 Ejecutar el wordcount en JupyterHub Notebooks EMR con datos en S3 (tanto datos de entrada como de salida) usando un clúster EMR.

Para este paso debemos inicar sesión en Jupyter Hub, para hacerlo, puedes [leer](https://github.com/jpcortesg1/ST0263/tree/main/Reto5/Reto%205.1)

Luego de iniciar sesión, debemos crear un nuevo notebook, para esto, damos click en new y luego en pyspark.

Este archivo debe verse así:
<img src="https://user-images.githubusercontent.com/60229777/239633134-71a46d33-aa4d-4a54-9548-b9e5fa81d494.png">

Para verificar podemos ver algo así:
<img src="https://user-images.githubusercontent.com/60229777/239633158-99035606-0c47-49dc-a869-ebf3ef7353eb.png">

Para verificar la data2 debemos hacer lo mismo.

# Universidad EAFIT

# ST0263 TÓPICOS ESPECIALES EN TELEMÁTICA, 2023-1

# Laboratior 5.2

## Juan Pablo Cortes Gonzalez

## 10 de Mayo del 2033

## Documentación para la gestión de archivos hacia HDFS y S3 vía HUE y SSH

cómo gestionar archivos hacia los sistemas de archivos distribuidos HDFS y S3 utilizando las herramientas HUE y SSH. La documentación detallará los pasos necesarios para llevar a cabo la transferencia de archivos de manera eficiente y efectiva.

## 1. CONECTARSE AL CLUSTER AMAZON EMR:

Para conectarse al cluster, debemos ir a la sección "Administración de clústeres", presionamos en "Conectarse al nodo principal mediante SSH", copiamos y pegamos la sentencia que hay en alguna terminal.
Debemos ver algo así.
<img src="https://user-images.githubusercontent.com/60229777/237524013-20689360-fd73-4966-8f66-912c65689066.png">

## 2. Clonación del dataset.

Para clonar el dataset, debemos ejecutar el siguiente comando:

```
git clone https://github.com/st0263eafit/st0263-231.git
```

En caso de no tener git instalado, debemos ejecutar el siguiente comando:

```
sudo yum install git
```

Para mover los datset a la carpeta de trabajo, debemos ejecutar el siguiente comando:

```
 mv /home/hadoop/st0263-231/bigdata/datasets /home/hadoop
```

## 3. GESTIÓN DE ARCHIVOS EN HDFS VÍA HUE.

Para crear un usuario y contraseña y primeros pasos de HUE puede ver [Documentación Servicios Cluster](https://github.com/jpcortesg1/ST0263/tree/main/Reto5/Reto%205.1#ahora-vamos-a-probar-los-servicios).

Para subir un archivo vía HUE, buscamos en la barra lateral la sección files, entramos a esta y aquí tenemos la interfaz para subir archivos.

En este caso vamos a subir los archivos a una carpeta llamada datasets

<img src="https://user-images.githubusercontent.com/60229777/237526261-0d18934c-5753-4acd-aa65-678cef48282f.png">

Para subir archivos, solo debemos arrastrarlos a la interfaz o seleccionarlos. Y estos quedan almacenados en mi caso subire 5 carpetas y un archivo.

<img src="https://user-images.githubusercontent.com/60229777/237526516-c36eeb0f-94ab-42f3-ad37-baec44771e1c.png">

Al arrastrarlos a la interfaz debemos ver algo así.

<img src="https://user-images.githubusercontent.com/60229777/237526656-64a9146e-8af0-436b-8d2a-abb7a0ede5d7.png">
<img src="https://user-images.githubusercontent.com/60229777/237526685-a357d3a1-4421-4941-bd7d-178409b942d3.png">

Para verificar lo podemos hacer en la consola ejecutando:

```
user@master$ hdfs dfs -ls /
user@master$ hdfs dfs -ls /user
user@master$ hdfs dfs -ls /user/<username>
user@master$ hdfs dfs -ls /user/<username>/datasets
```

Debemos ver algo similar a esto:
<img src="https://user-images.githubusercontent.com/60229777/237527171-ee844dc4-50b4-4c71-999c-cc7ddf4de5f3.png">

Aqui podemos ver que los archivos se subieron correctamente.

## 4. GESTIÓN DE ARCHIVOS EN HDFS VÍA SSH.

Como anteriormente clonamos e hicimos un proceso para tener los datasets de modo local, ahora vamos a subirlos a HDFS vía SSH.
Para verificar que los archivos estan en la carpeta de trabajo, debemos ejecutar el siguiente comando:

```
ls
ls datasets
```

Debemos ver algo similar a esto:

<img src="https://user-images.githubusercontent.com/60229777/237527491-b2dc6fe8-50aa-4b6e-92be-e890c405b2ec.png">

Como podemos ver nos faltan algunos archivos y carpetas:
/all-news
/covid19
/flights
/gutenberg
sample_data.csv

Para gestionar archivos en HDFS vía SSH, debemos ejecutar los siguientes comandos:

```
hdfs dfs -put /home/hadoop/datasets/sample_data.csv /user/hadoop/datasets
hdfs dfs -put /home/hadoop/datasets/all-news /user/hadoop/datasets
hdfs dfs -put /home/hadoop/datasets/covid19 /user/hadoop/datasets
hdfs dfs -put /home/hadoop/datasets/flights /user/hadoop/datasets
hdfs dfs -put /home/hadoop/datasets/gutenberg /user/hadoop/datasets
```

Para verificar que los archivos se subieron correctamente, debemos ejecutar el siguiente comando:

```
user@master$ hdfs dfs -ls /
user@master$ hdfs dfs -ls /user
user@master$ hdfs dfs -ls /user/<username>
user@master$ hdfs dfs -ls /user/<username>/datasets
```

Y podemos ver la interfaz de HUE, que los archivos se subieron correctamente.
Debemos ver algo similar a esto:

<img src="https://user-images.githubusercontent.com/60229777/237528598-97e2217f-abcc-45fe-b7a0-94982e603f01.png">
<img src="https://user-images.githubusercontent.com/60229777/237528520-c8777c06-c8fe-4459-bb33-fe5907c8b43b.png">

## 5. GESTIÓN DE ARCHIVOS EN S3 VÍA HUE.

Para tener la persistencia en S3, es necesario tener creado este y tenerlo enlazado a nuestro cluster.
Para más info visitar [Documentación para creación de cluster AWS EMR en Amazon.](https://github.com/jpcortesg1/ST0263/tree/main/Reto5/Reto%205.1)

Para subir un archivo vía HUE, buscamos en la barra lateral la sección S3, entramos a esta y aquí tenemos la interfaz para subir archivos.

En este caso mi bucket se llama notebookjpcortesg, y voy a subir los archivos a una carpeta llamada datasets.

<img src="https://user-images.githubusercontent.com/60229777/237529289-c1da82ce-0031-43ba-bc85-4106924041ad.png">

Para subir archivos, solo debemos arrastrarlos a la interfaz o seleccionarlos. Y estos quedan almacenados en mi caso subire 5 carpetas y un archivo.

<img src="https://user-images.githubusercontent.com/60229777/237526516-c36eeb0f-94ab-42f3-ad37-baec44771e1c.png">

Al arrastrarlos a la interfaz debemos ver algo así.

<img src="https://user-images.githubusercontent.com/60229777/237529532-94adf359-5adf-4021-91c9-daca0afa81f6.png">
<img src="https://user-images.githubusercontent.com/60229777/237529552-483d46f8-7859-4421-8a9d-755256168004.png">

Para verificar en nuestro bucket.

Debe quedar algo similar a esto:
<img src="https://user-images.githubusercontent.com/60229777/237529782-bc87bbf4-74d8-4ae5-aedd-6d49eba3bc1e.png">

## 6. GESTIÓN DE ARCHIVOS EN S3 VÍA SSH.

Como anteriormente clonamos e hicimos un proceso para tener los datasets de modo local, ahora vamos a subirlos a S3 vía SSH.
Para verificar que los archivos estan en la carpeta de trabajo, debemos ejecutar el siguiente comando:

```
ls
ls datasets
```

Debemos ver algo similar a esto:

<img src="https://user-images.githubusercontent.com/60229777/237527491-b2dc6fe8-50aa-4b6e-92be-e890c405b2ec.png">

Como podemos ver nos faltan algunos archivos y carpetas:
/all-news
/covid19
/flights
/gutenberg
sample_data.csv

Para gestionar archivos en S3 vía SSH, debemos ejecutar los siguientes comandos:

```
$ aws s3 cp /home/hadoop/datasets/all-news s3://notebookjpcortesg/datasets/ --recursive
$ aws s3 cp /home/hadoop/datasets/covid19 s3://notebookjpcortesg/datasets/ --recursive
$ aws s3 cp /home/hadoop/datasets/flights s3://notebookjpcortesg/datasets/ --recursive
$ aws s3 cp /home/hadoop/datasets/gutenberg s3://notebookjpcortesg/datasets/ --recursive
```

Debemos ver algo similar a esto:

<img src="https://user-images.githubusercontent.com/60229777/237530596-99b57e09-bd53-4ce1-a48c-7325a34c9543.png">

Para verificar que los archivos se subieron correctamente, podemos ir a la interfaz de S3 y verificar que los archivos se subieron correctamente.

<img src="https://user-images.githubusercontent.com/60229777/237530714-a7ca961e-0cee-4a93-866d-47b009e6a53a.png">

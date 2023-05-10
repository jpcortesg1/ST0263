# Universidad EAFIT
# ST0263 TÓPICOS ESPECIALES EN TELEMÁTICA, 2023-1
# Laboratior 5.1

## Juan Pablo Cortes Gonzalez
## 10 de Mayo del 2033
## Documentación para creación de cluster AWS EMR en Amazon.

Amazon EMR (Elastic MapReduce) es un servicio web que permite a empresas, investigadores, analistas de datos y desarrolladores procesar grandes cantidades de datos de manera rápida y rentable. Con Amazon EMR, puedes crear y gestionar clústeres de Amazon EC2 (Elastic Compute Cloud) que ejecutan aplicaciones de procesamiento de datos como Apache Spark, Apache Hive y Apache Hadoop.

## Paso a paso.

### 1. Crear cluster.

Inicie sesión en su cuenta de AWS Academy y navegue hasta el servicio Amazon EMR. Una vez allí, en la sección de clústeres, haga clic en el botón “Create cluster” para comenzar el proceso de creación de un nuevo clúster.

Para conectarse a las instancias EC2 de un clúster de Amazon EMR mediante SSH, es necesario tener un par de claves EC2. Un par de claves consta de una clave pública y una clave privada. La clave pública se almacena en las instancias EC2 y la clave privada se guarda en su equipo local. Al conectarse a una instancia EC2 mediante SSH, se utiliza la clave privada para autenticarse con la clave pública almacenada en la instancia.

Si aún no tiene un par de claves EC2, puede crear uno en la consola de EC2 antes de crear su clúster de Amazon EMR. Durante el proceso de creación del clúster, deberá seleccionar el par de claves que desea utilizar para conectarse a las instancias del clúster mediante SSH.

<img src="https://user-images.githubusercontent.com/60229777/237246225-fa5f3fd7-f979-476d-80de-7f37f27e1f6f.png">

### 2. Crear cluster.

Para crear el cluster, es necesario una configuración basica:
 + En la sección "Versión de Amazon EMR", seleccionamos "6.3.1".
 + En la sección "Paquete de aplicaciones", seleccionamos Custom.
 + En la sección "Personalizar el paquete de aplicaciones", seleccionamos:

    * HCatalog 3.1.2
    * Hadoop 3.2.1
    * Hive 3.1.2
    * Hue 4.9.0
    * JupyterEnterpriseGateway 2.1.0
    * JupyterHub 1.2.0
    * Livy 0.7.0
    * Spark 3.1.1
    * Sqoop 1.4.7
    * Tez 0.9.2
    * Zeppelin 0.9.0

+ En la sección "Grupos de instancias", debe quedar.

    * Principal: m4.xlarge
    * Central: m4.xlarge
    * En caso de que este "Tarea 1 de 1", se presiona en "eliminar grupo de instancias".

+ En la seccion "Volumen raíz de EBS - opcional", establecemos un volumen de 20 GiB.

+ En la sección "Opción de aprovisionamiento y escalado de clústeres", dejamos en central, en la parte tamaño, 2.

+ En la sección "Terminación del clúster", seleccionamos "Terminar el clúster después del tiempo de inactividad (recomendado)" y en "Tiempo de inactividad" en el apartado horas, lo establecemos en una hora.

+ En la sección "Editar la configuración de software: opcional", para la persistencia de jupyter, seleccionamos "ingresar la configuración", e insertamos:

    ```
    [
        {
            "Classification": "jupyter-s3-conf",
            "Properties": {
                "s3.persistence.enabled": "true",
                "s3.persistence.bucket": "MyJupyterBackups"
            }
        }
    ]
    ```

+ En la sección "Configuración y permisos de seguridad", ingresamos nuestra llave previamente creada, y descargada. En la sección "Par de claves de Amazon EC2 para el protocolo SSH al clúster - opcional", esto con el fin de poder hacer la conexión por ssh.

+ En la sección "Roles de Identity and Access Management (IAM)" seleccionamos:

    * En "Rol de servicio", ingresamos "EMR_DefaultRole".
    * En "Perfil de instancia", ingresamos "EMR_EC"_DefaultRole".

### Al finalizar esta configuración presionamos crear cluster.
Luego de crear el cluster, hay que esperar un lapso de 15 a 25 minutos para que este se levante y se configure, al final debemos ver algo así.

Debemos ver algo así:

<img src="https://user-images.githubusercontent.com/60229777/237250465-859fa8fb-55e1-429f-afd8-faed3b2307bc.png">
<img src="https://user-images.githubusercontent.com/60229777/237250467-9056f2e0-b626-48c0-9cfd-0eb91f6b9f1b.png">

## Luego de crear el cluster y este pase al estado esperando terminamos con algunas configuraciones.

* Vamos a la sección de "bloquear el acceso al publico", la activamos, e ingresamos los puertos:
    * 22, para el ssh.
    * 8888, para Hue. 
    * 9443, para el Jupyter.
    * 8090, para el Zeepelin.

    Debe quedar algo así.
    <img src="https://user-images.githubusercontent.com/60229777/237250735-958f317c-84cf-46c2-aa0e-3b10eacfd96f.png">

* Vamos a la sección "Red y seguridad", dentro del cluster, presionamos en "Grupos de seguridad de EC2 (firewall)", allí ingresamos al link del "node principal". 
En la sección "Reglas de entrada" presionamos "editar reglas de entrada".
Allí ingresamos los puertos ingresados anteriormente:
    * 22, para el ssh.
    * 8888, para Hue. 
    * 9443, para el Jupyter.
    * 8090, para el Zeepelin.

    Todos con la opción TCP personalizado - anywhere - 0.0.0.0/0

    Debe quedar algo así.
    <img src="https://user-images.githubusercontent.com/60229777/237250732-2ceb73d0-1a2c-4a7c-b059-562e053b78c3.png">
 
 * Para la configuración anterior es necesario crear el bucket anterior, por eso en caso de no tenerlo es necesario crearlo. Buscamos "S3" en la barra de busqueda. Presionamos "Crear bucket", ingresamos el nombre y presionamos en "crear Bucket"
 
     Nos debe quedar algo así:
     <img src="https://user-images.githubusercontent.com/60229777/237250733-08764053-a474-4128-8079-4452336fbf56.png">

## Ahora vamos a probar los servicios:

* Primero vamos a conectarnos por consola, para esto, vamos a "Administración de clústeres" dentro del cluster y presionamos "Conectarse al nodo principal mediante SSH", esto nos abrira un Pop Up, con la información que se debe poner en la consola local, copiamos y pegamos y al ejecutar se nos debe ver algo así.
<img src="https://user-images.githubusercontent.com/60229777/237250729-568ed36d-02ea-4be3-a040-3fdf002d8aa0.png">

* Primero entraremos al Hue. Seleccionamos la URl de este en el apartado "aplicaciones". Al abrirse este nos pedira crear un usuario y una contraseña, lo hacemos e ingresamos.
<img src="https://user-images.githubusercontent.com/60229777/237252760-170d2974-0876-4195-8a34-4011e1286505.png">

    Ahora la interfaz dentro de este debe ser algo así:
    <img src="https://user-images.githubusercontent.com/60229777/237252765-a11c7d87-d7e6-4f1e-98b4-5344d9e7b66b.png">

    Podemos porbar seleccionando en la barra lateral, en la sección editor, damos en hive. y ejecutamos

    ```
    show databases;
    ```
    Debemos ver algo así:
    <img src="https://user-images.githubusercontent.com/60229777/237252766-20946cc9-e2e2-402f-aeaf-22ca7222216d.png">

* Ahora probamos el Jupyterhub, ingresamos a la url, desde la sección aplicaciones del cluster. Y debemos ver algo así.

    <img src="https://user-images.githubusercontent.com/60229777/237252768-f0c41ea6-ed7b-4868-b6d6-94de264231ad.png">

    Ingresamos de username: jovyan
    Ingresamos de password: jupyter

    Luego debemos ver algo así al ingresar:
    <img src="https://user-images.githubusercontent.com/60229777/237252770-70580ba4-33cc-42c4-b782-220b0bab0fa3.png">  

    Creamos un nuevo archivo, dandole en el botton "new" y seleccionamos "PySpark".
    Para probar este ejecutamos lo siguiente:
    <img src="https://user-images.githubusercontent.com/60229777/237252770-70580ba4-33cc-42c4-b782-220b0bab0fa3.png">

* Luego podemos ingresar a Zeepelin, ingresando a la url que nos brinda el cluster, en la sección aplicaciones. Y debemos ver algo así.

<img src="https://user-images.githubusercontent.com/60229777/237252774-dfe52b12-510f-431c-ad17-fd403bfbb74d.png">

* Para probar que tenemos la persistencia de datos, vamos al hub en la sección de S3, y allí podemos ver:
<img src="https://user-images.githubusercontent.com/60229777/237252776-d5214aba-9956-4aa1-a373-49fe00cabc15.png">

* Para bajar el cluster, seleccionamos el cluster y presionamos en "terminar".
Debemos ver algo así:
<img src="https://user-images.githubusercontent.com/60229777/237252777-9e34ac1e-b296-48c2-8c3c-6ccdcc6795fb.png">

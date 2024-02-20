# CAJERO AUTOMATICO POR CONSOLA EN PYTHON

En un principio, se le pedira al usuario el tipo de perfil con el que quiere ingresar al programa:

![image](https://github.com/Barriose01/CajeroAutomaticoSimplePython/assets/107152796/ca6cdac4-76f9-4b52-8de5-cfdf32b00a91)

> El "Usuario normal" tendra acceso a las principales funciones del cajero (retiro, deposito, etc)
> El usuario "Admin" tendra acceso a los registros de transacciones del cajero automatico

## Usuario normal

El usuario normal tendra acceso a las siguientes operaciones:

![image](https://github.com/Barriose01/CajeroAutomaticoSimplePython/assets/107152796/4b7c18c5-08ea-4b8b-8001-c223875fa73c)

### Retiro

Permite realizar retiros al saldo que posee el usuario 

![image](https://github.com/Barriose01/CajeroAutomaticoSimplePython/assets/107152796/5ec7ce18-378c-46a7-b496-1729e2e55602)

Al tener saldo y seleccionar una opcion, se restara el saldo por la opcion seleccionada

> Se hizo un deposito para este ejemplo. Se selecciona la opcion de la consulta de saldo
 ![image](https://github.com/Barriose01/CajeroAutomaticoSimplePython/assets/107152796/b347009f-6ff5-41aa-b751-96df2885b281)
 ![image](https://github.com/Barriose01/CajeroAutomaticoSimplePython/assets/107152796/58360af3-4819-4730-a33a-4931b8657bc9)
 ![image](https://github.com/Barriose01/CajeroAutomaticoSimplePython/assets/107152796/9ba5b550-c356-4680-b227-723bf3f0bed4)

Tambien se puede ingresar un monto especifico para realizar un retiro:

![image](https://github.com/Barriose01/CajeroAutomaticoSimplePython/assets/107152796/88b7a50e-cb9a-470d-ae13-196d310237b5)
![image](https://github.com/Barriose01/CajeroAutomaticoSimplePython/assets/107152796/23e3c1a3-ea39-4ecb-8ce3-79c3752b0532)
![image](https://github.com/Barriose01/CajeroAutomaticoSimplePython/assets/107152796/2207ac4e-f9e6-4983-a438-400f92c4dbac)

### Deposito

Se selecciona la opcion del deposito y se ingresa un monto:

> Se usa el mismo saldo del caso anterior

![image](https://github.com/Barriose01/CajeroAutomaticoSimplePython/assets/107152796/f319ed55-02b1-4736-877c-53633e6257a3)
![image](https://github.com/Barriose01/CajeroAutomaticoSimplePython/assets/107152796/8e9d2fa2-e69b-4df7-8701-e15c7c1a15a0)
![image](https://github.com/Barriose01/CajeroAutomaticoSimplePython/assets/107152796/25c61c91-456d-4ad9-9b21-27c65f095f58)

### Consulta de saldo

Sirve para observar el saldo del usuario:

![image](https://github.com/Barriose01/CajeroAutomaticoSimplePython/assets/107152796/6df5f72b-0a02-4a3e-bd1b-de512db224d4)


### Salir

Permite regresar a las opciones anteriores (Seleccion de perfiles de usuario):

![image](https://github.com/Barriose01/CajeroAutomaticoSimplePython/assets/107152796/a5893f8a-cab6-4fda-baf0-0b33503e9d9d)

## Admin

El usuario Admin tiene acceso a los registros de transacciones. Podra revisarlos y eliminarlos:

![image](https://github.com/Barriose01/CajeroAutomaticoSimplePython/assets/107152796/8ed5cb2c-54d3-4b9c-a940-58d6dcb541b0)

### Revisar registro de transacciones

Lee el archivo generado con las transacciones realizadas por todos los usuarios:

![image](https://github.com/Barriose01/CajeroAutomaticoSimplePython/assets/107152796/436a5d48-3c71-4c07-bb7c-4ebb8ef47f98)

> Se leen los registros de un archivo de texto

![image](https://github.com/Barriose01/CajeroAutomaticoSimplePython/assets/107152796/9ab0ecd9-dff2-436a-9732-7883bfb1a3db)


### Eliminar registro de transacciones

Permite eliminar los registros de transacciones

![image](https://github.com/Barriose01/CajeroAutomaticoSimplePython/assets/107152796/f01ec454-f19a-4118-9976-ddecce17a51f)

> Si se selecciona la opcion (Y), se eliminaran los registros

![image](https://github.com/Barriose01/CajeroAutomaticoSimplePython/assets/107152796/56149fcb-f97b-4aa8-93bf-1cfac7a0481b)

> Si se observa el archivo de texto, ya no tendra registros:

![image](https://github.com/Barriose01/CajeroAutomaticoSimplePython/assets/107152796/dc4576cf-8657-4a93-95ac-aa3117323ca2)

> Si se intenta leer el archivo de texto, indicara que no tiene registros:

![image](https://github.com/Barriose01/CajeroAutomaticoSimplePython/assets/107152796/2f5b52f4-d6cd-45db-b2c4-ddbca154fcaf)

### Salir

Permite salir del perfil de Admin para llegar al menu principal de seleccion de perfiles:

![image](https://github.com/Barriose01/CajeroAutomaticoSimplePython/assets/107152796/e71ee11e-d637-4115-b749-62ac03e64d66)




















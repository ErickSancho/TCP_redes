# TCP_redes

Este proyecto consiste en el diseño de una comunicación sencilla de cliente-servidor en TCP con 3-way handshake. Permite enviar un string de caracteres en minúscula y recibe la respuesta de los caracteres en mayuscula. 

El IP utilizado para probar el programa es: 127.0.0.1
El puerto utilizado es: 5000 (aunque se probó con 4000,6000,7000)

El cliente puede desconectarse y volver a conectarse al servidor sin inconvenientes. Pueden llegar más clientes en cola y a penas el cliente que utiliza el servidor lo desocupe, uno de los clientes en espera toma el espacio. 

Se añade también que al realizar ctrl+c se cierre el servidor. 

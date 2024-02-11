nombre: str = input("Por favor ingrese su nombre: ")
apellidos: str = input("por favor ingrese sus apellidos: ")
telefono: str = input("Por favir ingrese su número de telefono: ")
correo: str = input("Por favor ingrese su correo: ")

bienvenida: str = f"Hola {nombre} {apellidos}, en breve recibirás un correo a {correo}"
print(bienvenida)
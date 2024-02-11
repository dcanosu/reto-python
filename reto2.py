num_usuarios: int = int(input("Por favor ingrese la cantidad de usuarios que desea registrar: "))

for i in range(num_usuarios):    
    nombre: str = input("Por favor ingrese su nombre: ")
    while not (5 <= len(nombre) <= 50):
        print("Nombre inválido. Debe tener entre 5 y 50 caracteres.")
        nombre: str = input("Por favor ingrese su nombre: ")

    apellidos: str = input("por favor ingrese sus apellidos: ")
    while not (5 <= len(nombre) <= 50):
        print("Apellidos inválidos. Deben tener entre 5 y 50 caracteres.")
        apellidos: str = input("por favor ingrese sus apellidos: ")
        
    telefono: str = input("Por favir ingrese su número de telefono: ")
    while not (len(telefono) == 10 and telefono.isdigit()):
        print("Número de teléfono inválido. Debe tener 10 dígitos.")
        telefono = input("Por favor ingrese su número de teléfono: ")
        
    correo: str = input("Por favor ingrese su correo: ")
    while not (5 <= len(correo) <= 50 and '@' in correo and '.' in correo):
        print("Correo electrónico inválido. Debe tener entre 5 y 50 caracteres y ser válido.")
        correo = input("Por favor ingrese su correo: ")
        
    bienvenida: str = f"Hola {nombre} {apellidos}, en breve recibirás un correo a {correo}"
    print(bienvenida)
    
# con funciones
def validar_nombre(nombre):
    return 5 <= len(nombre) <= 50

def validar_apellidos(apellidos):
    return 5 <= len(apellidos) <= 50

def validar_telefono(telefono):
    return len(telefono) == 10 and telefono.isdigit()

def validar_correo(correo):
    return 5 <= len(correo) <= 50 and '@' in correo and '.' in correo

num_usuarios = int(input("Por favor ingrese la cantidad de usuarios que desea registrar: "))

for i in range(num_usuarios):
    nombre = input("Por favor ingrese su nombre: ")
    while not validar_nombre(nombre):
        print("Nombre inválido. Debe tener entre 5 y 50 caracteres.")
        nombre = input("Por favor ingrese su nombre: ")
    
    apellidos = input("Por favor ingrese sus apellidos: ")
    while not validar_apellidos(apellidos):
        print("Apellidos inválidos. Deben tener entre 5 y 50 caracteres.")
        apellidos = input("Por favor ingrese sus apellidos: ")
    
    telefono = input("Por favor ingrese su número de teléfono: ")
    while not validar_telefono(telefono):
        print("Número de teléfono inválido. Debe tener 10 dígitos.")
        telefono = input("Por favor ingrese su número de teléfono: ")
    
    correo = input("Por favor ingrese su correo: ")
    while not validar_correo(correo):
        print("Correo electrónico inválido. Debe tener entre 5 y 50 caracteres y ser válido.")
        correo = input("Por favor ingrese su correo: ")
    
    bienvenida = f"Hola {nombre} {apellidos}, en breve recibirás un correo a {correo}"
    print(bienvenida)


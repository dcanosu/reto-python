print("-"*60)
num_usuarios = int(input("Por favor ingrese la cantidad de usuarios que desea registrar: "))
print("-"*60)
usuarios = []

for i in range(num_usuarios):
    print("*"* 60)
    nombre = input("Por favor ingrese su nombre: ")
    while not (5 <= len(nombre) <= 50):
        print("Nombre inválido. Debe tener entre 5 y 50 caracteres.")
        nombre = input("Por favor ingrese su nombre: ")
    
    apellidos = input("Por favor ingrese sus apellidos: ")
    while not (5 <= len(apellidos) <= 50):
        print("Apellidos inválidos. Deben tener entre 5 y 50 caracteres.")
        apellidos = input("Por favor ingrese sus apellidos: ")
    
    telefono = input("Por favor ingrese su número de teléfono: ")
    while not (len(telefono) == 10 and telefono.isdigit()):
        print("Número de teléfono inválido. Debe tener 10 dígitos.")
        telefono = input("Por favor ingrese su número de teléfono: ")
    
    correo = input("Por favor ingrese su correo: ")
    while not (5 <= len(correo) <= 50 and '@' in correo and '.' in correo):
        print("Correo electrónico inválido. Debe tener entre 5 y 50 caracteres y ser válido.")
        correo = input("Por favor ingrese su correo: ")
    
    usuarios.append({
        'id': len(usuarios) + 1,
        'nombre': nombre,
        'apellidos': apellidos,
        'telefono': telefono,
        'correo': correo
    })

print("\nListado de usuarios registrados:")
for usuario in usuarios:
    print(f"ID: {usuario['id']}, Nombre: {usuario['nombre']}, Apellidos: {usuario['apellidos']}, Teléfono: {usuario['telefono']}, Correo: {usuario['correo']}")

usuarios = []

def new_user():
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
    print("Usuario registrado exitosamente.")

def show_user(user_id):
    for usuario in usuarios:
        if usuario['id'] == user_id:
            print(f"\nInformación del usuario con ID {user_id}:")
            print(f"Nombre: {usuario['nombre']}, Apellidos: {usuario['apellidos']}, Teléfono: {usuario['telefono']}, Correo: {usuario['correo']}")
            return
    print("No se encontró ningún usuario con el ID especificado.")

def edit_user(user_id):
    for usuario in usuarios:
        if usuario['id'] == user_id:
            print(f"\nEditando información del usuario con ID {user_id}:")
            nombre = input("Nuevo nombre: ")
            while not (5 <= len(nombre) <= 50):
                print("Nombre inválido. Debe tener entre 5 y 50 caracteres.")
                nombre = input("Por favor ingrese su nombre: ")
            
            apellidos = input("Nuevos apellidos: ")
            while not (5 <= len(apellidos) <= 50):
                print("Apellidos inválidos. Deben tener entre 5 y 50 caracteres.")
                apellidos = input("Por favor ingrese sus apellidos: ")
            
            telefono = input("Nuevo número de teléfono: ")
            while not (len(telefono) == 10 and telefono.isdigit()):
                print("Número de teléfono inválido. Debe tener 10 dígitos.")
                telefono = input("Por favor ingrese su número de teléfono: ")
            
            correo = input("Nuevo correo: ")
            while not (5 <= len(correo) <= 50 and '@' in correo and '.' in correo):
                print("Correo electrónico inválido. Debe tener entre 5 y 50 caracteres y ser válido.")
                correo = input("Por favor ingrese su correo: ")

            usuario['nombre'] = nombre
            usuario['apellidos'] = apellidos
            usuario['telefono'] = telefono
            usuario['correo'] = correo
            print("Información actualizada exitosamente.")
            return
    print("No se encontró ningún usuario con el ID especificado.")

def delete_user(user_id):
    for i, usuario in enumerate(usuarios):
        if usuario['id'] == user_id:
            del usuarios[i]
            print(f"Usuario con ID {user_id} eliminado exitosamente.")
            return
    print("No se encontró ningún usuario con el ID especificado.")

def list_users():
    print("\nListado de usuarios registrados:")
    for usuario in usuarios:
        print(f"ID: {usuario['id']}, Nombre: {usuario['nombre']}, Apellidos: {usuario['apellidos']}, Teléfono: {usuario['telefono']}, Correo: {usuario['correo']}")

menu_options = {
    'A': new_user,
    'B': list_users,
    'C': show_user,
    'D': edit_user,
    'E': delete_user,
}

while True:
    print("\nMenú de opciones:")
    print("A.) Registrar nuevo usuario")
    print("B.) Listar usuarios")
    print("C.) Consultar usuario por ID")
    print("D.) Editar información de usuario por ID")
    print("E.) Eliminar usuario por ID")
    print("F.) Salir del programa")
    opcion = input("Seleccione una opción: ").upper()

    if opcion == 'F':
        print("Gracias por utilizar el programa. ¡Hasta luego!")
        break
    
    if opcion not in menu_options:
        print("Opción inválida. Por favor seleccione una opción válida.")
        continue

    if opcion == 'C' or opcion == 'D' or opcion == 'E':
        user_id = int(input("Ingrese el ID del usuario: "))
        menu_options[opcion](user_id)
    else:
        menu_options[opcion]()

usuarios = []

while True:
    print("\nMenú de opciones:")
    print("A.) Registrar nuevo usuario")
    print("B.) Listar usuarios")
    print("C.) Consultar usuario por ID")
    print("D.) Editar información de usuario por ID")
    print("E.) Salir del programa")
    opcion = input("Seleccione una opción: ").upper()

    if opcion == 'A':
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

    elif opcion == 'B':
        print("\nListado de usuarios registrados:")
        for usuario in usuarios:
            print(f"ID: {usuario['id']}, Nombre: {usuario['nombre']}, Apellidos: {usuario['apellidos']}, Teléfono: {usuario['telefono']}, Correo: {usuario['correo']}")

    elif opcion == 'C':
        id_usuario = int(input("Ingrese el ID del usuario que desea consultar: "))
        for usuario in usuarios:
            if usuario['id'] == id_usuario:
                print(f"\nInformación del usuario con ID {id_usuario}:")
                print(f"Nombre: {usuario['nombre']}, Apellidos: {usuario['apellidos']}, Teléfono: {usuario['telefono']}, Correo: {usuario['correo']}")
                break
        else:
            print("No se encontró ningún usuario con el ID especificado.")

    elif opcion == 'D':
        id_usuario = int(input("Ingrese el ID del usuario que desea editar: "))
        for usuario in usuarios:
            if usuario['id'] == id_usuario:
                print(f"\nEditando información del usuario con ID {id_usuario}:")
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
                break
        else:
            print("No se encontró ningún usuario con el ID especificado.")

    elif opcion == 'E':
        print("Gracias por utilizar el programa. ¡Hasta luego!")
        break
    
    else:
        print("Opción inválida. Por favor seleccione una opción válida.")

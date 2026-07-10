# ===============================
# Sistema FitPass - Evaluación Transversal
# ===============================

# Lista de planes
planes = [
    {"F001": ["Plan Básico", "mensual", 1, False, False, "libre"]},
    {"F002": ["Plan Full", "mensual", 1, True, True, "libre"]},
    {"F003": ["Plan Estudiante", "trimestral", 3, False, True, "tarde"]},
    {"F004": ["Plan Senior", "trimestral", 3, True, False, "mañana"]},
    {"F005": ["Plan Anual Pro", "anual", 12, True, True, "libre"]},
    {"F006": ["Plan Nocturno", "mensual", 1, False, True, "noche"]},
]

# Lista de inscripciones (precio y cupos)
inscripciones = [
    {"F001": [14990, 30]},
    {"F002": [22990, 10]},
    {"F003": [39990, 0]},
    {"F004": [35990, 6]},
    {"F005": [159990, 2]},
    {"F006": [18990, 15]},
]

# Funciones de validación
def validar_codigo(codigo):
    return codigo.upper().strip() != "" and all(codigo.upper().strip() not in list(p.keys())[0] for p in planes)

def validar_nombre(nombre):
    return nombre.strip() != ""

def validar_tipo(tipo):
    return tipo.lower() in ["mensual", "trimestral", "anual"]

def validar_duracion(duracion):
    return duracion.isdigit() and int(duracion) > 0

def validar_sn(valor):
    return valor.lower() in ["s", "n"]

def validar_horario(horario):
    return horario.strip() != ""

def validar_precio(precio):
    return precio.isdigit() and int(precio) > 0

def validar_cupos(cupos):
    return cupos.isdigit() and int(cupos) >= 0


# Funciones principales
def cupos_por_tipo(tipo):
    total = 0
    for plan in planes:
        clave = list(plan.keys())[0]
        datos = plan[clave]
        if datos[1].lower() == tipo.lower():
            for ins in inscripciones:
                clave_ins = list(ins.keys())[0]
                if clave_ins == clave:
                    total += ins[clave_ins][1]
    print("El total de cupos disponibles es:", total)

def buscar_por_precio(minimo, maximo):
    resultados = []
    for ins in inscripciones:
        clave = list(ins.keys())[0]
        precio, cupos = ins[clave]
        if minimo <= precio <= maximo and cupos > 0:
            for plan in planes:
                clave_plan = list(plan.keys())[0]
                if clave_plan == clave:
                    nombre = plan[clave_plan][0]
                    resultados.append(f"{nombre}---{clave}")
    if resultados:
        print("Planes encontrados:", sorted(resultados))
    else:
        print("No hay planes en ese rango de precios.")

def actualizar_precio(codigo, nuevo_precio):
    for ins in inscripciones:
        clave = list(ins.keys())[0]
        if clave.upper() == codigo.upper().strip():
            ins[clave][0] = nuevo_precio
            return True
    return False

def agregar_plan():
    codigo = input("Ingrese código nuevo: ").upper().strip():
    if not validar_codigo(codigo):
        print("Código inválido o ya existe.")
        return

    nombre = input("Ingrese nombre del plan: ")
    if not validar_nombre(nombre):
        print("Nombre inválido.")
        return

    tipo = input("Ingrese tipo (mensual/trimestral/anual): ")
    if not validar_tipo(tipo):
        print("Tipo inválido.")
        return

    duracion = input("Ingrese duración en meses: ")
    if not validar_duracion(duracion): 
        print("Duración inválida.")
        return

    piscina = input("¿Acceso a piscina? (s/n): ")
    if not validar_sn(piscina):
        print("Valor inválido.")
        return

    clases = input("¿Incluye clases grupales? (s/n): ")
    if not validar_sn(clases):
        print("Valor inválido.")
        return

    horario = input("Ingrese horario: ")
    if not validar_horario(horario):
        print("Horario inválido.")
        return

    precio = input("Ingrese precio: ")
    if not validar_precio(precio):
        print("Precio inválido.")
        return

    cupos = input("Ingrese cupos: ")
    if not validar_cupos(cupos):
        print("Cupos inválidos.")
        return

    planes.append({codigo: [nombre, tipo.lower(), int(duracion), piscina.lower() == "s", clases.lower() == "s", horario]})
    inscripciones.append({codigo: [int(precio), int(cupos)]})
    print("Plan agregado correctamente.")

def eliminar_plan(codigo):
    for plan in planes:
        clave = list(plan.keys())[0]
        if clave.upper() == codigo.upper().strip():
            planes.remove(plan)
            break
    for ins in inscripciones:
        clave = list(ins.keys())[0]
        if clave.upper() == codigo.upper().strip():
            inscripciones.remove(ins)
            return True
    return False

# Menú principal
def menu():
    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Cupos por tipo de plan")
        print("2. Búsqueda de planes por rango de precio")
        print("3. Actualizar precio de plan")
        print("4. Agregar plan")
        print("5. Eliminar plan")
        print("6. Salir")
        print("====================================")

        try:
            opcion = int(input("Ingrese opción: "))
        except ValueError:
            print("Debe ingresar un número entero")
            continue

        if opcion == 1:
            tipo = input("Ingrese tipo de plan: ")
            cupos_por_tipo(tipo)

        elif opcion == 2:
            try:
                minimo = int(input("Ingrese precio mínimo: "))
                maximo = int(input("Ingrese precio máximo: "))
                buscar_por_precio(minimo, maximo)
            except ValueError:
                print("Debe ingresar números enteros.")

        elif opcion == 3:
            codigo = input("Ingrese código del plan: ")
            try:
                nuevo_precio = int(input("Ingrese nuevo precio: "))
                if actualizar_precio(codigo, nuevo_precio):
                    print("Precio actualizado.")
                else:
                    print("El código no existe.")
            except ValueError:
                print("Precio inválido.")

        elif opcion == 4:
            agregar_plan()

        elif opcion == 5:
            codigo = input("Ingrese código del plan a eliminar: ")
            if eliminar_plan(codigo):
                print("Plan eliminado.")
            else:
                print("El código no existe.")

        elif opcion == 6:
            print("Programa finalizado.")
            break

# Ejecutar programa
menu()


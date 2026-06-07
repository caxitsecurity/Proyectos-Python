def sumar(a: float, b: float) -> float:
    return a + b


def restar(a: float, b: float) -> float:
    return a - b


def multiplicar(a: float, b: float) -> float:
    return a * b


def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b


def pedir_numero(mensaje: str) -> float:
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Ingresa un número válido.")


def mostrar_menu() -> None:
    print("\n=== Calculadora CLI ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")


def main() -> None:
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "5":
            print("Saliendo de la calculadora.")
            break

        if opcion not in {"1", "2", "3", "4"}:
            print("Opción inválida.")
            continue

        numero_a = pedir_numero("Ingresa el primer número: ")
        numero_b = pedir_numero("Ingresa el segundo número: ")

        try:
            if opcion == "1":
                resultado = sumar(numero_a, numero_b)
            elif opcion == "2":
                resultado = restar(numero_a, numero_b)
            elif opcion == "3":
                resultado = multiplicar(numero_a, numero_b)
            else:
                resultado = dividir(numero_a, numero_b)

            print(f"Resultado: {resultado}")
        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()

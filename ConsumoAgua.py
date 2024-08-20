class CalcularPagoConsumoAgua:
    
    A = float(input("Ingrese el valor de la altura (A) de la alberca en metros: "))
    L = float(input("Ingrese el valor del largo (L) de la alberca en metros: "))
    Ancho = float(input("Ingrese el valor del ancho de la alberca en metros: "))
    Costo_MetroCubico = float(input("Ingrese el costo por metro cúbico de agua: "))

    Volumen = A * L * Ancho

    
    Pago = Volumen * Costo_MetroCubico

    print(f"El volumen de la alberca es: {Volumen:.2f} metros cúbicos")
    print(f"El pago total por llenar la alberca es: {Pago:.2f} moneda")

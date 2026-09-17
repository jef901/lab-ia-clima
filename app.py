def calcular_impuesto(monto):
    if monto < 0:
        raise ValueError("El monto no puede ser negativo")
    return monto * 0.22  # Simulamos el IVA

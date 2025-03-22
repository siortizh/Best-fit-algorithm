def best_fit(mem_avail, req, index):
    if not mem_avail or req <= 0:
        return None

    # Inicializar variables para el mejor ajuste
    best_fit_index = -1
    best_fit_size = float('inf')
    best_fit_base = 0
    best_fit_limit = 0

    # Longitud de la lista de memoria disponible
    n = len(mem_avail)

    # Recorrer la lista de manera circular
    for i in range(n):
        current_index = (index + i) % n
        base, limit = mem_avail[current_index]

        # Verificar si el bloque actual puede satisfacer la solicitud
        if limit >= req:
            # Verificar si es el mejor ajuste hasta ahora
            if limit < best_fit_size:
                best_fit_size = limit
                best_fit_index = current_index
                best_fit_base = base
                best_fit_limit = limit

    # Si no se encontró un bloque adecuado
    if best_fit_index == -1:
        return None

    # Actualizar la lista de memoria disponible
    if best_fit_limit == req:
        # Si el bloque se agota completamente, eliminarlo
        mem_avail.pop(best_fit_index)
    else:
        # Si queda espacio, actualizar el bloque
        mem_avail[best_fit_index] = (best_fit_base + req, best_fit_limit - req)


    # Devolver el resultado en el formato especificado
    return (mem_avail, best_fit_base, req, best_fit_index)
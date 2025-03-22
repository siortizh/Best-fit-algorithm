def best_fit(mem_avail, req, index):
    if not mem_avail or req <= 0:
        return None

    best_index = -1
    size = float('inf')
    best_base = 0
    best_limit = 0

    n = len(mem_avail)

    for i in range(n):
        current_index = (index + i) % n
        base, limit = mem_avail[current_index]

        if limit >= req:
            if limit < size:
                size = limit
                best_index = current_index
                best_base = base
                best_limit = limit

    if best_index == -1:
        return None

    if best_limit == req:
        mem_avail.pop(best_index)
    else:
        mem_avail[best_index] = (best_base + req, best_limit - req)

    return (mem_avail, best_base, req, best_index)
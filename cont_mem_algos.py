def best_fit(mem_availe, req, index):
    size = float('inf')
    index = -1
    best_base = None
    best_limit = None
    
    start_index = 0

    for i in range(len(mem_availe)):
        current_index = (start_index + i) % len(mem_availe)
        base, limit = mem_availe[current_index]
        
        if base > limit:
            base, limit = limit, base
        
        block_size = limit - base
        
        if block_size >= req and block_size < size:
            size = block_size
            index = current_index
            best_limit = limit
            best_base = base
            

    if index == -1:
        print(f"Not enough memory for request: {hex(req)}")
        return None
    
    limit = best_limit
    base = best_base

    if limit >= req:
        if limit - req == 0:
            print(f"Removing block at index {index}: Base = {hex(base)}, Limit = {hex(limit)}")
            mem_availe.pop(index)
            return mem_availe, base, req, index
        else:
            mem_availe[index] = (limit, base + req)
            print(f"Updating block at index {index}: New Base = {hex(base + req)}, New Limit = {hex(limit)}")
            return mem_availe, base, req, index
    else:
        print(f"Not enough memory for request: {hex(req)}")
        return None

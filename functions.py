def process_node(inner, key, value):
    if isinstance(value, dict):
        nodes = tuple(map(lambda kv: process_node(inner, kv[0], kv[1]), value.items()))
        return {key: nodes}
    else:
        return {key: inner[value]}

def flatten_dict(nested_dict):
    flattened = {}
    for key, value in nested_dict.items():
        if isinstance(value, dict):
            flattened.update(flatten_dict(value))
        else:
            flattened[key] = value
    return flattened

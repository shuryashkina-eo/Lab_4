# TODO решите задачу
def task() -> float:
    with open('input.json') as f:
        import json
        file = json.load(f)
        b = 0
        for i in file:
            a = i["score"] * i["weight"]
            b += a
    return (round(b, 3))

print(task())

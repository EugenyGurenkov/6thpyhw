def same_by(characteristic, objects):
    return all(characteristic(x) == characteristic(objects[0]) for x in objects)


values = [0, 2, 10, 6]
# values = [1, 2, 3, 4]
if same_by(lambda x: x % 2, values):
    print('Одно и то же')
else:
    print('Не одно и то же')
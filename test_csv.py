import csv



data = [
    {'name':'John', 'age':20}
]

with open('test.csv', 'a', encoding='utf-8') as file:
    headers = ['name', 'age']
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    for i in data:
        writer.writerow(i)
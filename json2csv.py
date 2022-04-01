import json

with open('/home/vhessel/Downloads/products(1).json', encoding='utf-8') as meu_json:
    products_json = json.load(meu_json)
    products = products_json['products'] 

csv_open = open('products.csv', 'w')
data = 'product,plu\n'

for key in products:
    data = data + '{0},{1}\n'.format(
                    str(key),
                    str(products[key][0].get('dynID', ''))
                )
csv_open.write(data)
csv_open.close()

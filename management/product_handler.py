from menu import products


def get_product_by_id(product_id):

    if not (type(product_id) is int):
        raise TypeError('product id must be an int')
    for item in products:
        if item['_id'] == product_id:
            return (item)
    return {}


def get_products_by_type(product_type):
    if not (type(product_type) is str):
        raise TypeError('product type must be a str')
    item_by_types = []
    for item in products:
        if item['type'] == product_type:
            item_by_types.append(item)
    return (item_by_types)


def add_product(menu, **new_product):
    id_list = []
    new_id = 1
    for item in menu:
        if len(menu) > 0:
            id_list.append(item['_id'])
            id_list = ((sorted(id_list)))
            new_id = id_list[-1]+1
            new_product['_id'] = new_id
    new_product['_id'] = new_id
    menu.append(new_product)
    return new_product


def menu_report():
    product_count = len(products)
    price_products = []
    average_price = 0
    types_list = []
    types_and_quant = []
    quant_occurrence = []
    most_common_type = ''

    for item in products:
        price_products.append(item['price'])
        types_list.append(item['type'])
    average_price = round(((sum(price_products))/product_count), 2)
    
    
    for type in types_list:
        quant_occurrence.append(types_list.count(type))
        types_and_quant.append({'type': type,  'quant': types_list.count(type)})

    for i in types_and_quant:
        if i['quant'] == sorted(quant_occurrence)[-1]:
            most_common_type = i['type']
            break
    return f"Products Count: {product_count} - Average Price: ${average_price} - Most Common Type: {most_common_type}"
    

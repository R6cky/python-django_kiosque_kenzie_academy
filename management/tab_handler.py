from menu import products


def calculate_tab(dic_list):
    items_sum = []
    for item in products:
        for dic in dic_list:
            if item["_id"] == dic['_id']:
                items_sum.append(item['price'] * dic["amount"])
    return {"subtotal": f'${round((sum(items_sum)), 2)}'}

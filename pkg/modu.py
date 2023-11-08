import json
def triangle_zhonxin(a: tuple, b: tuple, c: tuple) -> tuple:
    """
    Calculate the centroid of a triangle given its three vertices.

    Args:
        a (tuple): Coordinates of vertex A.
        b (tuple): Coordinates of vertex B.
        c (tuple): Coordinates of vertex C.

    Returns:
        tuple: Coordinates of the centroid.
    """
    x = round((a[0] + b[0] + c[0]) / 3)
    y = round((a[1] + b[1] + c[1]) / 3)
    return (x, y)

def write_json(data: dict, file_name: str) -> None:
    """
    將字典轉換為JSON格式並寫入檔案。

    Args:
        data (dict): 要寫入的字典。
        file_name (str): 輸出檔案名稱。
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def process_data(data: dict, discount: float) -> None:
    """
    將字典中每個菜品的價格打折。

    Args:
        data (dict): 包含菜單資訊的字典。
        discount (float): 打折折數，例如0.9表示9折。
    """
    for category in data['categories']:
        for item in category['items']:
            item['price'] = int(item['price']*discount)

def print_json(data: dict) -> None:
    json_str = json.dumps(data, ensure_ascii=False, indent=4)
    print(json_str)

def read_json(file_name: str) -> dict:
    """
    讀取一個JSON檔案並轉換為字典後回傳。

    Args:
        file_name (str): JSON檔案名稱。

    Returns:
        dict: 轉換後的字典。
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

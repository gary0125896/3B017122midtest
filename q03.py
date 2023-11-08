import json
from pkg.modu import print_json, process_data, read_json, write_json

# 定義常數
MENU_FILE = 'menu.json'       # 輸入檔案名稱
OUTPUT_FILE = 'output.json'   # 輸出檔案名稱
if __name__ == "__main__":
    # 讀取菜單資訊
    menu_data = read_json(MENU_FILE)

    # 印出原始菜單
    print("原始菜單：")
    print_json(menu_data)
    # 新增資料到菜單
    new_item = {
        "name": "海鮮燉飯",
        "price": 239,
        "description": "西班牙的代表美食，海鮮配料豐富、色彩繽紛"
    }
    menu_data['categories'][1]['items'].append(new_item)
    # 處理菜單資訊（打折）
    a = float(input("請輸入折扣率(0.0 ~ 1.0):"))
    discount = a
    process_data(menu_data, discount)

    # 印出處理後的菜單
    print("\n打折後的菜單：")
    print_json(menu_data)

    # 寫入處理後的菜單到輸出檔案
    write_json(menu_data, OUTPUT_FILE)

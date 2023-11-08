from pkg import modu
print("請輸入三角形的 3 個頂點坐標")
print("------------------------------")
# 輸入三個點的座標
a = tuple(map(float, input("請輸入頂點 a 的坐標：").split(',')))
b = tuple(map(float, input("請輸入頂點 b 的坐標：").split(',')))
c = tuple(map(float, input("請輸入頂點 c 的坐標：").split(',')))
print("------------------------------")
# 調用 triangle_zhonxin 函數
center = modu.triangle_zhonxin(a, b, c)

# 輸出三角形的重心
print(f"此三角形的重心為：({center[0]}, {center[1]})")
